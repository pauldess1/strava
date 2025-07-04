import pandas as pd
from geopy.distance import great_circle
import random
from datetime import timedelta
from utils import get_elevation, add_white_noise


class TrajectoryManager:
    def __init__(self, coords, pace, start_time):
        self.coords = coords
        self.pace = self.pace_formatter(pace)
        self.start_time = start_time
        self.distance = self.compute_distance(coords)
        self.time = int(self.pace * self.distance)
        self.timeline = self.compute_timeline(self.time)
        self.trajectory = self.create_trajectory()
        self.output = self.create_running_df()

    def compute_distance(self, coords):
        distance = 0
        for i in range(len(coords) - 1):
            distance += great_circle(coords[i], coords[i + 1]).km
        return distance

    def pace_formatter(self, pace):
        return pace[0] * 60 + pace[1]

    def compute_timeline(self, time):
        actual_time = 0.0
        timeline = [actual_time]
        while actual_time < time - 6:
            actual_time += float(random.randint(1, 5))
            timeline.append(actual_time)
        timeline.append(time)
        return timeline

    def create_trajectory(self):
        time_step = 0.5
        num_points = int(self.time // time_step) + 1

        trajectory = []
        segment_distances = []
        total_distance = 0
        for i in range(len(self.coords) - 1):
            d = great_circle(self.coords[i], self.coords[i + 1]).km
            segment_distances.append(d)
            total_distance += d

        # Interpolation
        for step in range(num_points):
            t = step * time_step
            dist_traveled = (t / self.time) * total_distance

            dist_acc = 0
            for i, seg_dist in enumerate(segment_distances):
                if dist_acc + seg_dist >= dist_traveled:
                    ratio = (dist_traveled - dist_acc) / seg_dist
                    lat1, lon1 = self.coords[i]
                    lat2, lon2 = self.coords[i + 1]
                    lat = lat1 + ratio * (lat2 - lat1)
                    lon = lon1 + ratio * (lon2 - lon1)
                    lat, lon = add_white_noise(lat, lon)
                    elevation = get_elevation(lat, lon, "paris.tif")
                    trajectory.append([lat, lon, t, elevation])
                    break
                dist_acc += seg_dist
        return pd.DataFrame(trajectory, columns=["lat", "long", "time", "ele"])

    def create_running_df(self):
        filtered_df = self.trajectory[
            self.trajectory["time"].isin(self.timeline)
        ].reset_index(drop=True)

        for index, row in filtered_df.iterrows():
            delta = timedelta(seconds=row["time"])
            date = (self.start_time + delta).strftime("%Y-%m-%dT%H:%M:%SZ")
            filtered_df.at[index, "time"] = date
        return filtered_df

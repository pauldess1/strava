import pandas as pd
from geopy.distance import great_circle
import random


class TrajectoryManager:
    def __init__(self, coords, pace, start_time):
        self.coords = coords
        self.trajectory = pd.DataFrame(
            columns=["lat", "long", "elevation", "time", "hr", "cadence"]
        )
        self.pace = self.pace_formatter(pace)
        self.start_time = start_time
        self.distance = self.compute_distance(coords)
        self.timeline = self.compute_timeline(self.distance, self.pace)
        print(self.timeline)

    def compute_distance(self, coords):
        distance = 0
        for i in range(len(coords) - 1):
            distance += great_circle(coords[i], coords[i + 1]).km
        return distance

    def pace_formatter(self, pace):
        return pace[0] * 60 + pace[1]

    def compute_timeline(self, distance, pace):
        time = int(pace * distance)
        actual_time = 0
        timeline = [actual_time]
        while actual_time < time - 6:
            actual_time += random.randint(1, 5)
            timeline.append(actual_time)
        timeline.append(time)
        return timeline


coords = [
    (48.76179, 2.306828),
    (48.761451, 2.308116),
    (48.770955, 2.311807),
    (48.770333, 2.316484),
]
tm = TrajectoryManager(coords, [4, 30], 8)

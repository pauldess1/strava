from typing import List, Tuple
import rasterio
import numpy as np
from rasterio.transform import from_origin
from rasterio.sample import sample_gen


def interpolate_line(
    points: List[Tuple[float, float]], num_points_between: int = 10
) -> List[Tuple[float, float]]:
    """
    Interpole une ligne entre les points donnés en générant `num_points_between`
    points intermédiaires entre chaque paire de points.

    Args:
        points: liste de tuples (lat, lon)
        num_points_between: nombre de points à générer entre chaque paire

    Returns:
        Liste de tuples (lat, lon) incluant les points originaux + points interpolés
    """
    if not points or len(points) < 2:
        return points

    interpolated_points = []

    for i in range(len(points) - 1):
        start = points[i]
        end = points[i + 1]

        interpolated_points.append(start)  # on ajoute le point de départ

        # interpolation linéaire entre start et end
        for j in range(1, num_points_between + 1):
            lat = start[0] + (end[0] - start[0]) * j / (num_points_between + 1)
            lon = start[1] + (end[1] - start[1]) * j / (num_points_between + 1)
            interpolated_points.append((lat, lon))

    interpolated_points.append(points[-1])  # on ajoute le dernier point

    return interpolated_points


def get_elevation(lat, lon, path):
    with rasterio.open(path) as dataset:
        coords = [(lon, lat)]
        for val in sample_gen(dataset, coords):
            return val[0]


def convert_hgt_to_tif(hgt_path, tif_path):
    width = height = 3601
    dtype = np.int16

    with open(hgt_path, "rb") as f:
        data = np.fromfile(f, dtype=">i2").reshape((height, width))
    import re

    match = re.match(r"([NS])(\d+)([EW])(\d+)", hgt_path.split("/")[-1].split("\\")[-1])
    if not match:
        raise ValueError("Nom de fichier .hgt non reconnu")

    lat_sign = 1 if match.group(1) == "N" else -1
    lat = lat_sign * int(match.group(2))
    lon_sign = 1 if match.group(3) == "E" else -1
    lon = lon_sign * int(match.group(4))
    transform = from_origin(
        lon, lat + 1, 1 / 1200, 1 / 1200
    )  # 1° divisé par 1200 pour la résolution

    with rasterio.open(
        tif_path,
        "w",
        driver="GTiff",
        height=height,
        width=width,
        count=1,
        dtype=dtype,
        crs="EPSG:4326",
        transform=transform,
    ) as dst:
        dst.write(data, 1)

    print(f"Conversion terminée : {tif_path}")

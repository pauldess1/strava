from typing import List, Tuple


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

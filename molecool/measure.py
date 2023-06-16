"""
This file contains functions relevant to measure properties of molecules.
"""

import numpy as np


def calculate_distance(rA, rB):
    """
    Calculate the distance between two atoms in a space given by their Cartesian coordinates.

    Parameters
    ----------
    rA, rB : np.ndarray
        The coordinates of each point.

    Returns
    -------
    distance : float
        The distance between the two points.

    Examples
    --------
    >>> r1 = np.array([0.0, 0.0, 0.0])
    >>> r2 = np.array([0.0, 0.0, 1.0])
    >>> calculate_distance(r1, r2)
    1.0
    """

    d = rA - rB
    dist = np.linalg.norm(d)
    return dist


def calculate_angle(rA, rB, rC, degrees=False):
    """
    Calculate the angle between three points in a space given by their Cartesian coordinates.

    Parameters
    ----------
    rA, rB, rC : np.ndarray
        The coordinates of each point.
    degrees : bool, optional
        Return the calculated angle in degrees.

    Returns
    -------
    angle : float
        The angle between the three points.

    Examples
    --------
    >>> r1 = np.array([0.0, 0.0, 0.0])
    >>> r2 = np.array([0.0, 0.0, 1.0])
    >>> r3 = np.array([0.0, 1.0, 0.0])
    >>> calculate_angle(r1, r2, r3, degrees=True)
    90.0
    """

    AB = rB - rA
    BC = rB - rC
    theta = np.arccos(np.dot(AB, BC) / (np.linalg.norm(AB) * np.linalg.norm(BC)))

    if degrees:
        return np.degrees(theta)
    else:
        return theta

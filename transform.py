from math import cos, pi, sin

from matrix import *

def rotate3(z, y, x): # note: rotated around origin
    return (
        Matrix([
        [cos(z),    -sin(z),    0, 0],
        [sin(z),    cos(z),     0, 0],
        [0,         0,          1, 0],
        [0,         0,          0, 1]]) *
        Matrix([
        [cos(y),    0,  -sin(y),    0],
        [0,         1,  0,          0],
        [sin(y),    0,  cos(y),     0],
        [0,         0,  0,          1]]) *
        Matrix([
        [1, 0,      0,          0],
        [0, cos(x), -sin(x),    0],
        [0, sin(x), cos(x),     0],
        [0, 0,      0,          1]])
    )

def scale3(x, y, z):
    return Matrix([
        [x, 0, 0, 0],
        [0, y, 0, 0],
        [0, 0, z, 0],
        [0, 0, 0, 1]])

def translate3(dx, dy, dz):
    return Matrix([
        [1, 0, 0, dx],
        [0, 1, 0, dy],
        [0, 0, 1, dz],
        [0, 0, 0, 1]])

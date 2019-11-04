#!/usr/bin/python3

import sys
import math

def result(Vx, Vy, Vz, X, Y, Z, d):
    print("The velocity vector of the ball is:")
    print("(" + format(Vx, '.2f') + ", " + format(Vy, '.2f') + ", " + format(Vz, '.2f') + ")")
    print("At time t + 4, ball coordinates will be:")
    print("(" + format(X, '.2f') + ", " + format(Y, '.2f') + ", " + format(Z, '.2f') + ")")
    if ():
        print("The ball won't reach the paddle.")
    else:
        print("The incidence angle is:")
        print(format(d, '.2f') + " degrees")

def var_d(av):
    x0 = float(av[1])
    x1 = float(av[4])
    y0 = float(av[2])
    y1 = float(av[5])
    z0 = float(av[3])
    z1 = float(av[6])
    n = float(av[7])
    calcul(x0, x1, y0, y1, z0, z1, n)

def calcul(x0, x1, y0, y1, z0, z1, n):
    Vx = x1 - x0
    Vy = y1 - y0
    Vz = z1 - z0
    X = Vx * n + x1
    Y = Vy * n + y1
    Z = Vz * n + z1
    d = 0
    result(Vx, Vy, Vz, X, Y, Z, d)

def main():
    av = sys.argv
    var_d(av)

if __name__ == "__main__":
    main()
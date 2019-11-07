#!/usr/bin/python3

import sys
import math

def h():
    print("USAGE")
    print("    ./101pong x0 y0 z0 x1 y1 z1 n")
    print("")
    print("DESCRIPTION")
    print("    x0 ball abscissa at time t - 1")
    print("    y0 ball ordinate at time t - 1")
    print("    z0 ball altitude at time t - 1")
    print("    x1 ball abscissa at time t")
    print("    y1 ball ordinate at time t")
    print("    z1 ball altitude at time t")
    print("    n  time shift (greater than or equal to zero, integer)")

def result(Vx, Vy, Vz, X, Y, Z, ta):
    print("The velocity vector of the ball is:")
    print("(" + format(Vx, '.2f') + ", " + format(Vy, '.2f') + ", " + format(Vz, '.2f') + ")")
    print("At time t + 4, ball coordinates will be:")
    print("(" + format(X, '.2f') + ", " + format(Y, '.2f') + ", " + format(Z, '.2f') + ")")
    if (Vx < Vy and Vz < Vy):
        print("The incidence angle is:")
        print(format(ta, '.2f') + " degrees")
    else:
        print("The ball won't reach the paddle.")

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
    t = math.sqrt(math.pow(abs(Vx), 2) + math.pow(abs(Vy), 2) + math.pow(abs(Vz), 2))
    te = math.degrees(abs(Vz)/t)
    result(Vx, Vy, Vz, X, Y, Z, te)

def main():
    av = sys.argv
    if (av[1] == "-h"):
        h()
    else:
        var_d(av)

if __name__ == "__main__":
    main()
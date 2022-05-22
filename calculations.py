import math
import random


def solve_quadratic(a,b,c):
    try:
        a, b, c = float(a), float(b), float(c)
        sol = [(-b + math.sqrt((b * b) - (4 * a * c))) / (2 * a), (-b - math.sqrt((b * b) - (4 * a * c))) / (2 * a)]
    except:
        sol = ["No Real Solutions"]

    return sol

def pyramid_calc(height,base,slant,perimeter):
    s_area=base+(perimeter*slant*0.5)
    volume=1/3*base*height
    return [s_area, volume]

def generate_quadratic():
    a=str(random.randint(1,50))
    b=str(random.randint(1,50))
    c=str(random.randint(1,50))
    return [solve_quadratic(a, b, c), [a,b,c]]
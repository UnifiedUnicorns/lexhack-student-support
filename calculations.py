import math
import random


def solve_quadratic(a,b,c):
    try:
        a, b, c = float(a), float(b), float(c)
        sol = [(-b + math.sqrt((b * b) - (4 * a * c))) / (2 * a), (-b - math.sqrt((b * b) - (4 * a * c))) / (2 * a)]
    except:
        sol = ["No Real Solutions"]

    return sol

def generate_quadratic():
    a=str(random.randint(1,50))
    b=str(random.randint(1,50))
    c=str(random.randint(1,50))
    return [solve_quadratic(a, b, c), [a,b,c]]
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
    height, base, slant, perimeter = float(height), float(base), float(slant), float(perimeter)
    s_area = base+(perimeter*slant*0.5)
    volume = 1/3*base*height
    return [s_area, volume]


def sphere_calc(radius):
    radius = float(radius)
    s_area = 4*math.pi*(radius*radius)
    volume = 4/3*math.pi*(radius*radius*radius)
    return [s_area, volume]


def cyl_calc(r, h):
    r, h = float(r), float(h)
    base = r*r*math.pi
    base_cir = (r+r)*math.pi
    vol = base * h
    sur_ar = (base_cir*h)+(2*base)
    return [sur_ar, vol]


def prism_calc(height,area,perimeter):
    height,area,perimeter=float(height),float(area),float(perimeter)
    s_area=(2*area)+(perimeter*height)
    volume=height*area
    return [s_area,volume]


def circle_calc(radius):
    radius=float(radius)
    area=math.pi*radius*radius
    circum=2*math.pi*radius
    return [area,circum]


def triangle_calc(s1,s2,s3):
    s1, s2, s3 = float(s1), float(s2), float(s3)
    perimeter = s1+s2+s3
    s = perimeter/2
    area = math.sqrt(s*(s - s1)*(s - s2)*(s - s3))
    return [area,perimeter,s]


def generate_quadratic():
    a=str(random.randint(1,50))
    b=str(random.randint(1,50))
    c=str(random.randint(1,50))
    return [solve_quadratic(a, b, c), [a,b,c]]


def rect_calc(b,h):
    b,h = float(b), float(h)
    area = b*h
    per = (2*b)+(2*h)

    return [area, per]


def trap_calc(h, b, b1, s, s1):
    h, b, b1, s, s1 = float(h), float(b), float(b1), float(s), float(s1)
    area = (b+b1)*h/2
    per = b+b1+s+s1

    return [area, per]


def rhomb_calc(s, d, d1):
    s, d, d1 = float(s), float(d), float(d1)
    area = (d*d1)/2
    per = 4*s

    return [area, per]


def calc_reg_polygon(s, l):
    s, l = float(s), float(l)
    a = (s/2)/(math.tan(math.radians(360/(2*s))))
    p = l*s
    return [(p*a)/2, p]

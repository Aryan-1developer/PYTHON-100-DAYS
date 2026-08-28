import colorgram
import random
from turtle import Turtle, Screen


colors = colorgram.extract(r"C:\Users\Aryan Singh\Desktop\PYTHON 100 DAYS\Day 18\image.jpeg", 30)

rgb_colors = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb_colors.append((r, g, b))

print(rgb_colors)

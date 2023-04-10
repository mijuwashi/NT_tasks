def inside(cir_x, cir_y, radius, x_point, y_point):
    if ((x_point - cir_x) * (x_point - cir_x) +
            (y_point - cir_y) * (y_point - cir_y) == radius * radius):
        return 0
    elif ((x_point - cir_x) * (x_point - cir_x) +
          (y_point - cir_y) * (y_point - cir_y) < radius * radius):
        return 1
    elif ((x_point - cir_x) * (x_point - cir_x) +
          (y_point - cir_y) * (y_point - cir_y) > radius * radius):
        return 2


circle_x, circle_y, rad = map(float, input().split())
x, y = map(float, input().split())
print(inside(circle_x, circle_y, rad, x, y))

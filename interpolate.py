print("Linear:")
print('-'*40)
def linear_interpolate(points):
    x0, y0 = points[0]
    x1, y1 = points[1]
   
    m = (y1 - y0) / (x1 - x0)
    c = x0 - m * x0 #ponto onde intercepta o eixo y
    print(f"m = {m}, c = {c}")
    def linear_function(x_val):
        return m * x_val + c # valor de y = linha interpolada pelo eixo y


    return linear_function




points = [(0.1, 1.221), (0.6, 3.32)]
linear_function = linear_interpolate(points)


x_new = 2.5
y_new = linear_function(x_new)
print(f"The linear interpolated  value at x = {x_new} is y = {y_new}")


print('-'*100)




def interpolate(points):
    x = [point[0] for point in points]
    y = [point[1] for point in points]


    a0 = y[0]
    a1 = (y[1] - y[0]) / (x[1] - x[0])
    a2 = (((y[2] - y[1]) / (x[2] - x[1])) - a1) / (x[2] - x[0])
    print(f"a0 = {a0}, a1 = {a1}, a2 = {a2}")
    def polynomial(x_val):
        return a0 + a1 * (x_val - x[0]) + a2 * (x_val - x[0]) * (x_val - x[1])


    return polynomial


points = [(0.1, 1.221), (0.6, 3.320), (0.8, 4.953)]


poly_function = interpolate(points)


x_new = 0.2
y_new = poly_function(x_new)
print(f"The Polynomial interpolated value at x = {x_new} is y = {y_new}")



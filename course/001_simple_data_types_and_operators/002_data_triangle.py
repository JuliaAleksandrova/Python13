side_a = float(input('Enter side A: '))
side_c = float(input('Enter side B: '))
side_b = float(input('Enter side C: '))

half_perimetr = (side_a + side_b + side_c) / 2

print(half_perimetr)

area = (half_perimetr * (half_perimetr - side_a) *
        (half_perimetr - side_b) * (half_perimetr - side_c)) ** 0.5

print('Area of triangle is: ' + str(area)) #zdes nado bylo konvert potomu cto float + str budet float
jfdglh

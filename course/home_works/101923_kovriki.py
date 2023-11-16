def area(w, h):
    return w * h

def perimeter(w, h):
    return (w + h) * 2

def count_materials(order_list):
    result = {}
    for carpet_type in order_list:
        result[carpet_type['size']] = {
                'area': area(carpet_type['width'], carpet_type['height']) * carpet_type['qty'],
               'perimeter': perimeter(carpet_type['width'], carpet_type['height']) * carpet_type['qty']
            }
    return result

def count_total_material(order_counts):
    total_a = 0
    total_p = 0

    for value in order_counts.values():
        total_a += value['area']
        total_p += value['perimeter']
    return {
        'total_area': total_a,
        'total_perimeter': total_p
    }

# keys vozvrawaet kljuci
# values znacenija
# items vozvrasaet spisok kortezej, na 0 indekse kljuc na pervom znacenie


order = [
    {'size': 'small', 'qty': 35, 'width': 60, 'height': 40},
    {'size': 'medium', 'qty': 20, 'width': 80, 'height': 60},
    {'size': 'large', 'qty': 15, 'width': 90, 'height': 90},
    ]

print(count_materials(order))
print(count_total_material(count_materials(order)))



# def rectangle_area(rectangle):
#     width = order['width']
#     height = order['height']
#     return width * height
#
#
# def rectangle_perimeter(rectangle):
#     width = order['width']
#     height = order['height']
#     return (width + height) * 2
#
#
# def material_total(area, perimeter, qty):
#     qty = order['qty']
#     materials = (area + perimeter) * qty
#     return materials
#
# def calculate_materials(rectangle):
#
#
#
#
# #def material_need(rectangle_area, rectangle_perimeter, qty):
#  #   return (rectangle_area + rectangle_perimeter) * qty
#
# print('You need ', material_need, 'sm2')
#
#
#
#
#
#
#
#
# print(rectangle_area(60,40))
# print(rectangle_perimeter(60,40))
# print(material_need(2400,200,35))

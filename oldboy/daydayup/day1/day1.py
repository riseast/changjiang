# -*- coding:utf-8 -*-

cars = ['鲁A11111', '鲁B22222', '京B88888', '鲁C33333', '⿊C12345', '⿊C66666', '沪B00000']

new_cars = []
cou = []
for i in cars:
    new_cars.append(i[0])
print(new_cars)
for c in new_cars:
    co = new_cars.count(c)
    cou.append(co)
print(cou)

print(new_cars)





    # s = i + str(new_cars.count(i))
    # info = dict(zip(i,tuple(new_cars)))
    # print(set(info))
    # print(type(a),type(b))

# print(new_cars)

def get_radius(prompt):
    r=int(input(prompt))
    return r

def get_circle_area(radius):
    S=3.14 * radius * radius
    return S


#반지름 입력 
radius=get_radius('넓이를 구하고자 하는 반지름은? ')

#원의 넓이 
area=get_circle_area(radius)

#출력 
print('반지름', radius,'인 원의 넓이=','3.14','*',radius,'*',radius,'=',area)


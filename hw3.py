'''
할인율과 상품의 할인 가격을 전달받아
상품의 할인 전 가격을 계산하는 코드 작성
▪ 한 상품의 할인 전 가격을 계산하기 위해 함수 get_fixed_price() 정의
▪ 이 함수를 두 번 호출하여 A, B 두 상품의 할인 전 가격을 구함
'''

#할인율 
discount_rate=float(input('할인율(%)은? '))

#할인된 상품 > 할인 전 가격
def get_fixed_price(discount_price, rate):
    first_price=discount_price/(1-(rate/100))
    return first_price

#상품의 할인된 가격 
A_discount=float(input('A상품의 할인된 가격은? '))
B_discount=float(input('B상품의 할인된 가격은? '))

#원가 
A_first_price=get_fixed_price(A_discount,discount_rate)
print('A 상품의 정가는',A_first_price,'원')
B_first_price=get_fixed_price(B_discount,discount_rate)
print('B 상품의 정가는',B_first_price,'원')

shopping_bag={}

def buy(shopping_bag):
    print('[구입]')
    item=input('상품명? ')
    if item=='':
        return False
    n=int(input('수량은? '))
    shopping_bag[item]=n
    print(f'장바구니에 {item}가(이) {n}개 담겼습니다.')
    print()

def show(shopping_bag):
    print(f'>>> 장바구니 보기 : {shopping_bag}')

def find(shopping_bag):
    find_item=input('장바구니에서 확인하고자 하는 상품은? ')
    if find_item in shopping_bag:
        print(f'{find_item}(은)는 {shopping_bag[find_item]}개 담겨 있습니다.')
    else:
        print(f'장바구니에 {find_item}은(는) 없습니다')


while True:
    if buy(shopping_bag)==False:
        break
show(shopping_bag)
find(shopping_bag)



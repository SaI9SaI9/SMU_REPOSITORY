'''
exchange() = 500원 100원 50원 10원 변환 및 출력

'''

def exchange(amount) :
    W500=amount//500    #돈에서 500원
    amount%=500         #500원 바꾸고 남은 돈

    W100=amount//100   #돈에서 100원
    amount%=100         #100원 바꾸고 남은 돈

    W50=amount//50    #돈에서 50원
    amount%=50         #50원 바꾸고 남은 돈

    W10=amount//10    #돈에서 10원
    

    print('500원 동전의 개수 :',W500)
    print('100원 동전의 개수 :',W100)
    print('50원 동전의 개수 :',W50)
    print('10원 동전의 개수 :',W10)

#정수 변환
def get_integer(prompt):
    res=int(input(prompt))
    return res

amount=get_integer('동전으로 교환하고자 하는 금액은? ')
exchange(amount)
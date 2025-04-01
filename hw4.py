'''
영어로 된 이름을 입력 받아 두 줄의 환영 메시지를 완성
▪ 연습문제 6.4와 6.5의 사용자 정의 함수를 약간 변형하여 사용
▪ 첫줄과 두번째줄 중 긴 줄을 기준으로 박스선 길이를 설정
nstr = len(msg1) if (len(msg1) > len(msg2)) else len(msg2)
'''

#줄 긋기 
def rep_char(c,n):
    print(c*n)


#환영 메시지 
def welcome(name):
    msg1=f'Hello {name},'
    msg2=f'Welcome to Seoul.'

    nstr = len(msg1) if (len(msg1) > len(msg2)) else len(msg2)

    rep_char('-',nstr)
    print(msg1)
    print(msg2)
    rep_char('-',nstr)



#이름 입력 
name=str(input('Input his/her name: '))
welcome(name)
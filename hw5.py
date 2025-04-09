'''
 ◆ 사용자로부터세자리수이하의10진정수하나를입력받아
다음과같이각자릿수를한글로읽어주는프로그램작성
    ▪ 임의의한자리10진정수에대한한글문자열을화면상에출력하는
    함수read_single_digit() 작성
    ▪ 임의의세자리10진정수에대한한글문자열을반환하는함수
    read_number() 작성
    ▪ 주프로그램부에서는위두함수를이용해입출력처리담당
'''

#한 자리 10진 정수 > 한글 문자열
def read_single_digit(num):
    if num==0 :
        return '영'
    elif num==1 :
        return '일'
    elif num==2 :
        return '이'
    elif num==3 :
        return '삼'
    elif num==4 :
        return '사'
    elif num==5 :
        return '오'
    elif num==6 :
        return '육'
    elif num==7 :
        return '칠'
    elif num==8 :
        return '팔'
    elif num==9 :
        return '구'
    
#세 자리 10진 정수 > 한글 문자열
def read_number(num):
    str_num=str(num)
    num1=read_single_digit(int(str_num[0]))
    num2=read_single_digit(int(str_num[1]))
    num3=read_single_digit(int(str_num[2]))

    return f'{num1} {num2} {num3}'

#주 프로그램부 
num=int(input('세 자리 정수 입력 '))
res=read_number(num)
print(res)



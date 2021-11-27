print('어서오세요! 상명대학교 카페입니다!')
ame=2000; choco=2500; latte=3000; ade=3500
while True:
    print('1. 아메리카노: %d원'%ame)
    print('2. 핫초코: %4d원' %choco)
    print('3. 카페라떼 %5d원' %latte)
    print('4. 레몬에이드 %6d원' %ade)
    print('0. 주문 끝')
    s=0
    while 1:
        k=input('번호 선택:')
        n=int(input('개수 입력:'))
        if k=='1':
            print('아메리카노%d개 주문접수'%n)
            s=s+ame*n
        elif k=='2':
            print('핫초코%d개 주문접수'%n)
            s=s+choco*n
        elif k=='3':
            print('카페라떼%d개 주문접수'%n)
            s=s+latte*n
        elif k=='4':
            print('레몬에이드%d개 주문접수'%n)
            s=s+ade*n
        elif k=='0':
            break
        else:
            continue
    print('지불하실 금액은 %d원입니다.'%s)
    ans=input('카드결제를 하시려면 1을 현금 결제를 하시려면 2를 입력해주세요:')
    if ans =='1':
        print('결제가 완료되었습니다.')
    else:
        received=int(input("돈을 투입해주세요"))
        if received>=s:
            change=received-s
            print(f"{received}원을 받았습니다. 거스름돈은 {change}원입니다. 또 오세요!")
        else:
            print("금액이 부족합니다. 주문이 취소되었습니다.")
            print("다시 주문하시겠습니까?")
            answer=input("다시 주문하려면 1을 종료하시려면 2를 입력해주세요")

    if answer=='1':
        print("다시 주문해주세요")
    else:
        print("안녕히가세요")
        break
    

def my_coroutine():

    while True:
        value = yield
        print('Received value:', value)


# 코루틴 객체 생성
co = my_coroutine()

# 코루틴 실행 준비
next(co)

# 값을 보내기
co.send('Hello, world!')

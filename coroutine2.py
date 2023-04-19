def my_coroutine():

    while True:
        x = yield
        print('Received:', x)


co = my_coroutine()
next(co)

co.send(10)  # Received: 10
co.send(20)  # Received: 20
co.send(30)  # Received: 30

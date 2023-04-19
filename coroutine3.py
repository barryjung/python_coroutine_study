phone_book = {"john": "123-4567", "jane": "234-5678", "max": "345-6789"}


def search():
    name = yield
    while True:
        if name in phone_book:
            phone_number = phone_book[name]
        else:
            phone_number = "Cannot find the name in the phone book"
        name = yield phone_number


# 코루틴 객체 생성
search_coroutine = search()
next(search_coroutine)

# 검색 예시
result = search_coroutine.send("john")
print(result)

result = search_coroutine.send("jane")
print(result)

result = search_coroutine.send("sarah")
print(result)

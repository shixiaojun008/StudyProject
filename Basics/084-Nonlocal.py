def outer():
    b = 10

    def inner():
        nonlocal b
        print("inner b:", b)
        b =20

        print("outer b:", b)

    inner()


outer()
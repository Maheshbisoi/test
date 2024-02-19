# def outer():
#     name = "mahesh"

#     def inner(name):
#         print(name)
#         name = "ankit"
#         return name

#     name = inner(name)
#     print(name)


# outer()



#by using nonlocal
def outer():
    name = "mahesh"

    def inner():
        nonlocal name
        print(name)
        name = "ankit"

    inner()
    print(name)


outer()

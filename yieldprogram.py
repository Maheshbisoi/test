def generator_func():
    yield "Yield"
    yield "keyword"
    yield "in"
    yield "python"

#constructing a generator object and calling the  generator function
generator_object = generator_func()
print(type(generator_object))  #printing the generator object

for i in generator_object:
    print(i)

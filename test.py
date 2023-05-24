def foo(x):

    x[0] = ['def']

    x[1] = ['abc']

    return id(x)

q = ['abc', 'def']

print(id(q) == foo(q))




a={}

a[2]=1

a[1]=[2,3,4]

print(a[1][1])


def f(x):

    def f1(*args, **kwargs):

           print("Sanfoundry")

    return x(*args, **kwargs)

    return f1
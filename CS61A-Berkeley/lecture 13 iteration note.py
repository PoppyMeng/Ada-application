t=iter(list)
#next(iterator)
s=[3,4,5]
t=iter(s)
next(t)  #cannot say next(s) directly
#iterator is mutable factors

d={xxxxxx}
k=iter(d.keys())
v=iter(d.values())
i=iter(d.items()) #in pairs

map(func, iterable)
filter(func, itrable)
zip(first_iter, second_iter)
reversed(sequence):

list(iterable)
tuple(iterable)
sorted(iterable)

bcd=['b', 'c', 'd']
m=map(lambda x:x.upper(), bcd)
next(m)
'B'

m=map(double, range(3,7))
f=lambda y: y>=10
t=filter(f,m)
next (t)

t=[1,2,3,2,1]
reversed(t)==t? false!
reversed(t) is an iterator already
list(reversed(t))==t? True

d={'a':1, 'b':2}
items=iter(d.items())
is equal to 
items=zip(d.keys(), d.values()))


generator function--use yield, can yield multiple times

def plus_minus(x):
    yield x
    yield -x

t=plus_minus(3)
next(t)----3
next(t)----  -3

generator can yield from iterators
def a_then_b(a,b):
    yield from a 
    yield from b

    equals to:
    for x in a:
        yield x
    for x in b:
        yield x

def countdown(k):
    if k>0:
        yield k
        yield from countdown(k-1)
        #note don't say yield countdown(k-1), 
        # because you cannot yield a generator, 
        # can only yield from it or use for loop

s[:-1]--everything from s except for last letter

if we want to see elements of an iterator, we can choose list(t) to see all, or call next(t) to see next

def prefixes(s):
    if s:
        yield s
        yield from prefixes(s[:-1]):
is equal to:       
def prefixes(s):
    result=[]
    if s:
        result.append(s)
        for x in prefixes(s[:-1]):
            result.append(x)
    return result






    """
    docstring
    """
    raise NotImplementedError




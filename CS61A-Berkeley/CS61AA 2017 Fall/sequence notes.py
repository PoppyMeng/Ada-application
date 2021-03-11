class link:
    empty=()
    def __init__(self,first,rest=empty):
        assert rest is link.empty or isinstance(rest,link)
        self.first =first
        self.rest=rest
    def __getitem__(self,i):
        if i==o:
            return self.first
        else:
            return self.rest[i-1]
    def __len__(self):
        return 1+len(self.rest)


s=link(3, link(4, link(5)))



def make_counter():
    count=0
    def counter():
        nonlocal count
        count+=1
        return count
    return counter
class Car(object):
    num_wheels = 4
    gas = 30
    headlights = 2
    size = 'Tiny'

    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.color = 'No color yet. You need to paint me.'
        self.wheels = Car.num_wheels
        self.gas = Car.gas

    def paint(self, color):
        self.color = color
        return self.make + ' ' + self.model + ' is now ' + color
        
hilfingers_car.paint('black')
'Tesla Model S is now black'
Car.paint(hilfingers_car, 'red')
'Tesla Model S is now red'

def digits(n):
    """Return the digits of n as a linked list.

    >>> digits(0) is Link.empty
    True
    >>> digits(543)
    Link(5, Link(4, Link(3)))
    """
    s = Link.empty
    while n > 0:
        n, last = n // 10, n % 10
        '''*** YOUR CODE HERE ***'''
        s=Link(last,s)
    return s

counting how many times called
def count(f):
    def counted(n):
        counted.call_count+=1
        return f(n)
    counted.call_count=0
    return counted

memoization
def memo(f)
    cache={}
    if n not in cache:
        cache[n]=f(n)
    return cache[n]
return memoized

def count_frame(f):
    def counted(n):
        counted.open_count+=1
        if counted.open_count>counted.max_count:
            counted.max_count=counted.open_count
        result=f(n)
        counted.open_count-=1
        return result
    counted.open_count=0
    counted.max_count=0
    return counted

%%%%%%%%%mutable functions
def make_withdraw(balance):
    def withdraw(amount):
        nonlocal balance
        if balance>withdraw:
            return ('insufficient balance')
        balance = balance -amount
        return balance
    return withdraw
another way is to put balance in a list, cause list can be changed nd it's muteble

b=[balance]
.
.
.
if amount>b[0]: .....
b[0]=b[0]-amount



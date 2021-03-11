def count_leaves(t):
    if is_leaf(t):
        return 1
    else:
        branch_counts=[count_leaves(b) for b in branches(t)]

        return sum (branch_counts)

def leaves(tree):
    if is_leaf(tree):
        return [label(tree)]
    else:
        return sum ([leaves(b) for b in branches(tree)], [])

def increment_leaves(t):
    if is_leaf(t):
        return tree(label(t)+1)
    else:
        bs=[increment_leaves (b) for b in branches(t)]
        return tree(label (t),bs)
def increment(t):
    return tree(label (t)+1,increment_leaves (b) for b in branches(t))

def print_tree(t):
    print (label(t))
    for b in branches(t):
        print_tree (b)
%%%%%%%%%%%%%%%%%%%%%%%%%

def tree(label,branches=[]):
    for branch in branches:
        assert is_tree(branch)
    return [label]+ list(branches)

def label(tree):
    return tree(0)

def branches(tree):
    return tree[1:]

def is_tree(tree):
    if type(tree)!=list or len(tree)<1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True
def is_leaf(tree):
    return not branches(tree)

def gcd (a,b)
    smaller, larger = min(a, b), max(a, b)
    if larger % smaller == 0:
            return smaller

        return gcd(smaller, larger % smaller)

def sprout_leaves:
if is_leaf(t):
        return tree(label(t),[tree(i) for i in leaves])
    else:
        sub = [sprout_leaves(x,leaves) for x in branches(t)]
        return tree(label(t),sub)
        





    
    

class queue:
    def __init__(a):
        a.in_stack=[]
        a.out_stack=[]
    def __len__(a):
        return (len(a.in_stack)+len(a.out_stack))
    def push(a,obj):
        return a.in_stack.append(obj)
    def pop(a):
        if not a.out_stack:
            a.out_stack=a.in_stack[::-1]
            #a.in_stack=[]
            print(a.in_stack,a.out_stack)
        return a.out_stack.pop()
dsa=queue()
dsa.push(2)
dsa.push(3)
dsa.push(4)
print(dsa.pop())
print(dsa.pop())
print(dsa.pop())
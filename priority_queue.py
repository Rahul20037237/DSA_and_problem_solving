class pr_heap:
    def __init__(c,items):
        c.heap=[None]
        c.rank={}
        for x in items:
            c.push(x)
    def push(c,x):
        assert x not in c.rank
        i=len(c.heap)
        c.heap.append(i)
        c.rank[x]=i
        c.up(i)
    def up(c,i):
        x=c.heap[i]
        print(x)
        while i>1 and x<c.heap[i//2]:
            c.heap[i]=c.heap[i//2]
            c.rank[c.heap[i//2]]=i
            i//=2
        c.heap[i]=x
        c.rank[x]=i
    def down(c,i):
        x=c.heap[i]
        
    def print_(c):
        print("heap-->",c.heap,"rank--->",c.rank)
if __name__=="__main__":
    a=pr_heap(['A','B','C','D','o','F','G'])
    a.print_()

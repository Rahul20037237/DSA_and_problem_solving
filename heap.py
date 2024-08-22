class heap:
    def __init__(self,elements) -> None:
        self.rank={}
        self.elements=[None]
        for i in elements:
            self.push(i)
    def __str__(self):
        return f"{self.elements} {self.rank}"
    def push(self,x):
        assert x not in self.rank
        i=len(self.elements)
        self.elements.append(x)
        self.rank[x]=i
        self.up(i)
    def pop(self):
        root=self.elements[1]
        del self.rank[root]
        x=self.elements.pop()
        if self:
            self.elements[1]=x
            self.rank[x]=1
            self.down(1)
        return root
    def down(self,i):
        x=self.elements[i]
        n=len(self.elements)
        while True:
            left=2*i
            right=2*i+1
            if(right<n and self.elements[right]<x and self.elements[right]<self.elements[left]):
                self.elements[i]=self.elements[right]
                self.rank[self.elements[right]]=i
                i=right
            elif(left<n and self.elements[left]<x and self.elements[left]<self.elements[right]):
                self.elements[i]=self.elements[left]
                self.rank[self.elements[left]]=1
                i=left
            else:
                self.elements[i]=x
                self.rank[x]=i
                return
    def up(self,i):
        x=self.elements[i]
        while i>1 and x<self.elements[i//2]:
            self.elements[i]=self.elements[i//2]
            self.rank[self.elements[i//2]]=i
            i//=2
        self.elements[i]=x
        self.rank[x]=i
x=heap([1,32,3,4,42,234,23])
print(x)
x.pop()
print(x)
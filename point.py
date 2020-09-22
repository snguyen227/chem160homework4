class point:
    def __init__(self, dim, data):
        self.dim=dim
        self.data=[]
        for i in range(dim):
            self.data.append(float(data[i]))
    def __repr__(self):
        output=""
        for i in self.data:
            output+=str(i)+" "
        return output
    def scale(self, x):
        for i in range(self.dim):
            self.data[i]*=x
    def dot(self, apoint):
        sum=0
        for i in range(self.dim):
            sum+=self.data[i]*apoint.data[i]
        return sum
    
    def dist(self, apoint):
        sums=[]
        for i in range(self.dim):
            sums.append(self.data[i]+apoint.data[i])
            self.data[i] = sums[i]
        return self
    def mirror(self):
        mirror=[]
        for i in range(self.dim):
            mirror.append((self.data[i])*(self.data[i]))
        mirror=sum(mirror)
        return mirror

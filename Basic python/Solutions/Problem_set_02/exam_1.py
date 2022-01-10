class ECustomer:
    count = 0
    def __init__(self,name):
        self.name = name
        # self.lst = []
        ECustomer.count +=1
        
    def setProductDetails(self,*item):
        # for i in item:
        #     self.lst.append(i)
        self.lst = item
        self.total_cost=0
        for i in range(1,len(self.lst),2):
            self.total_cost += int(self.lst[i])

    def printDetail(self):
        print("Name: ",self.name)
        print("Product: ", end=' ')
        for i in range(0,len(self.lst)-2,2):
            print(self.lst[i], end=', ')
        print(self.lst[len(self.lst)-2])
        print("Total cost: ",self.total_cost)

print("Total E-Customer:", ECustomer.count)
c1 = ECustomer("James")
c1.setProductDetails("TV",35000,"Air Cooler", 9000)
c2 = ECustomer("Mike")
c2.setProductDetails("Mobile",20000,"Headphone",1200,"Fridge", 45000)
c3 = ECustomer("Sarah")
c3.setProductDetails("Headphone", 1200)
print("=========================")
c1.printDetail()
print("=========================")
c2.printDetail()
print("=========================")
c3.printDetail()
print("=========================")
print("Total E-Customer:", ECustomer.count)


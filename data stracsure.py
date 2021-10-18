#implemntion linked_list
class Slinked_list:
    def __init__(self,head=None,tail=None):
        self.head=head
        self.tail=tail
        self.length=0

    def add(self,i,v):
        
        if self.head==None:
            new_node=node(v)
            self.head=new_node
            self.length+=1
        elif i<=self.length:
            curent=self.head
          
               
                
            for j in range(i-1):
                curent=curent.Next
            
                
               
            if curent.Next==None:    
                new_node=node(v)
                #lst_node=curent.Next
                curent.Next=new_node
                #new_node.Next=lst_node
                self.length+=1
            else:
                print("this index booked up")
               
        else:
            print("index is not defined")
            
    def remove(self,i):
        curent=self.head
        if i==0:
            new=curent.Next
            self.head=new
            self.length-=1
        else:    
            for j in range(i-1):
                curent=curent.Next
            new=curent.Next.Next
            curent.Next=new
            self.length-=1
            
    def update(self,i,v):
        curent=self.head
        if i==0:
            curent.value=v
            #next_node=self.head.Next
            #self.head=node(v)
            #self.head.Next=next_node
            
        else:
            for j in range(i):
                curent=curent.Next
            curent.value=v
            
    def red(self,i):
        curent=self.head
        if i==0:
            return curent.value
        elif i<self.length:
            for j in range(i):
                curent=curent.Next
            return curent.value    
        else:
            return "this index is not defined in list"
    def print_all(self):
        curent=self.head
        for j in range(self.length):
            print(curent.value,"\n")
            curent=curent.Next
        
            
                
                
      
                
       
            
            
            
      
       
                
            
class node:
    def __init__(self,value,Next=None):
        self.value=value
        self.Next=Next
obj=Slinked_list()
obj.add(0,5)

obj.add(1,6)

obj.add(2,10)
obj.add(3,28)


#obj.add(0,17)
#obj.remove(4)
#obj.update(1,18)
x=obj.red(3)
obj.print_all()



        



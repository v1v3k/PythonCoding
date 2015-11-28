__author__ = 'george'


class node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def set_data(self,data):
        self.data=data


    def get_next(self):
        return self.next_node


    def set_next(self,new_node):
        self.next_node = new_node

    def has_next(self):
        return self.get_next() != None


class linked_list:

    def __init__(self,head=None):
        self.head = head


    def print_data(self):
        itr=self.head
        while(itr != None):
            print itr.get_data(),
            itr = itr.get_next()
        print ''

    def insert(self,new_node):
        new_node.set_next(self.head)
        self.head = new_node

    def insert_end(self,new_node):
        itr=self.head
        while(itr.get_next()!=None):
            itr=itr.get_next()
        itr.set_next(new_node)

    def del_beg(self):
        self.head=(self.head).get_next()

    def del_end(self):
        itr=self.head
        while((itr.get_next()).get_next()!=None):
            itr=itr.get_next()
        itr.set_next(None)

    def length_ll(self):
        itr=self.head
        count=1;
        while (itr.get_next()!=None):
            itr=itr.get_next()
            count+=1
        return count

    def revers_ll(self):

        curr=self.head
        prev=None
        next=None

        while curr!=None:
            next=curr.get_next()
            curr.set_next(prev)
            prev=curr
            curr=next

        self.head=prev
        self.print_data()



    def insert_pos(self,pos,new_node):

        l= self.length_ll()
        if pos == 0:
            self.insert(new_node)
            return True
        elif l< pos:
            print ('End of Linked List reached***')
            print (self.length_ll())
            return True
        else:
            itr=self.head
            cur_pos= 0

            while cur_pos < pos-1:
                itr=itr.get_next()
                cur_pos+=1

            if itr.get_next()==None:
                self.insert_end(new_node)

            else:
                temp=itr.get_next()
                itr.set_next(new_node)
                new_node.set_next(temp)




if __name__=="__main__":

    node1=node(10)
    node2=node(20)
    node3=node(30)
    l1= linked_list()
    l1.insert(node1)
    l1.insert(node2)
    l1.insert(node3)
    node4=node(50)
    l1.insert_end(node4)
    l1.print_data()
    temp=node(1000)
    l1.insert_pos(1,temp)
    l1.print_data()
    temp=node(2000)
    l1.insert_pos(1,temp)
    l1.print_data()
    temp=node(6000)
    l1.insert_pos(0,temp)
    l1.print_data()
    temp=node(6000)
    l1.insert_pos(0,temp)
    l1.print_data()
    temp=node(6000)
    l1.insert_pos(99,temp)
    l1.print_data()
    l1.length_ll()
    l1.insert_pos(6,node(350))
    l1.print_data()
    l1.insert_pos(99,node(360))
    l1.insert_pos(9,node(320))
    l1.print_data()
    l1.revers_ll()


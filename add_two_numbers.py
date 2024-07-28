class CreateNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.length = 0

    def print_l(self):
        temp = self.head
        while temp != None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        node = CreateNode(value)
        if self.length == 0:
            self.head = node
            self.tail = self.head
            self.length = self.length + 1
            return True
        temp = self.head
        while temp.next != None:
            temp = temp.next
        temp.next = node
        self.tail = node
        self.length = self.length + 1
        return True
    
    def get(self, index):
        if index < 0 or index > self.length:
            return None
        i = 0
        temp = self.head
        while i < index:
            temp = temp.next
            i = i+1
        return temp.value

    def reverse(self):
        current = self.head
        self.tail = current
        temp = self.head.next
        prev = None
        while temp != None:
            current.next = None
            current.next = prev
            prev = current
            current = temp
            temp = temp.next
        current.next = prev
        self.head = current
        return True

list1 = [9,9,9,9,9,9,9]

l = LinkedList()
for i in list1:
    l.append(i)

print("before reverse l1 :")
l.print_l()
#l.reverse()
#print("after reverse l1 :")
#l.print_l()

print()

list2 = [9,9,9,9,0,0,0]

l1 = LinkedList()
for i in list2:
    l1.append(i)

print("before reverse l2 :")
l1.print_l()
#l1.reverse()
#print("after reverse l2 :")
#l1.print_l()

carry = 0
l_sum = LinkedList()
for i in range(l.length):
    sum = l.get(i) + l1.get(i)
    if i == 0:
        if sum >= 10:
            l_sum.append(sum % 10)
        else:
            l_sum.append(sum)
    else:
        sum = carry+sum
        if sum >= 10:
            l_sum.append(sum % 10)
        else:
            l_sum.append(sum)
    carry = sum // 10
if carry != 0:
    l_sum.append(carry)

print("before reverse")
l_sum.print_l()

l_sum.reverse()
print("result : ")
l_sum.print_l()
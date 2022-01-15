#Design HashMap problem in Leetcode


class ListNode:
    def __init__(self,key,value):
        self.key=key
        self.value=value
        self.next=None
class MyHashMap:
    SIZE=10000
    def __init__(self):
        
        self.hashMap=[None]*self.SIZE #take the empty array inorder to make the hashmap!
    
    def index(self,key):
        return hash(key)%10000
    
    def find(self,key):
        hashKey=self.index(key)
        
        head=self.hashMap[hashKey]
        prev=None
        curr=head
        
        while curr and curr.key!=key:
            prev=curr
            curr=curr.next
        return prev

    def put(self, key: int, value: int) -> None:
        
        hashKey=self.index(key)
        
        if self.hashMap[hashKey]==None:
            self.hashMap[hashKey]=ListNode(-1,-1)
        
        
        ptr=self.find(key)
        
        
        #if key does not exists
        
        if ptr.next==None:
            newEntry=ListNode(key,value)
            ptr.next=newEntry
        
        #if key is existing
        else:
            ptr.next.value=value
        

    def get(self, key: int) -> int:
        hashKey=self.index(key)
        
        #null index/hashkey
        if self.hashMap[hashKey]==None:
            return -1
        
        ptr=self.find(key)
        
        
        
        #found
        if ptr.next!=None:
            return ptr.next.value
        
        #Not found
        else:
            return -1
        
          

    def remove(self, key: int) -> None:
        hashKey=self.index(key)
        
        if self.hashMap[hashKey]==None:
            return 
        
        ptr=self.find(key)
        
        #found
        if ptr.next==None:
            return None
        
        ptr.next=ptr.next.next
        
#         #not found
#         if ptr.next==None:
            


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)

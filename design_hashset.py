# Design hashset problem leetcode

class MyHashSet:

    def __init__(self):
        self.hashsetSize=1000
        self.listSize=1001
        self.hashSet=[None]*1000
    def hashKey(self,key):
        return key%self.hashsetSize
    
    def listIndex(self,key):
        return key//self.listSize
        
    def add(self, key: int) -> None:
        hashKey=self.hashKey(key)
        listIndex=self.listIndex(key)
        if self.hashSet[hashKey]==None:
            # print('it is empty')
            self.hashSet[hashKey]=[None]*self.listSize
        self.hashSet[hashKey][listIndex]=True
        
    def remove(self, key: int) -> None:
        hashKey=self.hashKey(key)
        listIndex=self.listIndex(key)
        if self.hashSet[hashKey]==None:
            return
        self.hashSet[hashKey][listIndex]=False

    def contains(self, key: int) -> bool:
        hashKey=self.hashKey(key)
        listIndex=self.listIndex(key)
        
        return self.hashSet[hashKey]!=None and self.hashSet[hashKey][listIndex]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)

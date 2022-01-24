class MyHashSet:

    def __init__(self):
        self.hashset = [None]*1000
        self.bucket = 1000
        self.bucketitems = 1001

    def add(self, key: int) -> None:
        i = self.hashfun1(key)
        if self.hashset[i] == None:
             self.hashset[i]= [None]*self.bucketitems
        j = self.hashfun2(key)
        self.hashset[i][j] = True
    def remove(self, key: int) -> None:
        i = self.hashfun1(key)
        if self.hashset[i] == None:
            return
        j = self.hashfun2(key)
        del self.hashset[i][j]

    def contains(self, key: int) -> bool:
        i = self.hashfun1(key)
        j = self.hashfun2(key)
        if self.hashset[i]!= None and self.hashset[i][j]:
            return True
        else:
            return False
    def hashfun1(self, key: int):
        return key % self.bucket
    def hashfun2(self, key: int):
        return key // self.bucketitems


if __name__ == "__main__":
    hashSet = MyHashSet()
    hashSet.add(1)
    hashSet.add(2)
    print(hashSet.contains(1))  # returns true
    print(hashSet.contains(3))  # returns false (not found)
    hashSet.add(2)
    print(hashSet.contains(2))  # returns true
    hashSet.remove(2)
    print(hashSet.contains(2))  # returns false (already removed)

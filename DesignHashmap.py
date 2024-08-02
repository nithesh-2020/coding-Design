class Node:

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
class hashmap:

    def __init__(self):
        self.size = 1000
        self.hash_arr = [None] * self.size


    def put(self, key: int, value: int) -> None:
        indx = key % self.size

        if self.hash_arr[indx] == None:
            #Nothing in the list
            self.hash_arr[indx] = Node(key, value)
        else:
            #Something in the list
            cur_node = self.hash_arr[indx]
            while True:
                if cur_node.key == key:
                    cur_node.value =  value
                    return
                if cur_node.next == None:
                    break
                cur_node = cur_node.next
            cur_node.next = Node(key, value)

    def get(self, key:int) -> int:
        indx = key % self.size
        cur_node = self.hash_arr[indx]
        while cur_node:
            if cur_node.key == key:
                return cur_node.value
            else:
                cur_node = cur_node.next
        return -1

    def remove(self, key:int) -> None:
        indx = key % self.size
        cur_node = prev_node = self.hash_arr[indx]
        if not cur_node: return
        if cur_node.key == key:
            self.hash_arr[indx] = cur_node.next
        else:
            cur_node = cur_node.next

            while cur_node:
                if cur_node.key == key:
                    prev_node.next = cur_node.next
                    break
                else:
                    prev_node, cur_node = prev_node.next, cur_node.next

if __name__ == '__main__':
    hashMap = hashmap()
    hashMap.put(1, 1)

    hashMap.put(2, 2)

    print(hashMap.get(1))

    print(hashMap.get(3))

    print(hashMap.get(2))

    hashMap.put(2, 1)

    print(hashMap.get(2))

    hashMap.remove(2)

    print(hashMap.get(2))




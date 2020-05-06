class HashTableEntry:
    """
    Hash Table entry, as a linked list node.
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None] * capacity

    def hash(self, key):
        return hash(key)

    def djb2(self, key):
        hash = 5381

        for x in key:
            hash = (hash * 33) + ord(x)

        return hash

    def hash_index(self, key):
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        index = self.hash_index(key)
        node = self.storage[index]

        if node is None or node.key == key:
            node.next = HashTableEntry(key, value)
        else:
            while True:
                if node.next is None or node.key == key:
                    node.next = HashTableEntry(key, value)
                    break
                node = node.next

    def delete(self, key):
        index = self.hash_index(key)
        node = self.storage[index]
        prev = None

        while node.next is not None and node.key != key:
            prev = node
            node = node.next

        if prev is None:
            self.storage[index] = node.next

        else:
            prev.next = node.next

    def get(self, key):
        index = self.hash_index(key)
        node = self.storage[index]

        if node == None:
            return None
        while True:
            if node.key == key:
                return node.value
            node = node.next

    def resize(self):
        self.capacity *= 2
        old = self.storage
        self.storage = [None] * self.capacity

        for o in old:
            node = o
            while node is not None:
                self.insert(node.key, node.value)
                node = node.next


if __name__ == "__main__":
    ht = HashTable(2)

    ht.put("line_1", "Tiny hash table")
    ht.put("line_2", "Filled beyond capacity")
    ht.put("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.get("line_1"))
    print(ht.get("line_2"))
    print(ht.get("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.get("line_1"))
    print(ht.get("line_2"))
    print(ht.get("line_3"))

    print("")

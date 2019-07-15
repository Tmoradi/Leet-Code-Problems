class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.set = {} 

    def add(self, key: int) -> None:
        self.set.add(key)       

    def remove(self, key: int) -> None:
        self.set.discard(key)

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        
        return {key}.issubset(self.set)
        
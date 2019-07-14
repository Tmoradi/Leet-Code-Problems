class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dictionary = {}
        

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        self.dictionary[key] = value

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        if key not in self.dictionary.keys():
            return -1
        return self.dictionary[key]

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        if key in self.dictionary.keys(): del self.dictionary[key]
        

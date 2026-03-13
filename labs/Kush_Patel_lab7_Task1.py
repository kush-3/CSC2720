# Kush Patel

# initialize the class for the custom map
class MyCustomMap:
    def __init__(self, N):
        self.size = N
        self.keys = [None] * self.size  # Stores keys
        self.values = [None] * self.size  # Stores corresponding values

    # hash function to hash the key
    def hash(self, key):
        if isinstance(key, int):
            return key % self.size
        
        elif isinstance(key, float):
            fraction = key - int(key)
            return int(fraction * 100) % self.size

        elif isinstance(key, str):
            hash_value = 0
            p = 31
            for char in key: 
                hash_value = hash_value * p + ord(char)
            return hash_value % self.size 
        else: 
            raise Exception("The given key is not supportes.")

    def put(self, key, value):        # add the key and value to the map
        index = self.hash(key)

        # Second hash function (step size)
        if isinstance(key, int):
            step = 1 + (key % 11)
        else: 
            step = 1 + (abs(self.hash(key)) % 11)

        original_index = index

        while self.keys[index] is not None and self.keys[index] != key:
            index = (index + step) % self.size
            if index == original_index:
                raise Exception("Hash table is full.")

        self.keys[index] = key
        self.values[index] = value

    def get(self, key):
        index = self.hash(key)

        if isinstance(key, int):
            step = 1 + (key % 11)
        else:
            step = 1 + (abs(self.hash(key)) % 11)

        original_index = index

        while self.keys[index] is not None:
            if self.keys[index] == key:
                return self.values[index]

            index = (index + step) % self.size

            if index == original_index:
                break

        return None

    def __setitem__(self, key, value):
        # set the value for the key
        self.put(key, value)

    def __getitem__(self, key):
        # get the value for the key
        return self.get(key)


# Example usage
# driver code:
map = MyCustomMap(13)
map.put(10, 'a')
map.put(22, 'b')
map.put(31, 'c')
map[9] = 'd'   # comment or remove this line out to not raise a collison error/
map[15] = 'e'

print(map.get(31))
print(map[15])
print(map.get(44))

class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        #I would have gone with a linked list here
        self.storage = [None]*capacity

    def append(self, item):
        self.storage[self.current] = item
        if self.current < self.capacity-1:
            self.current += 1
        else:
            self.current = 0

    def get(self):
        ret_arr = []
        i = 0
        while i < self.capacity and self.storage[i] is not None:
            ret_arr.append(self.storage[i])
            i += 1
        return ret_arr
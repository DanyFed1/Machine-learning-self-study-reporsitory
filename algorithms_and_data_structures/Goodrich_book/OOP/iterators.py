class SequenceIterator:
    """An iterator for any Python's sequence types"""

    def __init__(self, sequence):
        """Create an iterator for the given sequence"""
        self.sequence = sequence #keep a reference to the underlying data
        self._k = -1 #will increment to 0 on first call to next

    def __next__(self):
        """Return the next element of the sequence"""
        self._k += 1 #advance to the next index
        if self._k < len(self.sequence):
            return self.sequence[self._k] #returns the data element if we did not go out of sequence bounds
        else:
            raise StopIteration() #there are no more elements

    def __iter__(self):
        """Return the iterator itself"""
        return self #by convention, an iterator must return itself as an iterator

if __name__ == "__main__":
    my_list = [1,2,3,4,5]
    my_iterator = SequenceIterator(my_list)
    print(next(my_iterator))
    print(next(my_iterator))
    print(next(my_iterator))
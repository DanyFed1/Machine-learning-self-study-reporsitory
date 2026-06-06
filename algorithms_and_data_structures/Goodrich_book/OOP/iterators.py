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


#__________Example" Range Class that mimics the built-in range class
r = range(8,140,5)
print(type(r))
print(r)
print(r[0])
print(r[0:5:2])
print(len(r))

class Range:
    """A class that mimics the built-in range class
    Shows the implelmentation of generators as 
    len will automatically implemnt the iterator protocol"""

    def __init__(self, start, stop, step):
        """Initialize a Range instance.
        
        Semantics is similar to built-in range class"""
        if step == 0:
            raise ValueError("step cannot be 0")

        if stop is None: #Special case of range(n)
            start, stop = 0, start #Will return in range (0, n)
        
        #calculate the effective length once

        self._length = max(0, (stop - start + step - 1) // step)

        #Need knowledge of start and step (but not stop_ to support __getitem__)
        self._start = start
        self._step = step

    def __len__(self):
        """Return the number of entrieus in the range"""
        return self._length

    def __getitem__(self, k):
        """Return entry at index k (using standard interpretation if negative)"""
        if k < 0:
            k += len(self) #attempt to convert negative index

        if not 0 <= k < self._length:
            raise IndexError("index out of range")
        
        return self._start + k * self._step
    

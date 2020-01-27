def _attrs(self):
    if len(self) == 0:
        return ()
    return (next(iter(self)), next(reversed(self)), len(self))

class float_range:
    
    def __init__(self,*args):
        if len(args) == 3:
            self.start,self.stop,self.step = args
        elif len(args) == 2:
            self.start,self.stop = args
            self.step = 1.0
        elif len(args) == 1:
            self.stop = args[0]
            self.start = 0.0
            self.step = 1.0
        else:
            raise TypeError()

    def __iter__(self):
        if self.start < self.stop and self.step > 0:
            counter = self.start
            while counter < self.stop:
                yield counter
                counter += self.step
        elif self.start > self.stop and self.step < 0:
            counter = self.start
            while counter > self.stop:
                yield counter
                counter += self.step
        else:
            return
            yield

    def __len__(self):
        if self.stop > self.start and self.step > 0:
            diff = self.stop - self.start
        elif self.stop < self.start and self.step < 0:
            diff = self.start - self.stop
        else:
            return 0
        result = diff // abs(self.step)
        if (diff % abs(self.step)) == 0:
            return int(result)
        else:
            return int(result + 1)

    def __reversed__(self):
        counter = self.start + (len(self)-1)*self.step
        for x in range(len(self)):
            yield counter
            counter -= self.step

    def __eq__(self, other):
        if isinstance(other, (float_range, range)):
            return _attrs(self) == _attrs(other)
        else:
            return NotImplemented

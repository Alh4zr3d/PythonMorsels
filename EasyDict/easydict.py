class EasyDict(object):

    def __init__(self,_dict={},normalize=False,**kwargs):
        self._normalize = normalize
        for key, value in _dict.items():
            self[key] = value
        for key, value in kwargs.items():
            self[key] = value

    def normalized(self, key):
        if self._normalize:
            return key.replace(' ', '_')
        else:
            return key

    def __getitem__(self,_key):
        return self.__dict__[self.normalized(_key)]

    def __setitem__(self,_key,_value):
        self.__dict__[self.normalized(_key)] = _value

    def __eq__(self,other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        else:
            return False

    def __ne__(self,other):
        return not self.__eq__(other)

    def get(self, key, default=None):
        return getattr(self, self.normalized(key), default)

class AttrDict(dict):
    """
    Dictionary whose keys can be accessed as attributes.
    Example:
    >>> d = AttrDict(x=1, y=2)
    >>> d.x
    1
    >>> d.y = 3
    """

    def __init__(self, *args, **kwargs):
        self.dict_data = args[0]
        s=args[0]
        s["dict"]=args[0]
        super(AttrDict, self).__init__(s, **kwargs)
        self.__dict__ = self


    def __getattr__(self, item):
        return self.__dict__.get(item)

    def return_dict(self):
        return self.__dict__.get("dict")
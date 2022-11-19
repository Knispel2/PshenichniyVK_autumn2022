

class CustomMeta(type):
    def __new__(cls, name, bases, dct):
        def __setattr__(self, name, value):
            if name not in self.__dict__.keys():
                self.__dict__['custom_'+name] = value
            else:
                self.__dict__[name] = value
        edit_dict = {}
        for (key, value) in dct.items():
            if key.startswith('__') and key.endswith('__'):
                edit_dict[key] = value
            else:
                edit_dict['custom_'+key] = value
        edit_dict['__setattr__'] = __setattr__
        return super().__new__(cls, name, bases, edit_dict)

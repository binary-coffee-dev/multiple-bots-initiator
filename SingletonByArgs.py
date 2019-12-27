class SingletonByArgs(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if (cls, *args) not in cls._instances:
            cls._instances[(cls, *args)] = super(SingletonByArgs, cls).__call__(*args, **kwargs)
        return cls._instances[(cls, *args)]
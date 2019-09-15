class tst:
    def __init__(self):
        self.d = {}
    def __getitem__(self,*args,**kwargs):
        print(args)
        print(kwargs)
    def __setitem__(self,*args,**kwargs):
        print(args)
        print(kwargs)


# >>> t['m','n'] = 888
# (('m', 'n'), 888)
# {}
# >>>

# >>> t[1,2,3,4]
# ((1, 2, 3, 4),)
# {}
# >>> t[[1,2,3,4]]
# ([1, 2, 3, 4],)
# {}
# >>> t[(1,2,3,4)]
# ((1, 2, 3, 4),)
# {}


# real_args = args[0]
# *real_args

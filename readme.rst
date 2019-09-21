.. contents:: Table of Contents
   :depth: 5


*efuntool*
------------



Installation
============

    ::
    
        $ pip3 install efuntool

Usage
=====
    
    ::
        
        import efuntool.efuntool as eftl
        
        #the original function with 4 params

        def sum_of_4(a,b,c,d):
            return(a+b+c+d)

        #wrap it with eftl.curry(orig_func,params_count)

        f = eftl.curry(sum_of_4,4)

        #call at any params-combo, just keep the sequence

        f(1,2,3,4)
        f(1,2,3)(4)
        f(1,2)(3,4)
        f(1)(2,3)(4)
        
        >>> f(1,2,3,4)
        10
        >>> f(1,2,3)(4)
        10
        >>> f(1,2)(3,4)
        10
        >>> f(1)(2,3)(4)
        10
        >>> f(1,2)(3)(4)
        10
        >>> f(1)(2)(3)(4)
        10

        #step by step , pass params
        f(1)
        f(2)
        f(3)
        f(4)
        
        >>> f(1)
        <efuntool.efuntool.curry object at 0x7f242ffc5898>
        >>> f(2)
        <efuntool.efuntool.curry object at 0x7f242ffc5898>
        >>> f(3)
        <efuntool.efuntool.curry object at 0x7f242ffc5898>
        >>> f(4)
        10


        f(1,2)
        f(3)
        f(4)
        
        
        >>> f(1,2)
        <efuntool.efuntool.curry object at 0x7f242ffc5898>
        >>> f(3)
        <efuntool.efuntool.curry object at 0x7f242ffc5898>
        >>> f(4)
        10
        >>>


        f(1,2,3)
        f(4)
        
        >>> f(1,2,3)
        <efuntool.efuntool.curry object at 0x7f242ffc5898>
        >>> f(4)
        10
        >>>



APIS        
~~~~

- def goose():
- def curry(orig_func,params_count):
- def inplace_wrapper(func):
- def keep_ptr_wrapper(func):
- def dflt_kwargs(k,dflt,**kwargs):
- def self_kwargs(self,kl,dfltl,**kwargs):
- def de_args(kl,dfltl,*args):
- def pipeline(funcs):
- def reorder_params_trans(f,param_seqs)：
- def args2dict_trans(f):
- def bool_op(op,cond1,cond2):
- def bool_funcs_ops(funcs,ops):  

License
=======

- MIT

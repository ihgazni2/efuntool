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

curry
~~~~~
- wrap a function, currify the params, return a new function
- similiar to curry in lodash(javascript)

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


cygnus
~~~~~~
- count how many recursives done

    ::
        
        import efuntool.efuntool as eftl
        >>> egg = eftl.cygnus()
        >>> egg.count
        0
        >>> egg()
        >>> egg.count
        1
        >>> egg(
                egg()
            )
        >>> egg.count
        2
        >>> egg(
                egg(
                    egg()
                )
            )
        >>> egg.count
        3


duck
~~~~
- count how many calls done

    ::
        
        import efuntool.efuntool as eftl
        >>> egg = eftl.duck()
        >>> egg.count
        0
        >>> egg()
        >>> egg.count
        1
        >>> egg()
        >>> egg.count
        2
        >>>

hen        
~~~
- record params history
    
    ::
        
        import efuntool.efuntool as eftl
        >>> egg = eftl.hen()
        >>> egg("a")
        >>> egg("a")
        >>> egg.a
        2
        >>> egg("b")
        >>> egg("b")
        >>> egg("b")
        >>> egg.b
        3
        


APIS        
====

- def goose():
- def curry(orig_func,params_count):
- def copyornot_wrapper(func):
- def force_deepcopy_wrapper(func):
- def deepcopy_and_keep_ptr_wrapper(func):
- def force_deepcopy_and_keep_ptr_wrapper(func):
- def force_inplace_and_keep_ptr_wrapper(func):
- def dflt_kwargs(k,dflt,**kwargs):
- def self_kwargs(self,kl,dfltl,**kwargs):
- def de_args(kl,dfltl,*args):
- def pipeline(funcs):
- def params_pipeline(f,orig,*args):
- def reorder_params_trans(f,param_seqs)：
- def args2dict_trans(f):
- def bool_op(op,cond1,cond2):
- def bool_funcs_ops(funcs,ops):  
- def hen():
- def duck():
- def cygnus():


License
=======

- MIT

.. contents:: Table of Contents
   :depth: 5


*efuntool*
-----------



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

        #call at any params~combo, just keep the sequence

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


dflt_kwargs
~~~~~~~~~~~
    
    ::
        
    
       counts = dflt_kwargs("counts",100,**kwargs)
    


optional_arg(dflt,*args)
~~~~~~~~~~~~~~~~~~~~~~~~
    
    ::
        
    
        arg = optional_arg(100)
        arg
        >>>100
        arg = optional_arg(100,250)
        arg
        >>>250



kwargs_to_property_in_cls_init
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    ::
        
    
        >>> class tst():
        ...     def __init__(self,**kwargs):
        ...         eftl.self_kwargs(self,['name','age'],['stu','20'],**kwargs)
        ...
        >>> p = tst()
        >>> p.name
        'stu'
        >>> p.age
        '20'
        >>> p = tst(name='terry')
        >>> p.name
        'terry'
        >>> p.age
        '20'
        >>>
    


dictize_args
~~~~~~~~~~~~
    
    ::
        
    
        dictize args
        dictize_args(kl,dfltl,*args)

        kl = ['k1','k2','k3','k4']
        dfltl = [3,4]
        dictize_args(kl,dfltl,'a','b')
        {
            'k1':'a',
            'k2':'b',
            'k3':3,
            'k4':4
        }
    



compatibize_apply_or_call_args
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    ::
        
        >>> eftl.compatibize_apply_or_call_args(1,2,3)
        [1, 2, 3]
        >>>
        >>> eftl.compatibize_apply_or_call_args([1,2,3])
        [1, 2, 3]
        >>>
        >>> eftl.compatibize_apply_or_call_args([1])
        [1]
        >>> eftl.compatibize_apply_or_call_args(1)
        [1]
        >>>


ternaryop
~~~~~~~~~
    
    ::

    
        >>> ternaryop(3>2,"ye!","no")
        'ye!'
        >>> ternaryop(3<2,"ye!","no")
        'no'
        >>>




import ebojtool
~~~~~~~~~~~~~~~~

    ::

        import efuntool.eobjtool as eotl
        from efuntool.eobjtool import *



0. get_mros
~~~~~~~~~~~

    ::


                >>> a= 5
                >>> get_mros(a)
                [5,<class 'int'>, <class 'object'>]
                >>>


.. image:: ./images/get_mros.svg

1. get_attrs_chain
~~~~~~~~~~~~~~~~~~

    ::


                >>> class tst():
                ...     def __init__(self):
                ...         self._u = "_u"
                ...         self.u = "u"
                ...
                >>> t = tst()
                >>>
                >>> parr(get_attrs_chain(t))
                ['_u', 'u']
                ['__dict__', '__module__', '__weakref__']
                ['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']
                >>>


.. image:: ./images/get_attrs_chain.svg

2. get_own_attrs
~~~~~~~~~~~~~~~~

    ::


                >>> class tst():
                ...     def __init__(self):
                ...         self._u = "_u"
                ...         self.u = "u"
                ...
                >>> t = tst()
                >>>
                >>> get_own_attrs(t)
                ['_u', 'u']
                >>>


.. image:: ./images/get_own_attrs.svg


3. get_inherited_attrs
~~~~~~~~~~~~~~~~~~~~~~

    ::


                >>> class tst():
                ...     def __init__(self):
                ...         self._u = "_u"
                ...         self.u = "u"
                ...
                >>> t = tst()
                >>>
                >>> get_inherited_attrs(t,0)
                ['_u', 'u']
                >>>
                >>> get_inherited_attrs(t,1)
                ['__dict__', '__module__', '__weakref__']
                >>>
                >>> get_inherited_attrs(t,2)
                ['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']
                >>>
                >>> get_inherited_attrs(t,0,1)
                ['_u', 'u', '__dict__', '__module__', '__weakref__']
                >>>


.. image:: ./images/get_inherited_attrs.svg

4. get_own_visible_attrs
~~~~~~~~~~~~~~~~~~~~~~~~

    ::


                >>> class tst():
                ...     def __init__(self):
                ...         self._u = "_u"
                ...         self.u = "u"
                ...
                >>> t = tst()
                >>>
                >>> get_own_visible_attrs(t)
                ['u']
                >>>


.. image:: ./images/get_own_visible_attrs.svg

5. get_own_priv_attrs
~~~~~~~~~~~~~~~~~~~~~

    ::


                >>> class tst():
                ...     def __init__(self):
                ...         self._u = "_u"
                ...         self.u = "u"
                ...
                >>> t = tst()
                >>>
                >>> get_own_priv_attrs(t)
                ['_u']
                >>>


.. image:: ./images/get_own_priv_attrs.svg

6. get_own_builtin_attrs
~~~~~~~~~~~~~~~~~~~~~~~~

    ::


                >>> class tst():
                ...     def __init__(self):
                ...         self._u = "_u"
                ...         self.u = "u"
                ...
                >>> t = tst()
                >>>
                >>> get_own_buildin_attrs(t)
                []
                >>>


.. image:: ./images/get_own_builtin_attrs.svg


7. get_inherited_visible_attrs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    ::


                >>> class tst():
                ...     def __init__(self):
                ...         self._u = "_u"
                ...         self.u = "u"
                ...
                >>> t = tst()
                >>>
                >>> get_inherited_visible_attrs(t,1)
                []
                >>>


.. image:: ./images/get_inherited_visible_attrs.svg

8. get_inherited_priv_attrs
~~~~~~~~~~~~~~~~~~~~~~~~~~~

    ::


                >>> class tst():
                ...     def __init__(self):
                ...         self._u = "_u"
                ...         self.u = "u"
                ...
                >>> t = tst()
                >>>
                >>> get_inherited_priv_attrs(t,1)
                []
                >>>


.. image:: ./images/get_inherited_priv_attrs.svg

9. get_inherited_builtin_attrs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    ::


                >>> class tst():
                ...     def __init__(self):
                ...         self._u = "_u"
                ...         self.u = "u"
                ...
                >>> t = tst()
                >>>
                >>> get_inherited_buildin_attrs(t,1)
                ['__dict__', '__module__', '__weakref__']
                >>>
                >>> get_inherited_builtin_attrs(t,2)
                ['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']
                >>>


.. image:: ./images/get_inherited_builtin_attrs.svg

10. get_all_attrs
~~~~~~~~~~~~~~~~~

    ::


                >>> a= 5
                >>> get_all_attrs(a)
                ['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']


.. image:: ./images/get_all_attrs.svg

11. get_all_visible_attrs
~~~~~~~~~~~~~~~~~~~~~~~~~

    ::


                >>> a = 5
                >>> get_all_visible_attrs(a)
                ['bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
                >>>


.. image:: ./images/get_all_visible_attrs.svg

12. get_all_builtin_attrs
~~~~~~~~~~~~~~~~~~~~~~~~~

    ::


                >>> a = 5
                >>> get_all_builtin_attrs(a)
                ['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__']


.. image:: ./images/get_all_builtin_attrs.svg


13. get_all_priv_attrs
~~~~~~~~~~~~~~~~~~~~~~

    ::


                class tst():
                    def __init__(self):
                        self._u = "_u"
                        self.u = "u"

                t = tst()
                >>> get_all_priv_attrs(t)
                ['_u']
                >>>


.. image:: ./images/get_all_priv_attrs.svg


APIS        
====
- def is_none(obj):
- def is_bool(obj):
- def is_bytes(obj):
- def is_str(obj):
- def is_int(obj):
- def is_float(obj):
- def is_list(obj):
- def is_tuple(obj):
- def is_dict(obj):
- def is_set(obj):
- def is_regex(obj):
- def is_function(obj):
- def is_module(obj):
- def is_customer_defined_type(obj):
- def is_number(obj):
- def is_recursive_type(obj):
- def is_non_buildin_function(obj):
- def is_buildin_function(obj):
- def is_hashable_type(obj):
- def is_unhashable_type(obj):
- def is_json(obj,strict=False):
- def get_type(obj):
- def goose():
- def curry(orig_func,params_count):
- def not_wrapper(func):
- def copyornot_wrapper(func):
- def force_deepcopy_wrapper(func):
- def deepcopy_and_keep_ptr_wrapper(func):
- def force_deepcopy_and_keep_ptr_wrapper(func):
- def force_inplace_and_keep_ptr_wrapper(func):
- def dflt_kwargs(k,dflt,**kwargs):
- def self_kwargs(self,kl,dfltl,**kwargs):
- def kwargs_to_property_in_cls_init(self,kl,dfltl,**kwargs):
- def de_args(kl,dfltl,*args):
- def dictize_args(kl,dfltl,*args):
- def compatibize_apply_or_call_args(*args,**kwargs):
- def pipeline(funcs):
- def params_pipeline(f,orig,*args):
- def reorder_params_trans(f,param_seqs)：
- def args2dict_trans(f):
- def bool_op(op,cond1,cond2):
- def bool_funcs_ops(funcs,ops):  
- def hen():
- def duck():
- def cygnus():
- def get_mros(obj):
- def get_attrs_chain(obj):
- def get_own_attrs(obj):
- def get_inherited_attrs(obj,*whiches):
- def get_own_visible_attrs(obj):
- def get_own_priv_attrs(obj):
- def get_own_builtin_attrs(obj):
- def get_inherited_visible_attrs(obj,*whiches):
- def get_inherited_priv_attrs(obj,*whiches):
- def get_inherited_builtin_attrs(obj,*whiches):
- def get_all_attrs(obj):
- def get_all_visible_attrs(obj):
- def get_all_builtin_attrs(obj):
- def get_all_priv_attrs(obj):
- def optinal_arg(dflt,*args):
- def optional_which_arg(dflt,*args):
- def optional_whiches(arr,dflt,*args):
- def ternaryop(cond,if_tru_rslt,if_fls_rslt):
- def ifchain(paramd,*args)
- def ifcall(cond,f,*args):
- def ifapply(cond,f,args):
- def ifnt_call(cond,f,*args):
- def ifnt_apply(cond,f,args):
- def if_calla_else_callb(cond,fa,fb,*args):
- def if_applya_else_applyb(cond,fa,fb,args):
- def ifnt_calla_else_callb(cond,fa,fb,*args):
- def ifnt_applya_else_applyb(cond,fa,fb,args):
- def identity(o0,o1):
- def is_fls(value,*args):
- def blnot(p,*args):
- def bland(*args,**kwargs):
- def blor(*args,**kwargs):
- def bland_rtrn_last(*args,**kwargs):
- def blor_rtrn_first(*args,**kwargs):
- def scond(p,q):
- def dcond(p,q):
- def blxor(p,q):
- def product(l,repeat=2):
- def permutate(l,repeat=2):
- def permutate_all(l,*args):
- def combinate(l,repeat=2):
- def combinate_all(l,*args):
- def creat_tru_fls_mat(cnl,*args):
- def creat_tru_fls_dtb(cnl,*args):
- def if_p_then_q_else_true(p,q):
- def notp_or_q(p,q):
- def parrowq(p,q):
- def if_p_then_q_else_notq(p,q):
- def notporq_and_pornotq(p,q):
- def if_p_then_notq_else_q(p,q):
- def pandnotq_or_notpandq(p,q):
- def not_dcond(p,q):
- def if_p_then_notq_else_false(p,q):
- def p_and_notq(p,q):
- def not_scond(p,q):
- def if_p_the_notq_else_true(p,q):
- def notp_or_notq(p,q):
- def not_pandq(p,q):
- def if_p_then_false_else_notq(p,q):
- def notp_and_notq(p,q):
- def not_porq(p,q):


BOOLFUNC
========

`Link text <https://github.com/ihgazni2/efuntool/edit/master/readme.rst/>`_


License
=======

- MIT



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



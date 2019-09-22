import functools
import copy
import elist.elist as elel
import inspect


######################################################
# lambda number
# this will count how many recursives done 
###########

def cygnus():
    def egg(*o):
        lngth = len(o)
        if(lngth == 0):
            egg.count = 1
            return(egg)
        else:
            o = o[0]
            o.count = o.count + 1
        return(o)
    egg.__setattr__("count",0)
    return(egg)

#####################################
# how many calls done
#####################################

def duck():
    def egg():
        egg.count = egg.count + 1
        return(egg)
    egg.__setattr__("count",0)
    return(egg)


#########
#params history record
##############

def hen():
    def egg(zero):
        if(hasattr(egg,zero)):
            count = egg.__getattribute__(zero)
            count = count + 1
            egg.__setattr__(zero,count)
        else:
            egg.__setattr__(zero,1)
        return(egg)
    return(egg)


########################################################
##simulate  curry

def goose():
    def egg(*args):
        egg.arguments.extend(args)
        return(egg)
    egg.__setattr__("arguments",[])
    return(egg)


class curry():
    def __init__(self,orig_func,params_count):
        self.orig_func = orig_func
        self.params_count = params_count
        self.egg = goose()
    def __call__(self,*args):
        count = self.params_count
        orig_func = self.orig_func
        egg = self.egg
        egg(*args)
        args_lngth = len(egg.arguments)
        if(args_lngth<count):
            return(self)
        else:
            args = egg.arguments
            egg.arguments = []
            return(orig_func(*args))

########################################################

def reorder_params_trans(f,param_seqs):
    def new_func(*args):
        new_sorted_args = elel.select_seqs(args,param_seqs)
        return(f(*new_sorted_args))
    return(new_func)

def args2dict_trans(f):
    arg_names = inspect.getfullargspec(f).args
    def _func(arg_names,d):
        args = []
        for i in range(len(arg_names)):
            k = arg_names[i]
            args.append(d[k])
        return(f(*args))
    func = functools.partial(_func,arg_names)
    return(func)



def inplace_wrapper(func):
    @functools.wraps(func)
    def wrapper(obj,**kwargs):
        inplace = dflt_kwargs('inplace',False,**kwargs)
        if(inplace):
            return(func(obj,**kwargs))
        else:
            nobj = copy.deepcopy(obj)
            return(func(nobj,**kwargs))
    return(wrapper)

def keep_ptr_wrapper(func):
    @functools.wraps(func)
    def wrapper(obj,*args,**kwargs):
        keep_ptr = dflt_kwargs('keep_ptr',False,**kwargs)
        nobj = copy.deepcopy(obj)
        nobj = func(nobj,*args,**kwargs)
        if(keep_ptr):
            obj.clear()
            if(isinstance(obj,list)):
                obj.extend(nobj)
            elif(isinstance(obj,dict)):
                obj.update(nobj)
            else:
                pass
            return(obj)
        else:
            return(nobj)
    return(wrapper)


def dflt_sysargv(dflt,which):
    try:
        rslt = sys.argv[which]
    except:
        rslt = which
    else:
        pass
    return(dflt)


def dflt_kwargs(k,dflt,**kwargs):
    if(k in kwargs):
        v = kwargs[k]
    else:
        v = dflt
    return(v)


def self_kwargs(self,kl,dfltl,**kwargs):
    for i in range(len(kl)):
        k = kl[i]
        if(k in kwargs):
            self.__setattr__(k,kwargs[k])
        else:
            self.__setattr__(k,dfltl[i])
    return(self)


def de_args(kl,dfltl,*args):
    d = {}
    args_len = len(args)
    kl_len = len(kl)
    for i in range(args_len):
        k = kl[i]
        d[k] = args[i]
    for i in range(args_len,kl_len):
        k = kl[i]
        d[k] = dfltl[i]
    return(d)


def pipeline(funcs):
    def _pipeline(funcs,arg):
        func = funcs[0]
        arg = func(arg)
        for i in range(1,len(funcs)):
            func = funcs[i]
            arg = func(arg)
        return(arg)
    p = functools.partial(_pipeline,funcs)
    return(p)


def params_pipeline(f,orig,*args):
    for i in range(len(args)):
        orig = f(orig,*args[i])
    return(orig)

####


def bool_op(op,cond1,cond2):
    op = op.lower()
    if(op == "and"):
        return(bool(cond1 and cond2))
    elif(op == "or"):
        return(bool(cond1 or cond2))
    elif(op == "not"):
        return(not(cond1))
    elif(op == "xor"):
        c1 = bool(not(cond1) and cond2)
        c2 = bool(cond1 and not(cond2))
        c = bool(c1 or c2)
        return(c)
    else:
        raise(SyntaxError("not supported op: "+op))


def bool_funcs_ops(funcs,ops):
    def _rslt(funcs,ops,arg):
        rslts = []
        for i in range(len(funcs)):
            rslt = bool(funcs[i](arg))
            rslts.append(rslt)
        cond = rslts[0]
        for i in range(1,len(rslts)):
            op = ops[i-1]
            cond = bool_op(op,cond,rslts[i])
        return(cond)
    p = functools.partial(_rslt,funcs,ops)
    return(p)
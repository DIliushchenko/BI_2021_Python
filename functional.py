def sequential_map(*args):
    res = args[-1]
    arguments = args[:-1]
    for arg in arguments:
        res = list(map(arg, res))
    return res


def consensus_filter(*args):
    res = args[-1]
    arguments = args[:-1]
    for arg in arguments:
        res = list(filter(arg, res))
    return res


def conditional_reduce(fun1, fun2, cont):
    cont = cont
    cont = list(filter(fun1, cont))
    res = fun2(cont[0], cont[1])
    return res


def func_chain(*args):
    def inner_func(x):
        res = x
        for arg in args:
            res = arg(res)
        return res
    return inner_func

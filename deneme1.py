def gen_pass2(p):
    import builtins
    x = getattr(builtins,p)
    gt = str(help(x))

    return gt.__doc__#yapay zeka ile sadece,

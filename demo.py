def profile(wrapped_func):
    """
    simple decorator to profile functions, using cProfiler.
    usage:
        write @profile before function definition(decorate it with this function),
        after that use it to see results.
    """
    import functools

    @functools.wraps(wrapped_func)
    def wrapper_func(*args, **kwargs):
        import cProfile, pstats, io
        from pstats import SortKey

        pr = cProfile.Profile()
        pr.enable()

        res = wrapped_func(*args, **kwargs)

        pr.disable()
        s = io.StringIO()

        # sort by total function working time(not excluding other function call times from function) | "cumtime" column in normal output
        sort_by = SortKey.CUMULATIVE

        # # # or sort by specific function time(excluding other function call times from function) | "tottime" column in normal output
        # sort_by = SortKey.TIME

        ps = pstats.Stats(pr, stream=s).sort_stats(sort_by)

        # 20 - number of top lines to print
        ps.print_stats(20)
        print(s.getvalue())

        return res

    return wrapper_func


# example
@profile
def test(results_num):
    res = []
    curr_num = 2

    while len(res) != results_num:
        for i in range(2, int(curr_num ** 0.5) + 1):
            if curr_num % i == 0:
                break
        else:
            res.append(curr_num)
        curr_num += 1

    return res 

func_resp = test(results_num=1000)
print(func_resp)


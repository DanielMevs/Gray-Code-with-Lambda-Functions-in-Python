g= lambda x: ["0","1"] if x == 1 else ["0" + i for i in g(x-1)] + ["1" + i for i in g(x-1)[::-1]]

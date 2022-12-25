from timeit import Timer
import matplotlib.pyplot as plt

if __name__ == "__main__":
    # popzero = Timer("x.pop(0)", "from __main__ import x")
    # popend = Timer("x.pop()", "from __main__ import x")
    
    # start, stop, step = 1000, 100001, 1000
    # # x = [100, 200, 300, ...] -> each element is the size of the list
    # # y = [1, 2, 3, ...] -> each element is the time taken to do some operation
    # x_popzero, y_popzero = [], []
    # x_popend, y_popend = [], []
    # print("pop(0)   pop()")
    # for i in range(start, stop, step):
    #     # print(i)
    #     # break
    #     x = list(range(i))
    #     # print(x)
    #     pt = popend.timeit(number=1000)
    #     x = list(range(i))
    #     pz = popzero.timeit(number=1000)
    #     print(f"{pz:7.5f} {pt:7.5f}")

    #     x_popzero.append(i)
    #     y_popzero.append(pz)
    #     x_popend.append(i)
    #     y_popend.append(pt)

    # # plot the time complexity
    # plt.scatter(x_popzero, y_popzero, label="pop(0)", marker="o")
    # plt.scatter(x_popend, y_popend, label="pop()", marker="^")
    # plt.xlabel("Size of the list")
    # plt.ylabel("Time taken")
    # plt.legend()
    # plt.show()

    
    indexer_start = Timer("x[0]", "from __main__ import x")
    indexer_end = Timer("x[-1]", "from __main__ import x")
    
    start, stop, step = 1000, 100001, 1000
    # x = [100, 200, 300, ...] -> each element is the size of the list
    # y = [1, 2, 3, ...] -> each element is the time taken to do some operation
    x_indexer_start, y_indexer_start = [], []
    x_indexer_end, y_indexer_end = [], []
    print("indexer_start   indexer_end")
    for i in range(start, stop, step):
        # print(i)
        # break
        x = list(range(i))
        # print(x)
        ids = indexer_start.timeit(number=1000)
        x = list(range(i))
        ide = indexer_end.timeit(number=1000)
        print(f"{ids:7.5f} {ide:7.5f}")

        x_indexer_start.append(i)
        y_indexer_start.append(ids)
        x_indexer_end.append(i)
        y_indexer_end.append(ide)

    # plot the time complexity
    plt.scatter(x_indexer_start, y_indexer_start, label="indexer_start", marker="o")
    plt.scatter(x_indexer_end, y_indexer_end, label="indexer_end", marker="^")
    plt.xlabel("Size of the list")
    plt.ylabel("Time taken")
    plt.legend()
    plt.show()

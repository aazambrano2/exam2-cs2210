

def p1():
    pass

def p2():
    pass

def p3():
    pass

def p4():
    pass

def p5():
    pass

def integer_break(n):
    if n < 0:
        return 0
    sub_problems = [0 for i in range(n+1)]
    #first two indexes
    sub_problems [0] , sub_problems[1] = 0 , 1

    for i in range(1,n+1):
        for j in range(1,i):
            one_integer = sub_problems[i]
            two_integers = (i - j) * j
            sub_integer = sub_problems[i-j] * j
            sub_problems[i] = max(one_integer,two_integers,sub_integer)
            


    print(sub_problems)
    return sub_problems[-1]

def partition_to_k_equal_sum_subsets():
    pass

def p8():
    pass








if __name__ == "__main__":
    print("Test cases of integer_break")
    print(integer_break(2))
    print(integer_break(10))
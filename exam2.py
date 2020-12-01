

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
            

    #print(sub_problems)
    return sub_problems[-1]

def partition_to_k_equal_sum_subsets():
    #N/A
    pass

def perfect_squares(n):
    if n <= 0:
        return -1
    
    #storing initial sub problems
    sub_problems = [0 for i in range(n+1)]
    sub_problems[0] = 0
    sub_problems[1] = 0
    print(sub_problems)

    #start at index 1
    i = 1
    j = 1
    
    while i <= n:
        sub_problems[i] = i 

        while j * j <= i:
            square = j * j
            sub_problems[i] = min(sub_problems[i], sub_problems[i - square ] + 1)
            j = j + 1
       
        i = i + 1

        #reset j
        j = 1
    
    
    return sub_problems[n]


if __name__ == "__main__":
    print("Test cases of integer_break")
    print(integer_break(2))
    print(integer_break(10))

    print("Test cases of perfect_squares")
    print(perfect_squares(12)) #3
    print(perfect_squares(13)) # 2
import random
def random_number(min_val, max_val):
    """Generates an integer between min_val and max_val

    Args:
        min_val (int): The lower boundary of the interval
        max_val (int): The max boundary of the interval

    Returns:
        int: The generated random number

    """

    return random.randint(min_val,max_val)

generated_number = random_number(0,10)
print(generated_number)

def sum_even(numbers: list)->int:
    """Calculate the summary of even numbers from list on integers
    Args:
        list(int): Give list of integers and from there take even numbers and sum them
    
    Return:
        int: return sum numner of all even numbers in the lis t
    """
    ##Option1##
    # sum variable to calculate summary of all even numbers
    sum = 0 
    for num in numbers:
        if(num%2 == 0):
            sum = sum + num

    ##Option2##
    # return sum(num for num in numbers if num%2==0)
    return sum

    

test_list = [1,2,3,4,5,6]
print(sum_even(test_list))



def fibonacci(n:int):
    """create fib series until n numbers
    Arge:
        n(int): give me n numbers
    Return:
        list(int): list of n numbers
    """
    ## Option1 ##
    list_temp = [0,1,1]
    if n<=3 :
        return list_temp
    # n hanle index from 4 and more
    n=n-3
    for i in range(n):
        # add new item that equall two previos indexes values
        list_temp.append(int(list_temp[-1])+int(list_temp[-2]))
    
    return list_temp

    ## Option 2 ##
    # seq = [0,1]
    # for _ in range(2,n):
    #     seq.append(seq(-1) + seq[-2])
    # return seq[:n]


# test - build fibonacii with 3 numbers
print(fibonacci(3))
# test - build fibonacii with 4 numbers
print(fibonacci(4))
# test - build fibonacii with 5 numbers
print(fibonacci(5))





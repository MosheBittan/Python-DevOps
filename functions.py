def sum_even(numbers: list)->int:
    """Calculate the summary of even numbers from list on integers
    Args:
        list(int): Give list of integers and from there take even numbers and sum them
    
    Return:
        int: return sum numner of all even numbers in the lis t
    """
    # sum variable to calculate summary of all even numbers
    sum = 0 
    for num in numbers:
        if(num%2 == 0):
            sum = sum + num

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
    list_temp = [0,1,1]
    if n<=3 :
        return list_temp
    # n hanle index from 4 and more
    n=n-3
    for i in range(n):
        # add new item that equall two previos indexes values
        list_temp.append(int(list_temp[-1])+int(list_temp[-2]))
    
    return list_temp


# test - build fibonacii with 3 numbers
print(fibonacci(3))
# test - build fibonacii with 4 numbers
print(fibonacci(4))
# test - build fibonacii with 5 numbers
print(fibonacci(5))





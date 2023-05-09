import tools.numbers.simp

def sumofdigits(num):
    #check if you have already used simp func if not throw error
    if not tools.numbers.simp.simp_activated:
        raise Exception("first u should use simp functions at list one time.")
    #save the sum
    sum_of_digits = 0
    #save the digit to sum and divide the num
    while num > 0:
        digit = num % 10
        sum_of_digits += digit
        num //= 10

    return sum_of_digits

def ispal(num):
    #check if you have already used simp func if not throw error
    if not tools.numbers.simp.simp_activated:
        raise Exception("first u shoud use simp functions at list one time.")
    #converter to string and equal it to its revers
    if str(num) == str(num)[::-1]:
        return True
    
    return False


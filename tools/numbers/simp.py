simp_activated = False

def add(number1,number2):
    global simp_activated
    simp_activated = True
    return number1+number2

def sub(number1,number2):
    global simp_activated
    simp_activated = True
    return number1-number2
    
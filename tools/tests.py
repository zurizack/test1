from tools.numbers.comp import *
from tools.numbers.simp import *
from tools.col import *


if __name__ == "__main__":

    print(ispal(1))#An error should be thrown: "first u should use simp functions..."
    
    print(add(1,2))#need to print 3
    print(sub(1,2))#need to print -1

    print(ispal(1))#need to print True
    print(ispal(121))#need to print True
    print(ispal(127))#need to print False
    print(sumofdigits(127))#need to print 10
    print(sumofdigits(123))#need to print 6

    num_list = [1,2,3]
    name_list = ["zur","ilan","moshe"]
    #print al tuples
    for x in myzip(num_list,name_list):
        print(x)
    

#int -> int
#return true or false for n that reach 42 bears
def bears(n):

    #Base cases
    if n < 42:
        return False
    if n == 42:
        return True

    if (n % 5)==0 and bears(n-42):                  #Divisible by 5 subtract 42
        return True

    if (n % 2)==0 and bears(n//2):                  #Divisible by 2 divide by 2
        return True

    if (n % 4)==0 or (n % 3)==0:                    #Divisible by 3 or 4 use formula

        one = (n % 10)                              #Units
        two = (n % 100)//10                         #Tens
        return one*two != 0 and bears(n-one*two)

    return False
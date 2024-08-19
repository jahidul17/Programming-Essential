def test_prime(n):
    
    if(n==1):
        print(n,"is not prime number.")
        return False
    elif(n>=2):
        for x in range(2,n):
            if(n%x==0):
                print(n,"It is not prime number")
                # break
                return False
                
        else:
            print(n,"It is prime number.")
            return True
    else:
        print(n,"It is not prime number")
        return False

test_prime(20)
print(test_prime(13))
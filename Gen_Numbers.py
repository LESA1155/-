# number = int(input("Введите число "))
# def isPrime(n, k=5): # miller-rabin
#     from random import randint
#     if n < 2: return False
#     for p in [2,3,5,7,11,13,17,19,23,29]:
#         if n % p == 0: return n == p
#     s, d = 0, n-1
#     while d % 2 == 0:
#         s, d = s+1, d/2
#     for i in range(k):
#         x = pow(randint(2, n-1), d, n)
#         if x == 1 or x == n-1: continue
#         for r in range(1, s):
#             x = (x * x) % n
#             if x == 1: return False
#             if x == n-1: break
#         else: return False
#     return True

# print(isPrime(number))
#--------------------------------------------------------------
# import random
 
# def is_Prime(n):
#     """
#     Miller-Rabin primality test.
 
#     A return value of False means n is certainly not prime. A return value of
#     True means n is very likely a prime.
#     """
#     n=10
#     if n!=int(n):
#         return False
#     n=int(n)
#     #Miller-Rabin test for prime
#     if n==0 or n==1 or n==4 or n==6 or n==8 or n==9:
#         return False
 
#     if n==2 or n==3 or n==5 or n==7:
#         return True
#     s = 0
#     d = n-1
#     while d%2==0:
#         d>>=1
#         s+=1
#     assert(2**s * d == n-1)
 
#     def trial_composite(a):
#         if pow(a, d, n) == 1:
#             return False
#         for i in range(s):
#             if pow(a, 2**i * d, n) == n-1:
#                 return False
#         return True  
 
#     for i in range(8):#number of trials 
#         a = random.randrange(2, n)
#         if trial_composite(a):
#             return False
 
#     return True

# import random
# def miller_rabin(n, k):

#     if n == 2:
#         return True

#     if n % 2 == 0:
#         return False

#     r, s = 0, n - 1
    
#     while s % 2 == 0:
#         r += 1
#         s //= 2
        
#     for _ in range(k):
#         a = random.randrange(2, n - 1)
#         x = pow(a, s, n)
        
#         if x == 1 or x == n - 1:
#             continue
            
#         for _ in range(r - 1):
#             x = pow(x, 2, n)
#             if x == n - 1:
#                 break
#         else:
#             return False
        
#     return True



# coding: utf-8

# In[27]:


def reverse_integer(x):
    ans = ""
    L = str(x)

    if x < 0:
        ans += "-" 
        L = L[1:]
    for i in range (len(L)-1,-1, -1):
        ans += L[i]
    ans = int(ans)
    return ans
        

reverse_integer(-1230000)
    
    


# In[33]:


def reverse_string(L):
    X =""
    for i in range(len(L)-1,-1,-1):
        X += L[i]
    print(X)
    
reverse_string("Minh xinh gai qua")


# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.
# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:
#     I can be placed before V (5) and X (10) to make 4 and 9. 
#     X can be placed before L (50) and C (100) to make 40 and 90. 
#     C can be placed before D (500) and M (1000) to make 400 and 900.
#     Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.

# In[65]:


def value(x):
    Char = ["I", "V", "X","L","C","D","M"]
    Val = [1,5,10,50,100,500,1000]
    for i in range(len(Char)):
        if x == Char[i]:
            ans = Val[i]
    return ans 
    
def trans_roman(X):
    ans = 0
    for i in range (len(X)):
        d = value(X[i])
        if i < (len(X)-1):
            e = value(X[i+1])
            if d < e:
                d = -d
            ans += d 
        else:
            ans +=d
        
    print (ans)
        
trans_roman("MCMXCIV") 

        


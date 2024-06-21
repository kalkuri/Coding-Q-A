##1)count the number of characters in string . example 'hello"
##{'h': 1, 'e': 1, 'l': 2, 'o': 1}


##st='hello'
##
##dic={}
##for i in st:
##    if i in dic:
##        dic[i]+=1
##    else:
##        dic[i]=1
##print(dic)
##
##output:
##
##{'h': 1, 'e': 1, 'l': 2, 'o': 1}



##2)string compression . example "aabbbccc" "a2b3c3"

##st='aabbbccc'
##
##st1=''
##count=1
##for i in range(1,len(st)):
##    if st[i]==st[i-1]:
##        count+=1
##    else:
##        st1+=st[i-1]+str(count)
##        count=1
##st1+=st[-1]+str(count)
##print(st1)
##    
##output:
##a2b2c3

##3)Longest Substring Without Repeating Characters .
##example "abcabcbb" 3 (for "abc")


def substring(s):
    
    n = len(s)
    length = 0
    left = 0
    ls = []
    
    for i in range(n):
        while s[i] in ls:
            ls.remove(s[left])
            left += 1
        ls.append(s[i])
        length = max(length, i - left + 1)

    return length


print(substring("abcabcbb"))  
print(substring("abababbb"))     
print(substring("pwwkew"))    
print(substring(""))          



##4)generate the fibonacci series
#0,1,1,2,3,5,8,13,21,34.


##n=int(input('Enter the number of term to be print:'))
##a,b=0,1
##
##if n<=0:
##    print('Enter the positive number')
##elif n==1:
##    print(f'Fibonacci series of {n}th term is',a)
##else:
##    print('Fibonacci series are:')
##    print(a,b,end=' ')
##    for i in range(2,n):
##        c=a+b
##        print(c,end=' ')
##        a=b
##        b=c
##        
##    
##
##
##
##
##
##5)write a factorial function using recurssion

##
##def factorial(n):
##    if n==1:
##        return n
##    else:
##        return factorial(n-1)*n
##print(factorial(5))








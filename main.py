`#Given a string s, reverse only all the vowels in the string and return it.

#The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both cases.
def reverse_vowels(s):
    # Write your code here
    vowels = 'aeiou'
    strS = ''
    ns = ''
    ptr1 = 0
  
    for i in s:
        if i in vowels:
            strS += i
    
    strS = strS[::-1]
    
    for i in s:
        if i in vowels:
            if i == strS[ptr1]:
                ns += i
            else:
                ns += strS[ptr1]
            ptr1 += 1
        else:
            ns += i   
        
    return ns

#TestCases
s = 'hello'
print(reverse_vowels(s), '\n')

s = 'leetcode'
print(reverse_vowels(s), '\n')
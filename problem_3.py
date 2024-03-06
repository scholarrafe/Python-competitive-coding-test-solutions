import numpy as np
string_list = ['wjmzwvldcm', 'gelnbcvtxw', 'ltydsgawbb', 'rpbnberqny', 'ujogqqxgxm']
primes = [2,3,5,7]

def find_char(char, offset):
    char_code = ord(char)-offset
    return chr(122+(char_code-97+1)) if char_code<97 else chr(char_code)

decoded_string = []

for elements in string_list:
    for offset in primes:
        if find_char(elements[0], offset)=='p':
            decoded_string.append(''.join([find_char(chars, offset) for chars in elements]))
            break

def vowel_check(element):
    sum = 0
    vowels = 'aeiou'
    for i in element:
        if i in vowels:
            sum += 1
    return True if sum==2 else False


element_essence = list(filter(lambda x:vowel_check(x), decoded_string))

def sum_of_asci(elements):
    sum = 0
    for i in elements:
        sum += ord(i)
    return sum

sum_of_ascii = list(map(sum_of_asci, element_essence))

mean_sum_of_ascii = 0
if len(sum_of_ascii)>0:
    mean_sum_of_ascii = np.round(np.mean(sum_of_ascii))

    
print(mean_sum_of_ascii)
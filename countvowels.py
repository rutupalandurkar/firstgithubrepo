# #PYTHON PROGRAM TO COUNT THE NUMBER OF EACH VOWEL
# vowels='aeiou'
# str=input("Enter the string-")
# str=str.casefold()
# count={}.fromkeys(vowels,0)
# for char in str:
#     if char in count:
#         count[char]+=1
#
# print(count)

value=input("enter the vale")
reversed_value=value[::-1]
if value==reversed_value:
    print("it's a palindrome")
else:
    print("it's not a palindrome")

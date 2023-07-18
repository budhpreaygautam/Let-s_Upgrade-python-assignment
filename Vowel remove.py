def vowel_remove(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [letter for letter in string if letter.lower() not in vowels]
    result = ''.join(result)
    print(result)


string = input("Enter the string : ")
print("String after remove all the vowels : ", end="")
vowel_remove(string)

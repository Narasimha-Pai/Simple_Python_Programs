word = input("Enter the Word")
rev = word[ : : -1]      #[ : : -1] means form infinte to infinite in reverse order
if word == rev:
    print(word, "is a palindrome")
else:
    print(word, "is not a palindrome")
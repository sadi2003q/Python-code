# Palindrome check
word = input("Enter the word ")

def checkPalindrome(word) :
    length = len(word)
    for i in range(length // 2):
        if word[i] != word[length - 1 - i]:
            return False
    return True


print(checkPalindrome(word))

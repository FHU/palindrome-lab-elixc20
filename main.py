#REMOVE PASS AND FIX THIS FUNCTION
def palindrome(word):
    if word == word[::-1]:
        return ('True')
    else:
        return ('False')

if __name__ == '__main__': 
    word = input()
    print(palindrome(word))

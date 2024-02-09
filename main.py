#REMOVE PASS AND FIX THIS FUNCTION
def palindrome(word):
    new_word = word.lower()
    final_word = new_word.replace(" ", '')
    if final_word == final_word[::-1] and final_word.isalpha() == True:
        return True
    else:
        return False

if __name__ == '__main__': 
    word = input()
    print(palindrome(word))

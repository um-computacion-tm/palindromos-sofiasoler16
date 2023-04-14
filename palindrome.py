import unittest
def palindrome (palabra):
    alr = palabra[::-1]
    if alr == palabra:
        return True
    else:
        return False

def palindromerecur(palabra):
    print(palabra)
    if len(palabra) <= 1:
        return True
    if palabra[0] == palabra[-1]:
        return (palindromerecur(palabra[1:-1]))  
    else: 
        return False



if __name__ == "__main__":
    unittest.main()

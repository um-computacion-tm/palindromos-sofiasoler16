import unittest
from palindrome import palindromerecur

class testpalindrome(unittest.TestCase):
    def test_palindrome_neuquen(self):
       result =  palindromerecur("neuquen")
       self.assertEqual(result, True)
    def test_palindrome_aba(self):
       result =  palindromerecur("aba")
       self.assertEqual(result, True)
    def test_palindrom_casa(self):
       result =  palindromerecur("casa")
       self.assertEqual(result, False)

if __name__ == "__main__":
   unittest.main()
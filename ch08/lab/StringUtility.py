
class StringUtility:
  def __init__(self, string):
    self.string = string

  def __str__(self):
    ''' 
      This function returns the internal string itself, unchanged.
      args: (obj) self
      return: (string) internal string
    '''
    return self.string

  def vowels(self):
    '''
    This function counts the number of vowels in the string, and returns a new string of the amount of vowels. If the count is 5 or more, then return the word 'many' instead of the actual count. 
    args: (obj) self
    return: (string) amount of vowels in the string if there's less than 5 vowels, otherwise returns "many"

    '''
    return str(len([letter for letter in self.string if letter in 'aeiouAEIOU'])) if len([letter for letter in self.string if letter in 'aeiouAEIOU'])<5 else "many"

  def bothEnds(self):
    '''
    This function returns a string made of the first 2 and last 2 chars of the original string. If the string length is less than or equal to 2, then it returns an empty string instead.
    args: (obj) self
    return: (string) first and last 2 characters of the string, returns empty string if the string length is less than or equal to 2
    
    '''
    return (self.string if len(self.string)<=2 else self.string[:2] + self.string[-2:])

  def fixStart(self):
    '''
    This function returns a string where all occurrences of its first char have been changed to '*' except for the first character
    If the parameter is length 1 or less, it returns the parameter as is.
    args: (obj) self
    return: (string) a string where all occurences of its first character is "*" except the first character
    
    '''
    return self.string if len(self.string)<=1 else ''.join(["*" if self.string[i]==self.string[0] and i!=0 else self.string[i] for i in range(len(self.string))])

  def asciiSum(self):
    '''
    This function returns an integer that is the sum of all ascii values in the string.
    args: (obj) self
    return: (int) sum of all ASCII values in the string

    '''
    return sum([ord(char) for char in self.string])

  def cipher(self):
    '''
    This function returns an encoded string by incrementing all letters by the length of the string. Any characters that are not letters are unchanged and uppercase wraps to uppercase and the same for lowercase.
    args: (obj) self
    return: (string) a new string that is the original string but incremented by the length of the string in ASCII values
    
    '''
    return ''.join([chr(64+(len(self.string)-(90-ord(char)))) if char.isupper() and ord(char) > 90-len(self.string) else chr(((ord(char)-97+len(self.string))%26 + 97)) if char.islower() and ord(char) > 122-len(self.string) else " " if char==" " else chr(len(self.string)+ord(char)) for char in self.string])




  
    
def encriptCipher(phrase, key):
  newPhrase = ""
  for i in range(len(phrase)):
    char = phrase[i]
    if char.isalpha():
      asciiVal = ord(char)
      if char.isupper():
        asciiVal = (asciiVal - 65 + key) % 26 + 65
      else:
        asciiVal = (asciiVal - 97 + key) % 26 + 97
      char = chr(asciiVal)
    newPhrase += char
  return newPhrase

# Decripts an encripted Cipher Key Phrase using the key 
def decriptCipher(phrase, key):
  newPhrase = ""
  for i in range(len(phrase)):
    char = phrase[i]
    if char.isalpha():
      asciiVal = ord(char)
      if char.isupper():
        asciiVal = (asciiVal - 65 - key) % 26 + 65
      else:
        asciiVal = (asciiVal - 97 - key) % 26 + 97
      char = chr(asciiVal)
    newPhrase += char
  return newPhrase
  


phrase = input("Enter a phrase: ")
key = int(input("Enter a key: "))
print(decriptCipher(phrase, key))

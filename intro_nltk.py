
import nltk

nltk.download('punkt')

from nltk.tokenize import word_tokenize

palabra1 = str(input("Digita el texto 1: "))
palabra2 = str(input("Digita el texto 2: "))

token1 = word_tokenize(palabra1)
token2 = word_tokenize(palabra2)

#Convertir palabra en mayuscula
print(", " . join( map(str, token1[0:1]) ), palabra1[0:30].lower()  )
print(", " . join( map(str, token2[0:1]) ), palabra1[0:30].upper() )
print(", " . join( map(str, token2[0:1]) ), palabra1[0:30].capitalize() )


print(", " . join( map(str, token1[0:1]) ), palabra2[0:30].lower() )
print(", " . join( map(str, token2[0:1]) ), palabra2[0:30].upper() )
print(", " . join( map(str, token2[0:1]) ), palabra2[0:30].capitalize() )

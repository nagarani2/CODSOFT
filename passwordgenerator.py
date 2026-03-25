import string
import random
length=int(input('enter password lenth:'))
characters=string.ascii_letters+ string.digits + string.punctuation
password= ''.join(random.choice(characters) for _ in range(length))
print('Generated password:',password)
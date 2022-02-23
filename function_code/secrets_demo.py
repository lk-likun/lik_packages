import secrets
import string

x = string.ascii_letters + string.digits + string.punctuation
y = ''.join([secrets.choice(x) for i in range(7)])
c = secrets.choice(string.ascii_lowercase) + y
print(c)
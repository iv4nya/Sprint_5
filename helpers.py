import random
import string

#Метод генерации рандомного email по маске *******@****.ru
def rndemail():
    chars = string.ascii_lowercase + string.digits
    username = "".join(random.choice(chars) for _ in range(7))
    domain = "".join(random.choice(chars) for _ in range(4))
    return f'{username}@{domain}.ru'

#Метод генерации рфндомного email не по маске *******@****.ru
def rndemail_not_mask():
    chars = string.ascii_lowercase + string.digits
    username = "".join(random.choice(chars) for _ in range(10))
    domain = "".join(random.choice(chars) for _ in range(2))
    return f'{username}@{domain}ru'

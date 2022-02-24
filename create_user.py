import requests
import random
import string
import json

def passwordGenerator(len):
    chars = string.ascii_letters + string.digits
    pw = random.sample(chars, len)
    return pw

def createUser():
    names = json.load(open('names.json', 'r'))
    name = names[random.randint(0, len(names) - 1)]

    surnames = json.load(open('surnames.json', 'r'))
    surname = surnames[random.randint(0, len(surnames) - 1)]

    user = name + surname
    fullName = name + ' ' + surname
    email = name.lower() + '.' + surname.lower() + '@gmail.com'
    pw = "".join(passwordGenerator(10))

    value = {
        'username': user,
        'fullName': fullName,
        'email': email,
        'password': pw,
        'rpassword': pw,
        'city': 'Skopje',
        'country': '102',
        'profession': 'Programer',
        'institution': 'Doma'
    }

    r = requests.post('https://mendo.mk/SaveRegistration.do', data=value)
    return user, pw
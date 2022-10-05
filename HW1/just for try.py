import urllib.request


phonebook = {"Liron Lev": "0528013331", "Adi Lev":"1234", "Yaffa Lev":"0525950353"}

# Get
value = phonebook.get("Liron", -1)
value = phonebook.get("Liron")
if None == value:
    value = -1

value = phonebook["Liron Lev"]
print(value)

# has_key
print("Liron Lev" in phonebook.keys())
print("Liron" in phonebook.keys())

# items and values
print(phonebook.items())
print(phonebook.values())

# pop
value = phonebook.pop("Liron Lev", -1)
print(value)
print(phonebook)

print(phonebook.pop("Liron Lev", -1))
print(phonebook.__getitem__("Adi Lev"))

s = [x**2 for x in range(10)]
print(s)

with urllib.request.urlopen("http://raw.githubusercontent.com/GITenberg/Alice-s-Adventures-in-Wonderland_11/master/11.txt") as url:
    alice = url.read()
print(alice)
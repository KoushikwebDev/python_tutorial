str = "Hello 'Koushik'"
print(str)

# Multuline String
str2 = """Hello 
Koushik 
How 
are 
you
"""

print(str2)


str3 = "Hello\nKoushik\n"
print(str3)


# iNdexing
print(str[2])  # l


# ? for loop with string

for char in str2:
    print(char)


# ? String Length
print(len(str2))


# ? Check word present in string or not

str4 = "Koushik Saha How are You"
print("Saha" in str4)  # True
print("Saha" not in str4)  # False


# ? String Slice
b = "Hello, World!"

print(b[:3])  # * it prints first 3 char => Hel
print(b[3:])  # * It print all string except first 3 char, => lo, World!
print(b[2:6])  # * it prints after index 2 to before index 6 => llo,
print(b[-5:-2])  # * it prints from last and remove !d from last => orl
print(b[-5:])  # *  it prints =>orld!


# ? Lower case upper case , replace, split && remove white space

a = " Hello Python "
print(a.lower())
print(a.upper())
print(a.strip())  # * removes white space from begining and end

print(a.replace("H", "h"))  # * it return new string, does not modify original string
print(a.split(" "))


# ? String Format
age = 34
txt = "My name is John, and I am {}"
print(txt.format(age))


quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

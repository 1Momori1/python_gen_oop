'''
Класс MutableString 🌶️
Реализуйте класс MutableString, описывающий изменяемую строку. При создании экземпляра класс должен принимать один аргумент:

string — строка, определяющая начальное значение изменяемой строки. Если не передана, строка считается пустой
Класс MutableString должен иметь два метода экземпляра:

lower() — метод, переводящий все символы изменяемой строки в нижний регистр
upper() — метод, переводящий все символы изменяемой строки в верхний регистр
Экземпляр класса MutableString должен иметь неформальное строковое представление в следующем виде:

<текущее значение изменяемой строки>
Также экземпляр класса MutableString должен иметь формальное строковое представление в следующем виде:

MutableString('<текущее значение изменяемой строки>')
При передаче экземпляра класса MutableString в функцию len() должно возвращаться количество символов в нем.

Помимо этого, экземпляр класса MutableString должен быть итерируемым объектом, то есть позволять перебирать свои символы, например, с помощью цикла for.

Также экземпляр класса MutableString должен позволять получать, изменять и удалять значения своих элементов с помощью индексов, причем как положительных, так и отрицательных. Экземпляр класса MutableString должен поддерживать полноценные срезы, результатами которых должны быть новые изменяемые строки.

Наконец, экземпляры класса MutableString должны поддерживать между собой операцию сложения с помощью оператора +, результатом которой должен являться новый экземпляр класса MutableString, представляющий конкатенацию исходных.

Примечание 1. Реализация класса MutableString может быть произвольной, то есть требований к наличию определенных атрибутов нет.

Примечание 2. Дополнительная проверка данных на корректность в методах не требуется. Гарантируется, что реализованный класс используется только с корректными данными.
'''

class MutableString:
    def __init__(self,string =''):
        self.string = string
        
    def lower(self):
        
        return self.string.lower()
        
    def upper(self):
        return self.string.upper()
        
    def __str__(self):
        return self.string
        
    def __repr__(self):
        return f'MutableString({repr(self.string)})'
        
    def __len__(self):
        return len(self.string)
        
    def __iter__(self):
        yield from self.string
        
    def __getitem__(self, key):
        return MutableString(self.string[key])

    def __setitem__(self, key, value):
        string = list(self.string)
        string[key] = value
        self.string = ''.join(string)
        
    def __delitem__(self, key):
        string = list(self.string)
        del string[key] 
        self.string = ''.join(string)
           
            
    def __add__(self,other):
        if isinstance(other,MutableString):
            return MutableString(self.string+other.string)
            
# INPUT DATA:

# TEST_1:
mutablestring = MutableString('beegeek')

print(*mutablestring)
print(str(mutablestring))
print(repr(mutablestring))

# TEST_2:
mutablestring = MutableString('Beegeek')

mutablestring.lower()
print(mutablestring)
mutablestring.upper()
print(mutablestring)

# TEST_3:
mutablestring1 = MutableString('bee')
mutablestring2 = MutableString('geek')

print(mutablestring1 + mutablestring2)
print(mutablestring2 + mutablestring1)

# TEST_4:
mutablestring = MutableString('beegeek')

print(mutablestring)
mutablestring[0] = 'B'
mutablestring[-4] = 'G'
print(mutablestring)

# TEST_5:
mutablestring = MutableString('beegeek')

s1 = mutablestring[2:]
s2 = mutablestring[:5]
s3 = mutablestring[2:5:2]

print(s1, type(s1))
print(s2, type(s2))
print(s3, type(s3))

# TEST_6:
mutablestring = MutableString('Ada Wong')
id1 = id(mutablestring)

mutablestring.upper()
id2 = id(mutablestring)

print(id1 == id2)

# TEST_7:
string = '''For a long time it was a mystery to me how something very expensive and technologically advanced could be 
so useless. And I soon realized that a computer is a stupid machine that has the ability to do incredibly smart things, 
while programmers are smart people who have a talent for doing incredibly stupid things. In short, 
they found each other.
Bill Bryson'''

mutablestring1 = MutableString(string)
mutablestring2 = mutablestring1[20:45]

print(mutablestring1 is mutablestring2)

# TEST_8:
string = '''Sometimes it's better to stay home on Monday than to spend the whole week debugging code written on Monday.
Christopher Thompson'''
mutablestring = MutableString(string)

print(mutablestring[30], mutablestring[3], mutablestring[66], mutablestring[66], mutablestring[1], sep='')

# TEST_9:
string = '''Many of you are familiar with the virtues of being a programmer. There are only three of them, 
and of course this is: laziness, impatience and pride. Larry Wall'''
mutablestring = MutableString(string)

print(mutablestring[20])
print(mutablestring[-30])
print(mutablestring[:11])
print(mutablestring[16:])
print(mutablestring[4::10])
print(mutablestring[::-10])

# TEST_10:
string1 = MutableString('Разбежавшись')
string2 = MutableString('прыгну')
string3 = MutableString('со скалы')

array = [string1, string2, string3]
print(array)

# TEST_11:
mutablestring = MutableString()
print(repr(mutablestring))

# TEST_12:
mutablestring = MutableString('beegeek')

del mutablestring[2:5]
del mutablestring[1:5:2]
print(mutablestring)

# TEST_13:
mutablestring = MutableString('beegeek')

mutablestring[-1] = 'ee'
print(mutablestring)

mutablestring[-2:] = 'geek'
print(mutablestring)

# TEST_14:
mutablestring = MutableString('beegeek')

del mutablestring[1:3]
print(mutablestring)
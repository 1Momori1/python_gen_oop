'''
Класс NonNegativeInteger
Реализуйте класс NonNegativeInteger, описывающий дескриптор, который проверяет, что устанавливаемое или изменяемое значение атрибута является неотрицательным целым числом. При создании экземпляра класс должен принимать два аргумента в следующем порядке:

name — имя атрибута, за которым будет закреплен дескриптор
default — значение по умолчанию. Если не передан, имеет значение None
При обращении к атрибуту дескриптор должен возвращать значение этого атрибута, если оно установлено. Если значение не установлено, должно возвращаться значение по умолчанию, указанное при создании дескриптора. Если значение по умолчанию равняется None, должно быть возбуждено исключение AttributeError с текстом:

Атрибут не найден
При установке или изменении значения атрибута дескриптор должен проверять, является ли это значение неотрицательным целым числом. Если значение не является неотрицательным целым числом, должно быть возбуждено исключение ValueError с текстом:

Некорректное значение
Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 2. Никаких ограничений касательно реализации класса NonNegativeInteger нет, она может быть произвольной.
'''



class NonNegativeInteger:
    def __init__(self, name, default=None):
        self._name = name
        self.default = default
        
    def __get__(self,obj,cls):
        if obj is None:
            return self
        if self._name not in obj.__dict__:
            if self.default is None:
                raise AttributeError ('Атрибут не найден')
            else:
                return self.default
        return obj.__dict__[self._name]       

    
    def __set__(self,obj,value):
        if not isinstance(value,int) or value<0:
            raise ValueError ('Некорректное значение')
        obj.__dict__[self._name] = value
   
# INPUT DATA:

# TEST_1:
class Student:
    score = NonNegativeInteger('score')

student = Student()
student.score = 90

print(student.score)

# TEST_2:
class Student:
    score = NonNegativeInteger('score', 0)

student = Student()

print(student.score)
student.score = 0
print(student.score)

# TEST_3:
class Student:
    score = NonNegativeInteger('score')

student = Student()

try:
    print(student.score)
except AttributeError as e:
    print(e)

# TEST_4:
class Student:
    score = NonNegativeInteger('score')

student = Student()

try:
    student.score = -90
except ValueError as e:
    print(e)

# TEST_5:
class Student:
    score = NonNegativeInteger('score')

student = Student()
student.score = 90

try:
    student.score = -90
except ValueError as e:
    print(e)

# TEST_6:
class Student:
    score = NonNegativeInteger('score')

student = Student()

not_supported = [1.2, {1: 'one'}, {1, 2, 3}, [4, 5, 6], (7, 8, 9), '14']

for item in not_supported:
    try:
        student.score = item
    except ValueError as e:
        print(e)

# TEST_7:
class Student:
    score = NonNegativeInteger('score')

print(Student.score.__class__)        
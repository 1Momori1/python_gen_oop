'''
Класс Queue 🌶️
Очередь — абстрактный тип данных с дисциплиной доступа к элементам "первый пришёл — первый вышел". Добавление элемента возможно лишь в конец очереди, выборка — только из начала очереди, при этом выбранный элемент из очереди удаляется.

Реализуйте класс Queue, описывающий очередь. При создании экземпляра класс должен принимать произвольное количество позиционных аргументов, каждый из которых является элементом очереди. Порядок следования аргументов образует порядок элементов в очереди, то есть первый аргумент — первый элемент очереди, второй аргумент — второй элемент очереди, и так далее.

Класс Queue должен иметь два метода экземпляра:

add() — метод, принимающий произвольное количество позиционных аргументов и добавляющий их в конец очереди в том порядке, в котором они были переданы
pop() — метод, удаляющий из очереди первый элемент и возвращающий его. Если очередь пуста, метод должен вернуть значение None
Экземпляр класса Queue должен иметь следующее неформальное строковое представление:

<первый элемент очереди> -> <второй элемент очереди> -> <третий элемент очереди> -> ...
Помимо этого, экземпляры класса Queue должны поддерживать между собой операции сравнения с помощью операторов == и!=. Две очереди считаются равными, если они имеют равную длину и содержат равные элементы на равных позициях.

Также экземпляры класса Queue должны поддерживать между собой операцию сложения с помощью операторов + и +=:

результатом сложения с помощью оператора + должен являться новый экземпляр класса Queue, представляющий очередь со всеми элементами исходных очередей: сначала все элементы левой очереди, затем все элементы правой очереди
результатом сложения с помощью оператора += должен являться левый экземпляр класса Queue, представляющий очередь, к которой добавлены все элементы правой очереди
Наконец, экземпляр класса Queue должен поддерживать операцию побитового сдвига вправо на целое число n с помощью оператора >>, результатом которой должен являться новый экземпляр класса Queue, представляющий исходную очередь без первых n элементов. Если n больше или равно длине исходной очереди, результатом должен являться экземпляр класса Queue, представляющий пустую очередь.

Примечание 1. Если объект, с которым выполняется операция сравнения или арифметическая операция, некорректен, метод, реализующий эту операцию, должен вернуть константу NotImplemented.

Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 3. Никаких ограничений касательно реализации класса Queue нет, она может быть произвольной.
'''
class Queue:
    def __init__(self, *args):
        self.queue = list(args)
        
    def __str__(self):
        return f'{" -> ".join(map(str,self.queue))}'
        
    def  __eq__(self,other):
        if isinstance(other,Queue):
            f1 = len(self.queue)==len(other.queue)
            f2 = self.queue == other.queue
            return f1 and f2
                    
        else:
            return NotImplemented
            
    def add(self,*args):
        self.__iadd__(args)
        
    def pop(self):
        if self.queue:  
            return self.queue.pop(0)
        return None
        
    def __add__(self,other):
        if isinstance(other,Queue):
            new_queue = self.queue+other.queue
            return Queue(*new_queue)
        else:
            return NotImplemented
            
    def __iadd__(self,other):
        if isinstance(other,Queue):
            self.queue+=other.queue

            return self
        elif isinstance(other,(tuple,int,float)):
            self.queue+=other

            return self
        else:
            return NotImplemented
            
    def __rshift__(self,n):
        if isinstance(n,int):
            if n >= len(self.queue):
                return Queue('')
            else:
                return Queue(*self.queue[n:])
        else:
            return NotImplemented    
        
          
      
# INPUT DATA:

# TEST_1:
queue = Queue(1, 2)
queue.add(3)
queue.add(4, 5)

print(queue)
print(queue.pop())
print(queue)

# TEST_2:
queue1 = Queue(1, 2, 3)
queue2 = Queue(1, 2)

print(queue1 == queue2)
queue2.add(3)
print(queue1 == queue2)

# TEST_3:
queue1 = Queue(1, 2, 3)
queue2 = Queue(4, 5)
print(queue1 + queue2)

print('444444444444')
# TEST_4:
queue1 = Queue(1, 2, 3)
queue2 = Queue(4, 5)

queue1 += queue2

print(queue1)

# TEST_5:
queue = Queue(1, 2, 3, 4, 5)

print(queue >> 3)

# TEST_6:
queue = Queue(1, 2, 3, 4, 5)
id1 = id(queue)
print(queue)

queue += Queue(6, 7, 8, 9, 10)
id2 = id(queue)

print(queue)
print(id1 == id2)

queue = queue + Queue(11, 12, 13, 14, 15)
id3 = id(queue)

print(queue)
print(id1 == id3)

# TEST_7:
queue = Queue(*'beegeek')
for i in range(9):
    print(f'Queue >> {i} =', queue >> i)

# TEST_8:
queue = Queue(1)
item = queue.pop()
print(item)
print(queue.pop())

# TEST_9:
q1 = Queue(1, 2)
q2 = Queue(1, 2)

print(q1 == q2)
print(q1 != q2)

# TEST_10:
queue = Queue(1, 2, 3)
print(queue.__add__([]))
print(queue.__iadd__('bee'))
print(queue.__rshift__('geek'))
import threading
import time
from threading import Thread
import queue
from time import sleep

class Table:
    def __init__(self, number):
        self.number = number
        self.is_busy = False

class Cafe:
    def __init__(self, tables):
        self.tables = tables
        self.q = queue.Queue()

    def customer_arrival(self):
        for i in range(1, 21):
            print(f'Посетитель номер {i} прибыл')
            customer = Customer(i, self)
            customer.start()
            sleep(1)

    def serve_customer(self, customer):
        a = False
        for i in self.tables:
            if not i.is_busy:
                i.is_busy = True
                print(f'Посетитель номер {customer.number} сел за стол {i.number}')
                sleep(5)
                i.is_busy = False
                print(f'Посетитель номер {customer.number} покушал и ушел')
                a = True
                break
            if not a:
                print(f'Посетитель номер {customer.number} ожидает свободный стол')
                self.q.put(customer)
                self.q.get()

class Customer(Thread):
    def __init__(self, number, cafe):
        threading.Thread.__init__(self)
        self.number = number
        self.cafe = cafe

    def run(self):
        self.cafe.serve_customer(self)






table1 = Table(1)
table2 = Table(2)
table3 = Table(3)

tabl = [table1, table2, table3]
cafe = Cafe(tabl)

customer_arrival_thread = threading.Thread(cafe.customer_arrival())

customer_arrival_thread.start()

customer_arrival_thread.join()







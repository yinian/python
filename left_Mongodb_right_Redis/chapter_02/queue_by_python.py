#!/usr/bin/python3

import time
import random
from queue import Queue
from threading import Thread


class Producer(Thread):  # 生产者
    def __init__(self, queue):
        super().__init__()  # 显式调用父类的初始化方法
        self.queue = queue

    def run(self):
        while True:
            a = random.randint(0, 10)  # 在0-10之间生成一个随机整数
            b = random.randint(90, 100)
            print(f'生产者生产了两个数字: {a},{b}')
            self.queue.put((a, b))  # 把连个数字用元组的形式放进队列中
            time.sleep(2)


class Consumer(Thread):
    def __init__(self, queue):
        super().__init__()
        self.queue = queue

    def run(self):
        while True:
            num_tuple = self.queue.get(
                block=True)  # block = True 表示，如果队列为空则阻塞在这里，直到队列有数据为止
            sum_a_b = sum(num_tuple)
            print(f'消费者消费了一组数, {num_tuple[0]} + {num_tuple[1]} = {sum_a_b}')
            time.sleep(random.randint(0, 10))


queue = Queue()
producer = Producer(queue)
consumer = Consumer(queue)

producer.start()
consumer.start()
while True:
    time.sleep(1)
'''
由于生产过程和消费过程的时间不对等， 所以， 可能会出现生产者
生产的数据堆积在队列中的情况;
缺点：
    * 如果消费者每次暂停的时间都小于2秒， 那么队列始终是空的，来一组数立刻就被消费
    * 如果消费者每次暂停的时间都大于2秒， 那么队列里的数就会越来越多
'''

import sched
import time

s = sched.scheduler(time.time, time.sleep)

s.enter(2, 1, print, argument=('first'))
s.enter(3, 1, print, argument=('second'))

s.run()


start = '2018-08-12 7:35:15.629694'
stop = '2018-08-12 7:40:15.629694'

sc = sched.scheduler(time.time, time.sleep)

sc.enter(4, 1, print, argument=('third'))

sc.run()


def outer(num):
    def inner(num):
        return num - 2
    nums = inner(num)
    print(num, nums)


outer(3)


from datetime import datetime
print(datetime.today())

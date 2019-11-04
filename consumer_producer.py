import queue
import threading

q = queue.Queue()
max_thread_num = 5
threads = []


def consumer():
    while True:
        e = q.get()
        if e:
            # do you thing here
            print("Threading %s elem %s" %
                  (threading.current_thread().getName(), e))
            q.task_done()  # know that e has been processed
        else:
            return


# create a number of threads
for i in range(max_thread_num):
    t = threading.Thread(target=consumer)
    t.start()
    threads.append(t)


# producer
for i in range(1, 101):
    q.put(i)

q.join()  # block until all element are processed
q.put(None)  # to make threads returned

for t in threads:
    t.join()

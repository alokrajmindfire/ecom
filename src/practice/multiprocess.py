from multiprocessing import Process, cpu_count
import time

def counter(num):
    count = 0
    while count < num:
        count +=1
        print("counter: ",count)

def main():
    a = Process(target=counter,args = (30000000000,))
    b = Process(target=counter,args = (30000000000,))
    c = Process(target=counter,args = (30000000000,))
    a.start()
    b.start()
    c.start()
    a.join()
    b.join()
    c.join()
    print("Finished in : ",time.perf_counter(), "sec")

if __name__ == '__main__':
    main()
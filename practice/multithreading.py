import threading
import requests
import time

urls = [
    "https://httpbin.org/delay/2",
    "https://httpbin.org/delay/3",
    "https://httpbin.org/delay/1",
    "https://httpbin.org/delay/2",
]

def fetch_url(url):
    print(f"Fetching {url}")
    response = requests.get(url)
    print(f"Done {url} -> {response.status_code}")

start = time.time()
threads = []

def main():
    for url in urls:
        t = threading.Thread(target=fetch_url, args=(url,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()
    print(f"All fetched in {round(time.time() - start, 2)}s")


if __name__ == '__main__':
    main()
    
    
    
# GIL - Global Interpreter Lock 
# Due to this in python only one thread can be inteperated at a time

# Then how we can achive
# Multiprocessing
# Each process got it's own interperator and it's GIL
# Asynchronous Programing

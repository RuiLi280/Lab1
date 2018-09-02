import requests
from multiprocessing import Process


def http_call():
    r = requests.get("https://webhook.site/21ded089-3a49-4767-b54b-cca79f2e3d91")
    print(r.headers['Date'])


def http_async_call():
    processes = [Process(target=http_call) for i in range(3)]
    for p in processes:
        p.start()
    
    for p in processes:
        p.join()


if __name__ == '__main__':
    http_async_call()
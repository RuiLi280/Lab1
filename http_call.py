import requests


def http_call():
    for i in range(3): 
        r = requests.get("https://webhook.site/21ded089-3a49-4767-b54b-cca79f2e3d91")
        print(r.headers['Date'])


if __name__ == '__main__':
    http_call()
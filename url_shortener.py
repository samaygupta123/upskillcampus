from urllib.parse import urlencode
from urllib.request import urlopen
import contextlib

def make_mini(url):
    request_url = ("http://tinyurl.com/api-create.php?"+urlencode({'url':url}))
    with contextlib.closing(urlopen(request_url)) as response:
        return response.read().decode('utf-8')

if __name__ == "__main__":
    url = input("Enter the URL to shorten: ")
    mini_url = make_mini(url)
    print("The shortened URL is:", mini_url)
import urllib.request as urllib

def connectivity(url):
    print("Checking Connectivity .........")
    response = urllib.urlopen(url)
    print(f"Connecting to the {url}")
    print("Response is : ", response.headers.items())

print("Site Connection Checking")
url = input("Enter the url : ")
connectivity(url)
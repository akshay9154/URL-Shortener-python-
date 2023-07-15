import pyshorteners

url=input("Enter the Link: ")

def shortenurl(url):
    s=pyshorteners.Shortener()
    print("shorten url:",s.tinyurl.short(url))

shortenurl(url)
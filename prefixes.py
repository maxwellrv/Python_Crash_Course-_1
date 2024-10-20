# You can remove prefixes from strings with the removeprefix() method
url = "https://simplycyber.com"
new_url = url.removeprefix("https://")
print (new_url)

#make prefix removals permanent by assigning them to the original variable name. 
url = url.removeprefix("https://")
print(url)
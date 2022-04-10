"""
Extract the domain name from a URL: https://www.codewars.com/kata/514a024011ea4fb54200004b/train/python
Write a function that when given a URL as a string, parses out just the domain name and returns it as a string.

by far most challenging kata for me

my other solution: 
import tldextract

def domain_name(url):
    domain = tldextract.extract(url)
    return domain.domain
"""

def domain_name(url):
    dompar = url.split(".")
    
    if dompar[0][:1] == "h":
        if dompar[0].split("//")[1] == "www":
            return dompar[1]
        elif "https" in dompar[0]:
            dompar[0] = dompar[0][8:]
        elif "http" in dompar[0]:
            dompar[0] = dompar[0][7:]
        return dompar[0]
    if dompar[0][:3] == "www":
        return dompar[1]
    return dompar[0]


    #if dompar[0] == "http://www":
    #    return dompar[1]
    #elif dompar[0] == "http://" or dompar[0] == "www":
    #    return dompar[1]
    #elif len(dompar[0])>7:
    #    return dompar[0].split("//")[1]
    #elif dompar[0][:1] != "h" or dompar[0][:1] != "w":
    #    return dompar[0]

    # elif dompar[0][1:] != "h" or "w":
    #   return dompar[0].split("//")[1]



print(domain_name("http://google.com"))



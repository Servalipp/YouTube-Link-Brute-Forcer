import random
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.firefox.options import Options

_ytURL = 'https://youtu.be/'

base = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
        'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','Y','X','Y','Z',
        '0','1','2','3','4','5','6','7','8','9',
        '-','_']

options = Options()
options.headless = True

driver = webdriver.Firefox(options = options)
print("Driver Initiated")

'''Math says that if there are 5,000,000,000 videos on youtube, and youtube
uses base64 (managed by the array 'base' above) 11 times, then 5,000,000,000 is what percent of 64^11(7.3786976e+19):
You have                              a 0.000000006776263605111016% chance of getting a valid link.
to make those odds clear, you have    a 0.00008183306055646482% chance of getting struck by lightning,
                                      a 0.000007151123842018516% chance of winning the lottery
                                      a 0.0000015105619199406354% chance of choking right now (if you live in the US)'''
#I could have an ever growing library of already tried links, but the number is so huge, that it really is not even a reality that it would generate the same 2 links to begin with

#Generates a random url
def randomGen():
    output = _ytURL
    for x in range(11):
        output += base[random.randint(1,64)]
    return output

#Checks if it is valid with Selenium
def testSite():
    url = randomGen()
    driver.get(url)
    print("Driver Url is "+url)
    try:
        driver.find_element_by_class_name('style-scope yt-player-error-message-renderer')
    except:
        print("Url is successful! "+url)
        validLinksFile = open("validLinks.txt", "a")
        validLinksFile.write(url+'\n')
        validLinksFile.close()
    else:
        print("Invalid Link! Trying next...")

while True:
    testSite()

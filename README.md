#YouTube Link Brute Forcer
A small script written in python with Selenium.
###What does it do?
This script randomly generates YouTube links, randomly picking 11 characters from an array of 64, using YouTubes own modified base64 algorithm.
It then tries those links one after one, using **Selenium**'s Firefox Webengine. If the link is invalid, it will generate a new one. However,
if it IS valid, then it will add it to a .txt file called **validLinks.txt**.
###What are the chances that I will get a valid link?
Good question. I did some shoddy math that might not even be valid, but heres an estamation from a portion of code.
```Math says that if there are 5,000,000,000 videos on youtube, and youtube
uses base64 (managed by the array 'base' in the script) 11 times, then 5,000,000,000 is what percent of 64^11(7.3786976e+19):
You have                              a 0.000000006776263605111016% chance of getting a valid link.
to make those odds clear, you have    a 0.00008183306055646482% chance of getting struck by lightning,
                                      a 0.000007151123842018516% chance of winning the lottery
                                      a 0.0000015105619199406354% chance of choking this year (if you live in the US)
```
Also, if the page doesnt load correctly, or not fast enough, **the code might recognise it as valid. So most of the links inside validLinks.txt are probably invalid.**
###How do I get this working?
You have to download the script, and make sure you have <= python 3.7 installed.
Then you need selenium. `pip install selenium` should work.
After that, you need to download Firefox's **GeckoDriver** executable.
This can be found [here](https://github.com/mozilla/geckodriver/releases).
Make sure it is x86_64 (64 bit).
And thats it, you should now be able to run the python script successfully.
**If you see "Invalid Link!" that means its working! That just means that the link doesnt have a successful youtube video. There should be a LOT of these.**
###Is this optimized?
HAHAHAHAHA good one. No this script is pretty slow... I don't really know how to multithread, let alone code in python. Im still figuring stuff out.

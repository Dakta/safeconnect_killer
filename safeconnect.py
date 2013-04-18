import re
import urllib2
import time
import sys

def log(output):
    print output
    log = open("log", 'a')
    log.write("%s: %s\n" % (time.asctime(), output))
    log.close()

sys.stdin.close()
#sys.stdout.close()
#sys.stderr.close()

IPHONE_USER_AGENT = """Mozilla/5.0 (iPhone; U; CPU like Mac OS X; en) AppleWebKit/420+ (KHTML, like Gecko) Version/3.0 Mobile/1A534a Safari/419.3"""
RAZR_CHROME_AGENT = """Mozilla/5.0 (Linux; Android 4.0.4; DROID RAZR Build/6.7.2-180_DHD-16_M4-31) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19"""
IPAD_USER_AGENT = """Mozilla/5.0(iPad; U; CPU iPhone OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B314 Safari/531.21.10"""
XBOX_USER_AGENT = """Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0; Xbox)"""

useragents = [IPHONE_USER_AGENT, RAZR_CHROME_AGENT, IPAD_USER_AGENT, XBOX_USER_AGENT]

userAgentSelector = 0

while True:
    userAgent = useragents[userAgentSelector]
    userAgentSelector = (userAgentSelector + 1) % len(useragents)
    try:
        req = urllib2.Request('https://134.82.251.66:9443')
        req.add_header('User-agent', userAgent)
        log("Requesting URL with useragent\n%s" % userAgent)
        res = urllib2.urlopen(req)
        res.close()
        log("Beat SafeConnect")
    except:
        log("Returned Error")

    time.sleep(10)


import webbrowser
import time

print('\nYou can Enter One of The Following Websites By Entering Their First two Alphabets\n')
print('     ','-'*79)
print('      | Google | Youtube | Facebook | Wikipedia | Microsoft | Twitter | AmazonPrime |')
print('     ','-'*79)
print('      |  TED   | LinkedIn|  Netflix |   Gmail   |   Amazon  |  Quora  |  Instagram  |')
print('     ','-'*79)
print('''Example
         for YouTube. Enter yo or YO.\n''')   

youtube="https://www.youtube.com/"
facebook="https://www.facebook.com/"
wiki="https://en.wikipedia.org/wiki/Main_Page"
amazon="https://www.amazon.com/"
twitt="https://twitter.com/explore"
insta="https://www.instagram.com/"
quora="https://www.quora.com/"
google="https://www.google.com/"
ted="https://www.ted.com/"
linkedin="https://www.linkedin.com/"
netflix="https://www.netflix.com/in/"
gmail="https://www.gmail.com/mail/help/intl/en/about.html?utm_expid=..."
microsoft="https://www.microsoft.com/en-in"
prime="https://www.primevideo.com/?ref_=dvm_pds_amz_in_as_s_b_brand1|m_lgAX6a65c_c"

while True:
    w1=input('Site Alphabets:')
    if w1=='yo' or w1=='YO':
         url=youtube
         print(' \n         YouTube')
         break
    elif w1=='fa' or w1=='FA':
         url=facebook
         print('\n           Facebook')
         break
    elif w1=='wi' or w1=='WI':
         url=wiki
         print('\n           Wikipedia')
         break
    elif w1=='am' or w1=='AM':
         url=amazon
         print('\n           Amazon')
         break
    elif w1=='tw' or w1=='TW':
         url=twitt
         print('\n          Twitter')
         break
    elif w1=='in' or w1=='IN':
         url=insta
         print('\n           Instagram')
         break
    elif w1=='qu' or w1=='QU':
         url=quora
         print('\n           Quora')
         break
    elif w1=='go' or w1=='GO':
         url=google
         print('\n           Google')
         break
    elif w1=='te' or w1=='TE':
         url=ted
         print('\n           TED')
         break
    elif w1=='li' or w1=='LI':
         url=linkedin
         print('\n           LinkedIn')
         break
    elif w1=='ne' or w1=='NE':
         url=netflix
         print('\n           Netflix')
         break
    elif w1=='gm' or w1=='GM':
         url=gmail
         print('\n           Gmail')
         break
    elif w1=='mi' or w1=='MI':
         url=microsoft
         print('\n           Microsoft')
         break
    elif w1=='pr' or w1=='PR':
         url=prime
         print('\n           Amazon Prime')
         break

    else:
        print('U have Entered Wrong Term')
        continue        

        
         

        
print('\n     ','-'*39)
print('     | Chrome | Mozilla | Internet Explorer |')
print('     ','-'*39) 
    
while (True):
    b=input('Select ur Appropriate Browser by entering its first alphabet:')
    
    if b=='c' or b=='C':
         print('U have Choosen Chrome')
         time.sleep(1)
         webbrowser.register('chrome',None,webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
         webbrowser.open(url)
         break
    elif b=='m' or b=='M':
        print('U have Choosen Mozila')
        time.sleep(1)
        webbrowser.register('firefox',None,webbrowser.BackgroundBrowser("C://Program Files//Mozilla Firefox//firefox.exe"))
        webbrowser.get('firefox').open(url)
        break
    elif b=='i' or b=='I':
        print('U have Choosen Internet Explorer')
        time.sleep(1)
        ie=webbrowser.get("C:\Program Files\Internet Explorer\iexplore.exe")
        ie.open(url)
        break

    else:
        print('U have Entered Wrong Term')
        continue




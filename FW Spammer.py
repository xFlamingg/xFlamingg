import colorama
from colorama import Fore
colorama.init(autoreset=True)
import os, requests 
os.system("title Flame Webhook Spammer ^| xFlamingg")
import time
 

 
banner = f"""{Fore.YELLOW} 
 (               (                                       
  )\ ) (  (       )\ )                                    
 (()/( )\))(   ' (()/(          )    )      )     (  (    
  /(_)|(_)()\ )   /(_))`  )  ( /(   (      (     ))\ )(   
 (_))_|(())\_)() (_))  /(/(  )(_))  )\  '  )\  '/((_|()\  
 | |_ \ \((_)/ / / __|((_)_\((_)_ _((_)) _((_))(_))  ((_) 
 | __| \ \/\/ /  \__ \| '_ \) _` | '  \() '  \() -_)| '_| 
 |_|    \_/\_/   |___/| .__/\__,_|_|_|_||_|_|_|\___||_|   
                     |_|             
                                       
                                          Flame Webhook Spammer
                                            by xFlamingg 
""" 

 
 
print(banner)
message = input(" Message in webhook: ")
url = input(" Webhook URL: ")
delay = input(" Delay: ")
delay = float(delay)
while True:
  try:
    time.sleep(delay)
    r = requests.post(url, json={"content": message})
    if r.status_code == 204:
      print(f" {Fore.GREEN}[+]{Fore.WHITE} Message sent")
  except:
    print(f" {Fore.RED}[-]{Fore.WHITE} Invalid Webhook URL")
    time.sleep(10)          
    quit(0)
 
 

 

 
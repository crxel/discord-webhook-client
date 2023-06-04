import time
import requests
from colorama import Fore, Style
import os

os.system('cls')
def main():
    banner = fr"""{Fore.BLUE + Style.BRIGHT}
      _ _                       _                _     _                 _           _ _            _   
     | (_)                     | |              | |   | |               | |         | (_)          | |  
   __| |_ ___  ___ ___  _ __ __| | __      _____| |__ | |__   ___   ___ | | __   ___| |_  ___ _ __ | |_ 
  / _` | / __|/ __/ _ \| '__/ _` | \ \ /\ / / _ \ '_ \| '_ \ / _ \ / _ \| |/ /  / __| | |/ _ \ '_ \| __|
 | (_| | \__ \ (_| (_) | | | (_| |  \ V  V /  __/ |_) | | | | (_) | (_) |   <  | (__| | |  __/ | | | |_ 
  \__,_|_|___/\___\___/|_|  \__,_|   \_/\_/ \___|_.__/|_| |_|\___/ \___/|_|\_\  \___|_|_|\___|_| |_|\__|

  by crxelty                                                                                                                                                                                    
    """
    print(banner)
    
    webhook = input(fr"{Fore.BLUE + Style.BRIGHT}Input webhook: ")

    def messages():
        
        message = input(fr"{Fore.BLUE + Style.BRIGHT}Message : ")
        data = {
      "content" : f"{message}",
        }

        sendmessage = requests.post(webhook, json = data)
        try:
            sendmessage.raise_for_status()
        except requests.exceptions.HTTPError as e:
            print(fr"{Fore.RED}Webhook is invalid.")
            time.sleep(1)
            exit()
        else:
            print(fr'{Fore.BLUE + Style.BRIGHT}Successfully sent message "{message}" to "{webhook}"')
        messages()

    messages()

main()
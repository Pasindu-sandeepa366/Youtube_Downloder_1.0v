import subprocess
import os
import time
def logo():
    print(""" \033[1;31;40m 
                     __   __          _         _          
                     \ \ / /__  _   _| |_ _   _| |__   ___ 
                      \ V / _ \| | | | __| | | | '_ \ / _ )
                       | | (_) | |_| | |_| |_| | |_) |  __/
                       |_|\___/ \__,_|\__|\__,_|_.__/ \___|
                                                           
               ____                      _           _           
              |  _ \  _____      ___ __ | | ___   __| | ___ _ __ 
              | | | |/ _ \ \ /\ / / '_ \| |/ _ \ / _` |/ _ \ '__|
              | |_| | (_) \ V  V /| | | | | (_) | (_| |  __/ |   
              |____/ \___/ \_/\_/ |_| |_|_|\___/ \__,_|\___|_|   

    
    
    


                  [+] Coded_by_PASINDU_SANDEEPA
       \033[1;32;40m             [@] bombtiktiktik54321@gmail.com    
    
    """)


def main():
    logo()
    url=input("\033[1;34;40m[+] Input URL >> \033[1;32;40m")
    x=os.path.exists("Youtube_Downloder")
    if not x:
        os.mkdir("Youtube_Downloder")
    os.chdir("Youtube_Downloder")
    command="youtube-dl -F {0}".format(url)
    subprocess.call(command,shell=True)
    print("[+] Please wait....!")
    time.sleep(5)
    choice=input("\033[1;34;40m[+] Enter number>> \033[1;32;40m")
    command="youtube-dl -f {0} {1}".format(choice,url)
    subprocess.call(command,shell=True)
    print("\033[1;31;40m                      [+] Please restart you'r terminal after download complete..!")
    time.sleep(5)
    print("\n\n")
    




if __name__=="__main__":
    main() 
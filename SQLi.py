from googlesearch import search
import time
import requests
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:75.0) Gecko/20100101 Firefox/75.0'}

print ('''\033[1;34m

██████╗░███████╗░█████╗░██████╗░██╗░░░░░██╗░░░██╗
██╔══██╗██╔════╝██╔══██╗██╔══██╗██║░░░░░╚██╗░██╔╝
██║░░██║█████╗░░███████║██║░░██║██║░░░░░░╚████╔╝░
██║░░██║██╔══╝░░██╔══██║██║░░██║██║░░░░░░░╚██╔╝░░
██████╔╝███████╗██║░░██║██████╔╝███████╗░░░██║░░░
╚═════╝░╚══════╝╚═╝░░╚═╝╚═════╝░╚══════╝░░░╚═╝░░░

░██╗░░░░░░░██╗███████╗░█████╗░██████╗░░█████╗░███╗░░██╗
░██║░░██╗░░██║██╔════╝██╔══██╗██╔══██╗██╔══██╗████╗░██║
░╚██╗████╗██╔╝█████╗░░███████║██████╔╝██║░░██║██╔██╗██║
░░████╔═████║░██╔══╝░░██╔══██║██╔═══╝░██║░░██║██║╚████║
░░╚██╔╝░╚██╔╝░███████╗██║░░██║██║░░░░░╚█████╔╝██║░╚███║
░░░╚═╝░░░╚═╝░░╚══════╝╚═╝░░╚═╝╚═╝░░░░░░╚════╝░╚═╝░░╚══╝

                          \033[37mMade with \033[91m<3\033[37m DeadlyWeapon\033[1;m''')


q=str(input("\033[1;33;40mEnter your dork: "))
no=int(input("\033[1;33;40mEnter the number of results you want to search: "))
times=int(input("\033[1;33;40mEnter the timeout :"))
op=str(input("\033[1;33;40mDo you want to save the vulnerable sites(Y/n) :"))
if(op=="Y" or op=="y"):
 name=str(input("\033[1;33;40mEnter the name of your output file :"))
 print("\033[1;32;40mURLs will be saved in "+name)
 time.sleep(2)
 f=open(name,"a+")
i=1
for url in search(q,tld="com",num=no,stop=no,pause=2):
 if("php?" not in url):
  i=i+1
  continue   
 print("\033[1;37;40m"+str(i)+". \033[1;35;40mChecking in this URL: ")
 print("\033[1;34;40m"+url)
 try:
  checkurl=url+"%27"
  r=requests.get(url,headers=headers,timeout=times)
  s=requests.get(checkurl,headers=headers,timeout=times)
  if((s.url != checkurl) or ("af.org.pk" in url)):
   print("\033[1;31;40mNot Vulnerable!\n")
   i=i+1
   continue
  if(r.text==s.text):
   print("\033[1;31;40mNot Vulnerable!\n")
  else:
   print("\033[1;32;40mVulnerable.\n")
   if(op=="Y" or op=="y"):
    f.write(url+"\n")   
 except:
  print("\033[1;31;40mThis site can't be reached.")
  print("")
 i=i+1
try: 
 f.close()
 print("\033[1;32;40mURLs are saved in "+name)
except:
 pass

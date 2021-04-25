import pywhatkit
import time
import emoji
def yt_search(srch):
      print(f"{srch} will be searched on youtube and the most recent video will be played \n ")
      try:
          pywhatkit.playonyt(srch)
      except:
          print("you entered invalid address")

def whatsapp_msg():
      mob=input("Enter the mobile number to whom the message is to be sent\n")
      msg=input("Please type in your message\n")
      hr=int(input("Enter the time in 24-hour format at which the message is to be sent\n"))
      mn=int(input("Enter the minutes in which the message is to be sent\n"))
      try:
          pywhatkit.sendwhatmsg(("+91"+(mob)),msg,hr,mn)
      except Exception as e:
          print("Sorry! invalid input as",e)

'''FUNCTION UNDER CONTRUCTION------
def send_email():
    em_us=input("Enter your email address")
    pass_us=input("Enter your password")
    print("Don't worry your password won't be stored in our system")
    em_re=input("Enter the receiver's email address")
    con=input("Enter the content of the email")
    try:
        pywhatkit.sendMail(em_us,pass_us,em_re,con)
    except Exception as e:
        print("Invalid input as ",e)'''

def google_search(srch):
        print(f"{srch} will be searched on google and you will be redirected to it \n ")    
        try:
          pywhatkit.search(srch)
        except:
          print("Sorry! invalid input")

def info_search(srch):
        print(f"{srch} will be searched on wikipedia and 4 lines will be extracted from wikipedia and will be displayed on this terminal \n ")
        try:
         print("*************************************************")
         pywhatkit.info(srch,lines=4)
         print("*************************************************")
         time.sleep(7)
        except:
           print("Sorry! invalid input")

while(True):
    time.sleep(3)
    welcomeMsg = '''\n ====== Welcome ======
        I am here to make your browsing experience easier
        Please choose an option:
        1: Youtube search
        2: Google search
        3: Quick search
        4: Sending a Whatsapp message
        5: Exit 
        '''
    print(welcomeMsg)
    n=int(input("Please enter your choice\n"))
    if n<4:
     srch=input("Please enter the topic name you want to search \n")
    if n==1:
        yt_search(srch)
    elif n==2:
        google_search(srch)
    elif n==3:
        info_search(srch)
    elif n==4:
        whatsapp_msg()
    elif n==5:
        print("Thank you for using my service\n & I Hope you liked it!!")
        exit()
    else:
        print('''Sorry! 
Either the choice entered by you is still under development 
             OR
You have entered a wrong choice 
Please choose any of the choice from the dropdown menu below: ''')

import os
import pyttsx3

#  This code is created by Pramod Jitendra Yadav (py90490@gmail.com) from group id IISE_RISE.27.26 . I have used only that concepts that are taught by Vimal Daga Sir .I tried to create a software along with its manual in the 'help' command . I am eager to make the next version of this program using voice input
#  Hope You like It :)   

print("\n")
while 1:
    print("\nHello , write what to do :- ",end=" ")


    r = input()
    p = r.upper()                                                   # user can answer in any case
    # if " " in p or "" in p :                                        #in case of no input
     #   print("\n\tPlease write something \n")
      #  pyttsx3.speak("Please write something")
    
    if "DONT" in p or "NEVER" in p or "DO NOT" in p or "NEGATIVE" in p  :     # In case of Negative Input
        print("\n\t=> Ok As you wish\n")
        pyttsx3.speak(" => Ok as you wish")                           # discussed module so used for more user friendly and flexibility . 
                                                                #Thinking of how google responds
        
    elif "EXIT" in p or "STOP" in p or "CLOSE" in p or "TERMINATE" in p or "DISCARD" in p:   # In case of Exit from software launche
        print("\n\t => Thank you for using my Software Launcher\t:)\n")
        pyttsx3.speak("Thank you for using my Software Launcher")
        break
        
    elif("HELP" in p or "SUPPORT" in p):                                                    # In case user wants help or see software manual
            
        print("\n\t\t\t\t\t\t Welcome to my Software Launcher Help utility  :) ")
        print("\t\t\t\t\t\t---------------------------------------------------\n")
        pyttsx3.speak("Welcome to my Software Launcher Help utility")
        print(" \t=> You have to write your input in English only\n")
        print(" \t=> You can launch these softwares( Apps ) :- \n")
        print("\t\t\t\t\tCalculator , Notepad , Paint , Quick Assist ,  Chrome  ") 
        print("\t\t\t\t\tVlc Media Player , Visual Studio Code , Firefox Browser , KM Player ") 
        print("\t\t\t\t\tPicasa 3 , Windows  Fax and Scan , Snipping Tool\n")
            
        print(" \t=> In order to launch any software make sure you enter any keywords (Case-insensitive) like 'run', 'start','execute','open', 'launch' in your input \n")
        
        print(" \t=> Steps to create or modify environment variables on Windows :->\n\n\t\t1)\tRight click on the software and select Open file Location . Copy the address from the address bar\n\t\t2)\tRight-click the Computer icon and choose Properties, or in Windows Control Panel, choose System.\n\t\t3)\tChoose Advanced system settings. \n\t\t4)\tOn the Advanced tab, click Environment Variables.\n\t\t5)\tClick New to create a new environment variable.\n\t\t6)\tPaste the location of the software and click OK.\n ")
        print(" \n\t=> Steps to create or modify environment variables on Mac\n\n\t\tClick on link \t https://rb.gy/fdfxix  ") 
        print(" \n\t=> Steps to create or modify environment variables on Linux\n\n\t\tClick on link \t https://rb.gy/th8oxf \n")    
        
    elif(("RUN" in p) or ("LAUNCH" in p) or ("EXECUTE" in p) or ("START" in p) or ("OPEN" in p)):      # In open the software 
        if (("CODE" in p) or ("VS CODE" in p) or ( "VISUAL STUDIO CODE" in p) ):                      # launching software
            os.system("Code")
        elif (("CHROME" in p) or ("CHROME BROWSER" in p) or ( "GOOGLE CHROME" in p)):                  # launching software
            os.system("chrome")
        elif (("VLC" in p) or ("VLC PLAYER" in p) or ( "VLC MEDIA PLAYER" in p)):                  # launching software
            os.system("vlc")
        elif (("FIREFOX" in p) or ("FIREFOX BROWSER" in p)):                  # launching software
            os.system("firefox")
        elif (("PICASA" in p) or ("PICASA3" in p) or ("PICASA 3" in p)):                  # launching software
            os.system("picasa3")
        elif (("KMPLAYER" in p) or ("KM PLAYER" in p) or ("KM" in p)):                  # launching software
            os.system("KMPlayer")
        elif (("NOTEPAD" in p) or ("NOTEPAD EDITOR" in p) or ("NOTE" in p) ):                  # launching software
            os.system("notepad")
        elif (("CALC" in p) or ("CALCULATOR" in p) or ("CAL" in p)):                  # launching software
            os.system("CALC")
        elif(("WINDOWS FAX AND SCAN" in p) or ("WFS" in p) or ("WINDOWS FAX" in p) or ("WINDOWS SCAN" in p)):                     # launching software
            os.system("wfs")
        elif(("PAINT" in p) or ("MSPAINT" in p) or ("MS PAINT" in p) or ("MICROSOFT PAINT" in p)):                                            # launching software
            os.system("mspaint")
        elif(("QUICKASSIST" in p) or ("QUICK ASSIST" in p)):                                                              # launching software
            os.system("quickassist")
        elif("SNIPPING TOOL" in p):                                                                       # launching software
            os.system("snippingtool")
        else:
            print("\n")
            print("\t=> Please launch only supported softwares \n")
            print("\t=> Make sure you have the software file location in your user environment variable in case of any launching issue\n ")
                
            
            print("\t => Write '  help  '  to check supported softwares ( Apps )\n")
            pyttsx3.speak("Please launch only supported softwares \nMake sure you have the software file location in your user environment variable in case of any launching issue\n ")
    else:
        if p.isspace() :                                        #in case of no input 
                                                                # Used isspace as discussed the functions associated with string 
            print("\n\t => Please write something \n")
            pyttsx3.speak("Please write something")
        else:
            print("\n\t=> Sorry But I did not get what do you mean to say ! \n")
            pyttsx3.speak("Sorry But I did not get what do you mean to say")          # for no proper input
            print("\t=> Please write ' help ' for Software Manual Details\n")
    
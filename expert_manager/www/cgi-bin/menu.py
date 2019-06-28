from os import system
import pyttsx3
from subprocess import getoutput as go
import docker
import video_stream
import spacy as spy
import speech_recognition as sr
import face

def speakerfun(text):
    sp = pyttsx3.init()
    sp.say(text)
    sp.setProperty('rate',150)
    #sp.setProperty('voice','english+f1')
    sp.runAndWait()

def taketext(text):
    sp = pyttsx3.init()
    sp.say(text)
    sp.setProperty('rate',150)
    #sp.setProperty('voice','english+f1')
    sp.runAndWait()
    microphone = sr.Microphone()
    recognizer = sr.Recognizer()
    with microphone as source:
        audio = recognizer.listen(source)
        text = recognizer.recognize_google(audio)
        return text
    return "Becuase of some reasons i can't listen your voice"

def returnwords(tell):
    dict = spy.load('en_core_web_sm')
    text = taketext(tell)
    text = dict(text)
    words = []
    for x in text:
        words.append(str(x))
    return words

def returnmenu(words):
    if "video" in words or "stream" in words or "streaming" in words:
        return 1
    elif "docker" in words and ("setup" in words or "create" in words):
        return 2
    elif "docker" in words and ("run" in words or "start" in words or "initialize" in words):
        return 3
    elif ("amazon" in words or "aws" in words) and ("loggin" in words or "singin" in words or "login" in words):
        return 4
    elif ("amazon" in words or "aws" in words) and ("setup" in words or "configure" in words):
        return 5
    elif ("server" in words and "web" in words) and ("setup" in words or "configure" in words):
        return 6
    elif "mail" in words:
        return 7
    else:
        return 0




#system("tput setaf 1")
speaker=pyttsx3.init()
face.displayface()
speakerfun("Welcome to the automation service") 
while True:
    x = returnwords("Tell me what i can do for you")
    face.displayface()
    print(x)
    x = returnmenu(x)
    loc = returnwords("where you want to run your command")
    print(loc)
    if "local" in loc:
        if int(x)==1:
           system("python36 menu_video.py")

        elif int(x)==2:
           system("ansible-playbook ansible/docker.yml")

        elif int(x)==3:
           system("ansible-playbook ansible/docker_local.yml")
        elif int(x)==4:
           uName=input("enter your user name:")	
           go("useradd {}".format(uName))	
        elif int(x)==5:
           file_name=input("enter file name")	
           go("touch {}".format(file_name))
        elif int(x)==6:
           system("ansible-playbook ansible/local_web.yml")	
        else:
           print("not supported")
    elif "remote" in loc:
        if int(x)==1:
           video_stream.video_stream()

        elif int(x) == 2:
           ip = input("Enter the ip of remote system")
           system("echo '{}' >> hosts".format(ip))
           system("ansible-playbook ansible/docker_remote.yml")
           
        elif int(x) == 3:
           docker.docker_setup()

        elif int(x) == 4:
           aws_ip = input("Enter the public ip of your aws instance: ")
           system("sshpass ssh -l ec2-user {} -i /root/Downloads/aws_key.pem ".format(aws_ip))

        elif int(x) == 5:
           system("ansible-playbook --ask-vault-pass /ansible/aws.yml")
           	
        elif int(x) == 6:	
           system("ansible-playbook docker ansible/remote_web.yml")
        elif int(x) == 7:
           system("ansible-playbook  ansible/ansible_mail.yml")
           	
    final_choice = taketext("Do you want to continue")
    if final_choice == "yes":
        system("clear")
        continue
    else:
        break	

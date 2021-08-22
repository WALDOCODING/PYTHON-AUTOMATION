from selenium import webdriver
from selenium.webdriver.chrome.options import Options
opt=Options()

def mission_input():
    link=input("enter the website link: ")
    return link
link1=mission_input()



opt.add_argument('--start-maximized')
bro=webdriver.Chrome(options=opt)
bro.get("https://"+link1)



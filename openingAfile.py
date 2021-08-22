from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

opt=Options()

def mission_input():
    link=input("enter the website name:")
    return link
link1=mission_input()

opt.add_argument('--start-maximized')
bro=webdriver.Chrome(options=opt)
bro.get("https://google.com")

search=bro.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")
search.send_keys(link1)
search.send_keys(Keys.RETURN)
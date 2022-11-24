from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import pyautogui
import keyboard
import os
import time

def lenlist(test_list):
    counter = 0
    for i in test_list:
    
        # incrementing counter
        counter = counter + 1
    return counter

def sortphnnumber(f):
    res = [i for i in range(len(f)) if f.startswith("+91 ", i)]
    
    # printing result
    print("The start indices of the substrings are : " + str(res))
    listlength = lenlist(res) -1
    i = 0
    while i<= listlength:
        phntxt = open("dbtxt.txt", "a", encoding='utf-8', errors='ignore').write(f[int(res[i]):int(res[i])+16] + "\n")
        i = i+1

def savepagesource():
    get_source = driver.page_source
    open("old.txt", "w", encoding='utf-8', errors='ignore').write(get_source)


width, height= pyautogui.size()
width = int(width)
height = int(height)
new_width = (width / 3) / 2
new_height = height / 2


def sortwhatsappulti():
    dick = open("dbtxt.txt", "r").readlines()
    remdubli = [*set(dick)]
    remdubli = str(list(remdubli)).replace("'", "")
    remdubli = remdubli.replace("]", "")
    remdubli = remdubli.replace("[", "")
    remdubli = remdubli.replace(",", "")
    remdubli = remdubli.replace(r"\n", "\n")
    remdubli = remdubli.replace(" +91", "+91")
    remdubli = remdubli.replace("<", "")
    remdubli = remdubli.replace(r'"', "")
    open("sortedwpunsaved.txt", "w", encoding='ascii', errors='ignore').write(remdubli)
    dick = open("sortedwpunsaved.txt", "r").readlines()
    remdubli = [*set(dick)]
    remdubli = str(list(remdubli)).replace("'", "")
    remdubli = remdubli.replace("]", "")
    remdubli = remdubli.replace("[", "")
    remdubli = remdubli.replace(",", "")
    remdubli = remdubli.replace(r"\n", "\n")
    remdubli = remdubli.replace(" +91", "+91")
    remdubli = remdubli.replace(" ", "")
    remdubli = remdubli.replace("\n", "")
    remdubli = remdubli.replace("+91", "\n+91")
    open("sortedwpunsaved.txt", "w", encoding='ascii', errors='ignore').write(remdubli)

    dick = open("sortedwpunsaved.txt", "r").readlines()
    remdubli = [*set(dick)]
    remdubli = str(list(remdubli)).replace("'", "")
    remdubli = remdubli.replace("]", "")
    remdubli = remdubli.replace("[", "")
    remdubli = remdubli.replace(",", "")
    remdubli = remdubli.replace(r"\n", "\n")
    remdubli = remdubli.replace("\n", "")
    remdubli = remdubli.replace(" ", "")
    remdubli = remdubli.replace("+91", "\n+91")
    open("sortedwpunsaved.txt", "w", encoding='ascii', errors='ignore').write(remdubli)
    g = open("sortedwpunsaved.txt", "r", encoding='ascii', errors='ignore').readlines()
    open("wpoutput.txt", "w", encoding='ascii', errors='ignore')
    i = 1
    while i < len(g):
        io = str(g[i]).replace("\n", "")
        io = io[0:3] + " " + io[3:8] + " " + io[8:13]
        print(io)
        open("wpoutput.txt", "a", encoding='ascii', errors='ignore').write(io+"\n")
        i = i+1





print('WELCOME TO WHATSAPP UNSAVED CONTACTS EXTRACTOR!!\nDEVELOPED BY -- XLR_8\n!!!TESTED ON RESOLUTION 1366X768!!!\n\n\n1) TO CONTINUE\n2) EXIT')
print("\n")
take = input("Enter your choice\n>>")
if take == "1":
    pass
elif take == "2":
    exit()
else:
    print("Invalid input\n>>")



open("dbtxt.txt", "w", encoding='utf-8', errors='ignore')
# Here Chrome will be used
driver = webdriver.Chrome()
str1 = driver.capabilities['browserVersion']
str2 = driver.capabilities['chrome']['chromedriverVersion'].split(' ')[0]

if str1[0:3] != str2[0:3]: 
  print("****************************please download correct chromedriver version**********************\n")
  time.sleep(5)
else:
    pass





  
# URL of the website 
url = "https://web.whatsapp.com/"


# Opening the URL
driver.get(url)
driver.fullscreen_window()
DP = WebDriverWait(driver, 10000).until(ec.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div[3]/header/div[1]/div/img")))

pyautogui.moveTo(new_width, new_height)


while True:
    if keyboard.is_pressed("s"):
        print("exit\n")
        driver.quit()
        break
    else:
        savepagesource()
        f = open("old.txt", "r", encoding='utf-8', errors='ignore').read()
        sortphnnumber(f)
        pyautogui.scroll(-200)

sortwhatsappulti()
os.remove("dbtxt.txt")
os.remove("old.txt")
os.remove("sortedwpunsaved.txt")





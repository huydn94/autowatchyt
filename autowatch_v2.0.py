import subprocess
import time
from tkinter import *
from tkinter import ttk
import psutil
import random
import tkinter as tk
from tkinter import messagebox
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pytube import YouTube 
#open new window



def open_new_window(url):
    #set path
    chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"  # Path to Chrome executable
    guest_profile_path = r"C:\Users\HuyDang\AppData\Local\Google\Chrome\User Data\Guest Profile"  # Path to guest profile directory

    # Set Chrome options
    options = Options()
    options.binary_location = chrome_path
    options.add_argument("--guest")
    options.add_argument("--user-data-dir={}".format(guest_profile_path))

    # Create a new instance of the Chrome driver with the specified options
    browser = webdriver.Chrome(options=options)
    # Open a new window
    browser.get(url)
    #time.sleep(5)
    button_play_selector="#movie_player > div.ytp-cued-thumbnail-overlay > button" 
    #playButton = browser.find_element(By.CSS_SELECTOR, button_play_selector)
    wait = WebDriverWait(browser, 10)
    playButton = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, button_play_selector)))
    playButton.click()
    time.sleep(watch_time)


#apply tham số
def apply_info():
    global numberofview, linklist, wait_time, lenlinklist, number_of_tab#, watch_time
    #watch_time = int(e5.get())
    number_of_tab = int(e4.get())
    wait_time = int(e3.get())
    numberofview = int(e1.get())
    linklist_txt = str(e2.get())
    linklist = linklist_txt.split(",")
    lenlinklist = len(linklist)
    #linklist_output = [link.split() for link in linklist_output]

#open từng link
def open_main():
    global watch_time
    j=0
    for i in range (numberofview):
        new_link_list = linklist
        for x in range (number_of_tab):
            random_link = random.choice(new_link_list) # lấy link ngẫu nhiên
            new_link_list = [x for x in linklist if x != random_link] #tạo list các link còn lại
            #lấy độ dài video
            yt=YouTube(random_link) 
            video_length = yt.length
            watch_time = (random.randint(25,99))*video_length
            #print (video_length)            
            open_new_window(random_link)   

            #time.sleep(20)
        j=j+1 #tăng biến đếm
        progress_bar['value']=(j*100//numberofview) #tăng giá trị cho progress bar
        pVal = str(j*100//numberofview) + "%"   #tăng giá trị cho label progress bar
        parent.update_idletasks()

        if j < numberofview:
            progress_label = Label(parent, text=pVal)
            progress_label.place(x=250, y=250)
            parent.update_idletasks()

        if j == numberofview:
            progress_label = Label(parent, text="DONE!")
            progress_label.place(x=250, y=250)
            parent.update_idletasks()   

        #print("lan thu: ",j)
        time.sleep(wait_time)
        close_all_chrome_windows()
        time.sleep(random.randint(25,100))

#    progress_bar.stop()
#close all chrome windows đã bật
def close_all_chrome_windows():
    chrome_processes = [proc for proc in psutil.process_iter() if proc.name() == "chrome.exe"]
    
    for proc in chrome_processes:
        try:
            proc.kill()
        except psutil.NoSuchProcess:
            pass
    # for proc in psutil.process_iter(['pid', 'name']):
    #     if proc.info['name'] == 'chrome.exe':
    #         proc.kill()


if __name__ == "__main__":
    parent = Tk()
    parent.geometry('300x300')

    #Number of view
    view = Label(parent, text = "Số view").place(x = 30, y = 50)
    e1 = Entry(parent)
    e1.place(x = 100, y = 50)
    
    #list of link
    link = Label(parent, text = "Link List").place(x = 30, y = 90)
    e2 = Entry(parent)
    e2.place(x = 100, y = 90)

    #wait time
    wait_time = Label(parent, text = "wait time").place(x = 30, y = 130)
    e3 = Entry(parent)
    e3.place(x = 100, y = 130)
    
    number_of_tab = Label(parent, text = "tab/list").place(x = 30, y = 170)
    e4 = Entry(parent)
    e4.place(x = 100, y = 170)

    watch_time = Label(parent, text = "watch time").place(x = 30, y = 210)
    e5 = Entry(parent)
    e5.place(x = 100, y = 210)

    apply_button = ttk.Button(parent, text='Apply', command=apply_info).grid(row = 4, column = 0)
    run_button = ttk.Button(parent, text='run', command=open_main).grid(row=4, column=1)
    #kill_button = ttk.Button(parent, text='close all', command=close_all_chrome_windows).grid(row=4, column=2)
    loading_label = Label(parent, text="Progress")
    loading_label.place(x = 30, y = 250)

    # Create a progress bar
    progress_bar = ttk.Progressbar(parent, mode="determinate", length=125)
    progress_bar.place(x = 100, y = 250)

    parent.mainloop()
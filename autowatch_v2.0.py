import time
from tkinter import *
from tkinter import ttk
import random
import tkinter as tk
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pytube import YouTube
import threading


time_count = 0

#apply tham số
def apply_info():
    global time_out, linklist, lenlinklist, number_of_tab
    number_of_tab = int(e4.get())
    #time_out = int(e1.get())
    linklist_txt = str(e2.get())
    linklist = linklist_txt.split(",")
    lenlinklist = len(linklist)
    #linklist_output = [link.split() for link in linklist_output]

#mở cửa sổ guest mới
def open_new_window(url):
    #set path
    chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"  # Path to Chrome executable
    #guest_profile_path = r"C:\Users\HuyDang\AppData\Local\Google\Chrome\User Data\Guest Profile"  # Path to guest profile directory

    # Set Chrome options
    options = Options()
    options.binary_location = chrome_path
    options.add_argument("--guest")
    #options.add_argument("--user-data-dir={}".format(guest_profile_path))

    # Create a new instance of the Chrome driver with the specified options
    browser = webdriver.Chrome(options=options)

    # Open a new window
    browser.get(url)

    button_play_selector="#movie_player > div.ytp-cued-thumbnail-overlay > button"
    #click nút play
    wait = WebDriverWait(browser, 10)
    playButton = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, button_play_selector)))
    playButton = browser.find_element(By.CSS_SELECTOR,button_play_selector)
    playButton.click()
    watch_time = watch_time_cr(url)
    print (watch_time)
    global time_count
    time_count= time_count + watch_time
    print (time_count)

    time.sleep(watch_time)
    
#open từng link
def open_main(thread_id):
    print(f"Thread {thread_id} started.")
    # lấy link ngẫu nhiên
    random_link = random.choice(linklist)
    print(random_link)
    open_new_window(random_link)
    print(f"Thread {thread_id} completed.")
    

def watch_time_cr(url):
    #Tính thời gian xem video 25-99% thời lượng
    yt=YouTube(url)
    video_length = yt.length
    watch_time = (random.randint(25,99))*video_length//100
    return watch_time

# #close all chrome windows đã bật
# def close_all_chrome_windows():
#     chrome_processes = [proc for proc in psutil.process_iter() if proc.name() == "chrome.exe"]
    
#     for proc in chrome_processes:
#         try:
#             proc.kill()
#         except psutil.NoSuchProcess:
#             pass

# def close_session_chrome(session_id):
#     service_session = Service('path/to/chromedriver.exe')
#     service_session.stop_service()
#     options = webdriver.ChromeOptions()
#     options.add_argument(f'--remote-debugging-port={session_id}')
#     driver = webdriver.Chrome(service=service_session, options=options)
#     driver.quit()

def thread_open():

    # Create an initial pool of threads
    threads = []

    for i in range (number_of_tab):
        thread = threading.Thread(target=open_main, args=(i,))
        thread.start()
        threads.append(thread)
        # time_label.config(text=f"thoi gian da chay {time_count}")
        # parent.update_idletasks

    # Main thread keeps running to maintain the thread pool
    while True:
        # Check if any thread has finished, and join them
        for thread in threads:
            if not thread.is_alive():
                thread.join()
                threads.remove(thread)
                print("Thread joined.")

        # Create new threads to maintain the pool size
        while len(threads) < number_of_tab:
            thread = threading.Thread(target=open_main, args=(i,))
            thread.start()
            threads.append(thread)
            print("New thread created.")
        
if __name__ == "__main__":

    parent = Tk()
    parent.geometry('500x500')

    #Number of view
    # view = Label(parent, text = "Max time").place(x = 30, y = 50)
    # e1 = Entry(parent)
    # e1.place(x = 100, y = 50)

    #list of link
    link = Label(parent, text = "Link List").place(x = 30, y = 90)
    e2 = Entry(parent)
    e2.place(x = 100, y = 90)
    
    number_of_tab = Label(parent, text = "số tab").place(x = 30, y = 130)
    e4 = Entry(parent)
    e4.place(x = 100, y = 130)

    # def time_count_def():
    #     messagebox.showinfo("Pop-up", "Thời gian đã chạy là "+str(time_count))

    time_label = tk.Label(parent, text="Processing...")
    time_label.place(x = 100, y = 170)

    apply_button = ttk.Button(parent, text='Apply', command=apply_info).grid(row = 4, column = 0)
    run_button = ttk.Button(parent, text='run', command=thread_open).grid(row=4, column=1)
    #check_time_run = ttk.Button(parent, text='check time', command = time_count_def).grid(row =4 , column = 2)
    #kill_button = ttk.Button(parent, text='close all', command=close_all_chrome_windows).grid(row=4, column=2)

    parent.mainloop()
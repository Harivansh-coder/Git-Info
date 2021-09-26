"""
Following script uses git REST api to get desired data.
This script return all repository information currently(repositry name, clone link, private or not, watch_count)
for a user whose userName entered. 
"""
import requests
from pprint import pprint 
from Repo import *
from tkinter import Button, Entry, Label, Listbox, Tk

master = Tk()
master.title("Git Info")
master.geometry("300x150") 


# The GUI
label = Label(master,text="User Name: ").grid(row=0, column=0)
user_name = Entry(master, width = 25,borderwidth = 5)
user_name.grid(row=0, column=1,columnspan = 4,padx = 10,pady = 5)


# get repo function
def get_repo():
    
    user_name_text = user_name.get()


    url_repos = "https://api.github.com/users/"+user_name_text+"/repos"
    r = requests.get(url = url_repos)

    # getting the data
    data = r.json()

    # creating repo object and printing the data
    repo = Repo()
    repo.print_repo(data)

Button(master, text ="Go",height = 3,width = 10,command = get_repo).grid(row=2, column=1,padx = 10,pady = 5)



master.mainloop()






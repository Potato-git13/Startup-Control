import os
import webbrowser
from tkinter import *

# Declaring links and paths to programs/sites frequently used
reddit = "https://www.reddit.com"
youtube = "https://www.youtube.com"
stack_overflow = "https://stackoverflow.com"
Ps = "your Photoshop path"
Mc = "Your Minecraft path"
toggl_programming_comics = "https://toggl.com/blog/tag/comics"
discord = "Your Discord path"
VS_code = "Your Vs Code path"


def opening(site_program):
    # sites
    try:
        if site_program == reddit:
            webbrowser.open(reddit)
        elif site_program == youtube:
            webbrowser.open(youtube)
        elif site_program == stack_overflow:
            webbrowser.open(stack_overflow)
        elif site_program == toggl_programming_comics:
            webbrowser.open(toggl_programming_comics)
    except:
        if site_program == reddit:
            webbrowser.open_new(reddit)
        elif site_program == youtube:
            webbrowser.open_new(youtube)
        elif site_program == stack_overflow:
            webbrowser.open_new(stack_overflow)
        elif site_program == toggl_programming_comics:
            webbrowser.open_new(toggl_programming_comics)

    # programs
    if site_program == Ps:
        os.startfile(Ps)
    elif site_program == Mc:
        os.startfile(Mc)
    elif site_program == discord:
        os.startfile(discord)
    elif site_program == VS_code:
        os.startfile(VS_code)


def gui():
    # configuring the tkinter window
    window = Tk()
    window.title("Startup Control")
    window.config(background="light blue")
    window.iconbitmap("StartupControlIcon.ico")

    title_window = Label(text="Pick a website or a program you want to open", bg="light blue")
    title_window.grid(row=0, column=0)

    # creating buttons
    reddit_button = Button(text="Reddit", command=lambda: opening(reddit), width=34, bg="orange")
    reddit_button.grid(row=1, column=0)
    yt_button = Button(text="Youtube", command=lambda: opening(youtube), width=34, bg="red")
    yt_button.grid(row=2, column=0)
    stck_overflow_button = Button(text="Stack Overflow", command=lambda: opening(stack_overflow), width=34,
                                  bg="yellow")
    tpc_button = Button(text="Toggl Programming Comics", command=lambda: opening(toggl_programming_comics), width=34,
                        bg="violet")
    tpc_button.grid(row=3, column=0)
    stck_overflow_button.grid(row=4, column=0)
    ps_button = Button(text="Photoshop CC 2019", command=lambda: opening(Ps), width=34, bg="blue")
    ps_button.grid(row=5, column=0)
    mc_button = Button(text="Minecraft", command=lambda: opening(Mc), width=34, bg="lime")
    mc_button.grid(row=6, column=0)
    discord_button = Button(text="Discord", command=lambda: opening(discord), width=34, bg="light blue")
    discord_button.grid(row=7, column=0)
    vs_code_button = Button(text="Visual Studio Code", command=lambda: opening(VS_code), width=34, bg="blue")
    vs_code_button.grid(row=8, column=0)

    mainloop()


if __name__ == "__main__":
    gui()

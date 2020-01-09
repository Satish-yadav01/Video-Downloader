#It is a simple youtube video downloader
from tkinter import *
from pytube import *
root=Tk()
root.title("Satish-VideoDownloader")
root.geometry("300x300")
#---------------------------------------------
def DownlaodVid():
    global E1
    string=E1.get()
    yt=YouTube(str(string))
    videos=yt.streams.all()
    s=1
    for v in videos:
        print(str(s)+'.'+str(v))
        s+=1
    n=int(input("Enter your choice:"))
    vid=videos[n-1]
    destination=str(input("Enter your destination:"))
    vid.download(destination)
    print(yt.title+"\n has been downloaded")
    
frame=Frame(root)
frame.pack()
l1=Label(root,text="Enter your link",fg="blue",bd="2")
l1.pack(anchor="nw")
E1=Entry(root,width="100",bd="5",relief="sunken")
E1.pack(anchor="nw")
B1=Button(root,text="Download",fg="red",command=DownlaodVid)
B1.pack(anchor="nw")
root.mainloop()

#----------------------------------------------#
# Assignment 3                                 #
# Group 3 | Section 1                          #
# - Bilkis Musa A20EC0233                      #
# - Fatin Aimi Ayuni Binti Affindy A20EC0190   #
#----------------------------------------------#

import cv2 as cv
import tkinter as tk
import numpy as np
from matplotlib import pyplot as plt
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk

#User interface
root = tk.Tk()

root.geometry("1000x700")
root.title("Image Thresholding")
root.resizable(0, 0)

root.columnconfigure(1, weight=5)
root.columnconfigure(2, weight=5)

title = tk.Label(root, text="Image Thresholding", bg= '#F5AFAF', width=50,font=('Helvetica', 20))
title.grid(row=1, column=1, columnspan=2, sticky=S)

text1 = tk.Label(root, text="\n Input: written text, hand-written signature, or picture", font=('Helvetica', 14))
text1.grid(row=2, column=1, columnspan=2)

text2 = tk.Label(root, text="\n Upload the image to see the result\n", font=('Helvetica', 14))
text2.grid(row=3, column=1, columnspan=2)

#button to upload black and white image
button1 = tk.Button(root, text="Upload Black&White Image", font=('Helvetica', 12), height = 2, width=25, border = 7, activeforeground = "black", activebackground = '#F5B7B1', background='#A9CCE3', command=lambda:bw())
button1.grid(row=5, column=1)

#button to upload colored image
button2 = tk.Button(root, text="Upload Colored Image", font=('Helvetica', 12), height = 2, width=25, border = 7, activeforeground = "black", activebackground = '#F5B7B1', background='#A9CCE3', command=lambda:color())
button2.grid(row=5, column=2)

text3 = tk.Label(root, text="\n Median Blur Kernel Size", font=('Helvetica', 12))
text3.grid(row=6, column=1)

text4 = tk.Label(root, text="\n Threshold Value", font=('Helvetica', 12))
text4.grid(row=6, column=2)

#image threshold of black and white image
def bw():
    global median, img, imgin, file, bInp, bOut
    file =  filedialog.askopenfilename(initialdir = "./",title = "File", type =  (('Jpg Files', '*.jpg')))
    print (file)
    img = cv.imread(file,0)
    imgin = Image.open(file)

    median = cv.medianBlur(img, 7)
    threshold = cv.adaptiveThreshold(median,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,\
                cv.THRESH_BINARY,11,2)

    #to resize image
    (widthinp, heightinp) = imgin.size

    if widthinp > 500:
        newinpw = int(widthinp/3)
        newinph = int(heightinp/3)

    else:
        newinpw = int(widthinp)
        newinph = int(heightinp)

    inresized = imgin.resize((newinpw, newinph))

    inp = ImageTk.PhotoImage(image=inresized)
    bInp = tk.Button(root,image=inp)
    bInp.grid(row=15, column=1)

    imgout = Image.fromarray(threshold)

    #to resize image
    (widthout, heightout) = imgout.size

    if widthinp > 500:
        newoutw = int(widthout/3)
        newouth = int(heightout/3)

    else:
        newoutw = int(widthout)
        newouth = int(heightout)

    outresized = imgout.resize((newoutw, newouth))

    imagetk = ImageTk.PhotoImage(image=outresized)
    bOut = tk.Button(root,image=imagetk)
    bOut.grid(row=15, column=2)

    save = tk.Button(root, text="Save", font=('Helvetica', 12), width= 15, activeforeground = "black", activebackground = '#FFECB3', background='#E1BEE7', command= lambda:imgout.save("images/output.jpg"))
    save.grid(row=25, column=2)

    root.mainloop()

#image threshold of colored image
def color():
    global threshold, img, imgin, file, bInp, bOut
    file =  filedialog.askopenfilename(initialdir = "./",title = "File", type =  (('Jpg Files', '*.jpg')))
    print (file)
    img = cv.imread(file)
    imgin = Image.open(file)

    img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    img = np.array(img)
    ret,threshold = cv.threshold(img,127,255,cv.THRESH_BINARY)

    #to resize image
    (widthinp, heightinp) = imgin.size

    if widthinp > 500:
        newinpw = int(widthinp/3)
        newinph = int(heightinp/3)

    else:
        newinpw = int(widthinp)
        newinph = int(heightinp)

    inresized = imgin.resize((newinpw, newinph))

    inp = ImageTk.PhotoImage(image=inresized)
    bInp = tk.Button(root,image=inp)
    bInp.grid(row=15, column=1)

    imgout = Image.fromarray(threshold)

    #to resize image
    (widthout, heightout) = imgout.size

    if widthinp > 500:
        newoutw = int(widthout/3)
        newouth = int(heightout/3)

    else:
        newoutw = int(widthout)
        newouth = int(heightout)

    outresized = imgout.resize((newoutw, newouth))

    imagetk = ImageTk.PhotoImage(image=outresized)
    bOut = tk.Button(root,image=imagetk)
    bOut.grid(row=15, column=2)
    
    save = tk.Button(root, text="Save", font=('Helvetica', 12), width= 15, activeforeground = "black", activebackground = '#FFECB3', background='#E1BEE7', command= lambda:imgout.save("images/output.jpg"))
    save.grid(row=25, column=2)

    root.mainloop() 

#to update output with inserted kernel size
def updateblur():
    value = bvalue.get(1.0, "end-1c")
    kernel = int(value)

    if (kernel%2)==0:
        kernel = kernel+1

    median = cv.medianBlur(img, kernel)
    threshold = cv.adaptiveThreshold(median,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,\
                cv.THRESH_BINARY,11,2)

    #to resize image
    (widthinp, heightinp) = imgin.size

    if widthinp > 500:
        newinpw = int(widthinp/3)
        newinph = int(heightinp/3)

    else:
        newinpw = int(widthinp)
        newinph = int(heightinp)

    inresized = imgin.resize((newinpw, newinph))

    inp = ImageTk.PhotoImage(image=inresized)
    bInp = tk.Button(root,image=inp)
    bInp.grid(row=15, column=1)

    imgout = Image.fromarray(threshold)

    #to resize image
    (widthout, heightout) = imgout.size

    if widthinp > 500:
        newoutw = int(widthout/3)
        newouth = int(heightout/3)

    else:
        newoutw = int(widthout)
        newouth = int(heightout)

    outresized = imgout.resize((newoutw, newouth))

    imagetk = ImageTk.PhotoImage(image=outresized)
    bOut = tk.Button(root,image=imagetk)
    bOut.grid(row=15, column=2)

    save = tk.Button(root, text="Save", font=('Helvetica', 12), width= 15, activeforeground = "black", activebackground = '#FFECB3', background='#E1BEE7', command= lambda:imgout.save("images/output.jpg"))
    save.grid(row=25, column=2)

    root.mainloop()

#to update output with inserted threshold value
def updatethres():
    value = tvalue.get(1.0, "end-1c")
    thres = int(value)

    ret,threshold = cv.threshold(img,thres,255,cv.THRESH_BINARY)
    
    #to resize image
    (widthinp, heightinp) = imgin.size

    if widthinp > 500:
        newinpw = int(widthinp/3)
        newinph = int(heightinp/3)

    else:
        newinpw = int(widthinp)
        newinph = int(heightinp)

    inresized = imgin.resize((newinpw, newinph))

    inp = ImageTk.PhotoImage(image=inresized)
    bInp = tk.Button(root,image=inp)
    bInp.grid(row=15, column=1)

    imgout = Image.fromarray(threshold)

    #to resize image
    (widthout, heightout) = imgout.size

    if widthinp > 500:
        newoutw = int(widthout/3)
        newouth = int(heightout/3)

    else:
        newoutw = int(widthout)
        newouth = int(heightout)

    outresized = imgout.resize((newoutw, newouth))

    imagetk = ImageTk.PhotoImage(image=outresized)
    bOut = tk.Button(root,image=imagetk)
    bOut.grid(row=15, column=2)

    save = tk.Button(root, text="Save", font=('Helvetica', 12), width= 15, activeforeground = "black", activebackground = '#FFECB3', background='#E1BEE7', command= lambda:imgout.save("images/output.jpg"))
    save.grid(row=25, column=2)

    root.mainloop() 

#textbox to input new kernel size for median blur
bvalue = tk.Text(root, width=20, height=1, bg="#FFECB3", pady=10, font=('Helvetica', 14))
bvalue.insert(INSERT, '7')
bvalue.grid(row=7, column=1)

#textbox to input new threshold value for threshold function
tvalue = tk.Text(root, width=20, height=1, bg="#FFECB3", pady=10, font=('Helvetica', 14))
tvalue.insert(INSERT, '127')
tvalue.grid(row=7, column=2)

#to save new kernel size for median blur
saveb = tk.Button(root, text="Save Kernel Size", font=('Helvetica', 10), activeforeground = "black", activebackground = '#FFECB3', bg= '#F5AFAF', height= 1, width=20, border=3,  command=lambda:updateblur())
saveb.grid(row=8, column=1)

#to save new threshold value
savet = tk.Button(root, text="Save Threshold Value", font=('Helvetica', 10), activeforeground = "black", activebackground = '#FFECB3', bg= '#F5AFAF', height= 1, width=20, border=3, command=lambda:updatethres())
savet.grid(row=8, column=2)

root.mainloop()
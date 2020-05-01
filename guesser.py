#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter

#97 is 'a' 122 is 'z'

class Guesser:
    
    def __init__(self):
        self.mainWindow =tkinter.Tk()
        self.mainWindow.title("Computer is so fast")
        self.mainWindow.geometry("1400x180")
        self.topFrame = tkinter.Frame(self.mainWindow)

        self.label1 = tkinter.Label(self.topFrame, text = "Enter the 5-letter password: ")
        self.label1.config(font=("Courier", 44))
        self.label1.pack(side = "left")
        
        self.inputEntry = tkinter.Entry(self.topFrame, width = 5)
        self.inputEntry.config(font=("Courier", 44))
        self.inputEntry.pack(side = "right")
        self.topFrame.pack()
    
        self.bottomFrame = tkinter.Frame(self.mainWindow)
        
        self.message = tkinter.StringVar() #the string that appears in the label
        self.messageLabel = tkinter.Label(self.bottomFrame, textvariable=self.message)
        
        self.messageLabel.config(font=("Courier", 44))
        self.messageLabel.pack()
        self.bottomFrame.pack(side = "bottom")
        
        self.mainWindow.bind('<Return>', self.guess)
        self.inputEntry.focus()

        tkinter.mainloop()


        
    def clearEntry(self):
        self.inputEntry.delete(0, tkinter.END)
        self.inputEntry.focus
        self.message.set("Error: enter 5 letters, no numbers")
        
    def validate(self):
        try:
             userInput = self.inputEntry.get()
             userInput = str.lower(userInput)

             if (len(userInput) != 5):
                 self.clearEntry()
                 return -1
             elif (not userInput.isalpha()):
                 self.clearEntry()
                 return -1
             else:
                 return userInput
        except:
            return -1


    def guess(self, event): #event needs to be here to catch the key <Return> event
        secretWord = self.validate()
        if (secretWord == -1):
            self.clearEntry()
            return -1
        result = "thinking..."
        self.message.set(result)
        count = 0
        guessedWord = "";
        for first in range(97,123):
            guessedWord += chr(first)
            for second in range(97,123):
                guessedWord += chr(second)
                for third in range(97,123):
                    guessedWord += chr(third)
                    for fourth in range(97,123):
                        guessedWord += chr(fourth)
                        for fifth in range(97,123):
                            guessedWord += chr(fifth)
                            count+=1
                            if guessedWord == secretWord:
                                self.clearEntry()
                                count = format(count, ",d")
                                result = "Guessed " +guessedWord+ " in " + count + " attempts."
                                self.message.set(result)
                                return
                            else:
                                guessedWord = guessedWord[0:4]
                        guessedWord = guessedWord[0:3] 
                    guessedWord = guessedWord[0:2]
                guessedWord = guessedWord[0:1]
            guessedWord = "" 
        

from tkinter import *

textFont = ('Arial', 12)
scoreFont = ('Trebuchet MS', 32)
buttonFont = ('Segou UI Variable', 10)

green = '#99BC85'

game = True

def openMenu(score):
    root = Tk()

    root.geometry(f'300x175+480+250')
    root.title('menu')

    root.resizable(False, False)


    def stopGame():

        global game

        game = False
        root.destroy()


    resultLabel = Label(root, text=f'your score is...', font=textFont)
    resultLabel.pack(padx=10, pady=10)

    scoreLabel = Label(root, text=f'{score}', font=scoreFont, foreground=green)
    scoreLabel.pack(padx=10, pady=10)

    continueButton = Button(root, text='Restart', font=buttonFont, command=root.destroy)
    continueButton.pack(side=LEFT, padx= 30)

    stopButton = Button(root, text='Quit', font=buttonFont, command=stopGame)
    stopButton.pack(side=RIGHT, padx= 30)

    root.mainloop()

    if game:
        return True
    else:
        return False


from tkinter import *
import boardgameidea
import data


def generate():
    resMechanics.configure(state='normal')
    resMechanics.delete('1.0', END)
    mechanics = boardgameidea.draw_mechanics(int(mechanicsNb.get()))
    for i in range(len(mechanics)):
        resMechanics.insert(END, mechanics[i] + " -> " + data.mechanics[mechanics[i]] + "\n")
    resMechanics.configure(state='disabled')
    resCategory.set("Category : " + boardgameidea.draw_category())


if __name__ == "__main__":
    window = Tk()
    window.title("BoardGameIdea")

    frameMechEntry = Frame()
    frameResCategory = Frame()

    Label(frameMechEntry, text='Mechanics number ').pack(side=LEFT, padx=5, pady=5)

    mechanicsNb = StringVar()
    mechanicsNb.set(3)
    box = Spinbox(frameMechEntry, from_=1, to=10, increment=1, textvariable=mechanicsNb, width=5)
    box.pack(side=LEFT, padx=30, pady=10)
    Button(frameMechEntry, text='Generate', command=generate).pack(side=LEFT, padx=5, pady=5)

    resCategory = StringVar()
    resCategory.set("Category : ")
    Label(frameResCategory, textvariable=resCategory).pack(padx=30, pady=10)

    resMechanics = Text(frameResCategory, state='disabled')
    resMechanics.pack()

    frameMechEntry.pack()
    frameResCategory.pack()

    window.mainloop()

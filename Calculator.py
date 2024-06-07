import tkinter as tk

class Calculator: 
    
    
    def __init__(self):
        self.buttons = []
        self.currentNumber = 0
        self.__pastNumber = 0
        self.opperation = 0
        self.pastOpperation = 0
        self.buttonColor = ""
        self.newNum = True
        
        self.root = tk.Tk()
        self.root.title("Calculator")
        self.root.geometry("450x650")
        self.__makeLabel()
        self.__makeButtons()
        self.root.mainloop()
        
    def __makeLabel(self):
        self.label = tk.Label(self.root, text= self.currentNumber, font = ("Arial", 24))
        self.label.place(x=10,y=10)
    def __calculate(self):
        if self.pastOpperation == 1:
            self.currentNumber += self.__pastNumber
        if self.pastOpperation == 2:
            self.currentNumber = self.__pastNumber - self.currentNumber
        if self.pastOpperation == 3:
            self.currentNumber *= self.__pastNumber
        if self.pastOpperation == 4:
            self.currentNumber = self.__pastNumber/self.currentNumber
        self.pastOpperation = self.opperation      
    def onButtonClick(self, i):
        print(i)
        if i < 10:
            if self.newNum:
                self.currentNumber = 0
                self.__pastNumber = 0
                self.pastOpperation = 0
                self.opperation = 0
            if self.opperation != 0:
                self.__calculate()
                self.__pastNumber = self.currentNumber
                self.pastOpperation = self.opperation
                self.currentNumber = i
            else:
                self.currentNumber *= 10
                self.currentNumber += i
                self.newNum = False
            self.label.config(text=self.currentNumber)
        elif i == 16:
            self.currentNumber = int(self.currentNumber/10)
            self.label.config(text=self.currentNumber)
        elif i == 14:
            if self.currentNumber == 0:
                self.__pastNumber = 0
            self.currentNumber = 0
            self.label.config(text=self.currentNumber)
        elif i == 15:
            self.newNum = False
            self.currentNumber *=-1
            self.label.config(text=self.currentNumber)
        elif i < 14:
            self.newNum = False
            if self.opperation == (i%10)+1:
                self.buttons[i].config(bg = self.buttonColor)
                self.opperation = 0
            else:
                self.buttons[i].config(bg = "red")
                self.opperation = (i%10)+1
                self.__pastNumber = self.currentNumber
        elif i == 17:
            self.buttons[self.opperation+9].config(bg = self.buttonColor)
            self.__calculate()
            self.label.config(text=self.currentNumber)
            self.pastOpperation = 0
            self.opperation = 0
            self.newNum = True


    def __makeButtons(self):
        textArr = ["+","-","x", "/", "C","+/-","del"]
        button = tk.Button(self.root, text = "0", command = lambda: self.onButtonClick(0), width=10, height=5, font=("Arial", 12))
        self.buttonColor = button.cget("background")
        buttonX =120
        buttonY = 505
        button.place(x = buttonX, y = buttonY)
        self.buttons.append(button)
        buttonX = 220
        buttonY = 400
        for i in range(1,10):
            buttonText = str(i)
            button = tk.Button(self.root, text = buttonText, command = lambda i=i: self.onButtonClick(i), width=10, height=5, font=("Arial", 12))
            button.place(x = buttonX, y = buttonY)
            buttonX -= 100
            if(i%3 == 0):
                buttonY -= 105
                buttonX = 220
            self.buttons.append(button)
        buttonX = 320
        buttonY = 400
        counter = 0
        for i in range(10,14):
            buttonText = textArr[counter]
            button = tk.Button(self.root, text = buttonText, command = lambda i=i: self.onButtonClick(i), width=10, height=5, font=("Arial", 12))
            button.place(x = buttonX, y = buttonY)
            buttonY -= 105
            counter+=1
            self.buttons.append(button)
        buttonX = 20
        buttonY = 85
        for i in range(14,17):
            buttonText = textArr[counter]
            button = tk.Button(self.root, text = buttonText, command = lambda i=i: self.onButtonClick(i), width=10, height=5, font=("Arial", 12))
            button.place(x = buttonX, y = buttonY)
            buttonX += 100
            counter+=1
            self.buttons.append(button)
        button = tk.Button(self.root, text = "=", command = lambda: self.onButtonClick(17), width=10, height=5, font=("Arial", 12))
        button.place(x= 320, y = 505)
        self.buttons.append(button)
        
def main():
   calc = Calculator()
    
if __name__ == "__main__" :
    main()

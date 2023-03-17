import tkinter as tk
from tkinter import *
import webbrowser

class ParentWindow(Frame):
    def __init__(self,master):
        Frame.__init__(self,master)
        self.master.title("Web Page Generator")
        
        self.btn = Button(self.master, text="Default HTML Page", width=30, height=2,font=('Helvetica',10,'normal'), command=self.defaultHTML)
        self.btn.grid(row=0,column=0,padx=10,pady=10)
        # Creating another button to launch a web page with custom text
        self.btn = Button(self.master, text="Custom Text Page", width=30, height=2,font=('Helvetica',10,'normal'), command=self.customHTML)
        # Using the grid manager to place the custom text button in row 1, column 0
        self.btn.grid(row=1,column=0,padx=10,pady=10)

        # Assigning a variable to the Entry widget named 'texty' to be able to retrieve the value using the 'get()' method
        texty =tk.StringVar(root)

        # Creating the lable 'Input Custom Text'
        self.name_label = tk.Label(root, text = 'Input Custom Text', font=('Helvetica',10, 'normal'))
        # Using the grid manager to place the lable to the left of the Entry field, in row 2, column 0
        self.name_label.grid(row=2,column=0,padx=(20,20),pady=(20,20))
        # Creating the text Entry field where the user can enter custom text to be displayed between the body tags of the html document
        self.custom_entry = tk.Entry(root, textvariable =texty,width=75,font=('Helvetica',10,'normal'))
        # Using the grid manager to place the Entry filed in row 2, column 1
        self.custom_entry.grid(row=2,column=1,columnspan=2,padx=10,pady=10)
    
    # This function will create the default html page that will reflect the same text within the body
    def defaultHTML(self):
        htmlText = "Stay tuned for our amazing summer sale!"
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")

    # This function will create the custom html page with the user's chosen verbiage in the body of the page
    def customHTML(self):
        # This is retrieving the user's text from the the Entry field 
        cus_text=self.custom_entry.get()
        # This ensures that the 

        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + cus_text + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")




if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
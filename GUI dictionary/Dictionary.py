import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
import wikipedia

class MainPage(QDialog):
    def __init__(self):
        super(MainPage, self).__init__()
        loadUi("amarna.ui",self)
        self.button_1.clicked.connect(self.gotosearch)
        self.button_2.clicked.connect(self.gotodisplay)

    def gotosearch(self):
        search= SearchPage() 
        widget.insertWidget(2,search)
        widget.setCurrentIndex(2)

    def gotodisplay(self):
        display = DisplayPage()
        widget.insertWidget(2,display)
        widget.setCurrentIndex(2)
        
class SearchPage(QDialog):
    def __init__(self):
        super(SearchPage,self).__init__()
        loadUi("search page.ui",self)
        self.pushButton.clicked.connect(self.searchvalue)
        self.pushButton_2.clicked.connect(self.savevalue)

    def searchvalue(self):
        global topic
        global values
        topic = self.lineEdit.text()
        try:
            values = wikipedia.summary(topic,sentences=5)
            if len(values)>0:
                self.value.setText(values)
                print("Successfully searched")
            if True:
                self.label_3.setText("Do you want to save this data?")

        except:
            print("fault")
                
    def savevalue(self):
        if  len(values) > 0:
            F=open("D:\\12th File handle\\Information.txt ","a")
            F.write(topic+"\n")
            F.write(values+"\n")
            F.close()
            print("Data saved successfully")
            self.data.setText("Data saved successfully")

class DisplayPage(QDialog):
    def __init__(self):
        super(DisplayPage,self).__init__()
        loadUi("display.ui",self)
        if True:
            self.loaddata()

    def loaddata(self):
        F=open("D:\\12th File handle\\Information.txt ","r")
        value= F.read()
        F.close()
        if True:
            self.label.setText(value)
        print("Value printed successfully")            

# main
app = QApplication(sys.argv)
mainpage = MainPage()

widget = QtWidgets.QStackedWidget()
widget.addWidget(mainpage)
widget.setFixedHeight(750)
widget.setFixedWidth(1390)
widget.show()

try:
    sys.exit(app.exec_())
except:
    print("Exiting..")    

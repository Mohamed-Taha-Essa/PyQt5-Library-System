#
import os

import setuptools
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox, QApplication, QFileDialog
import sys

class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        uic.loadUi('main.ui', self)

#######################################################################
    def Handel_Ui(self):
        pass

    def DB_Connect(self):
        pass

    def Handel_Button(self):
        pass

    def Handel_Login(self):
        pass

    def Handel_Reset_Password(self):
        pass

    def Handel_To_Day_Work(self):
        pass
    ###################################################
    def Show_All_books(self):
        pass
    def Add_New_book(self):
        pass
    def Edit_book(self):
        pass
    def Delete_book(self):
        pass
#################################################################
 ###################################################
    def Show_All_Clients(self):
        #Show_All_Clients
        pass
    def Add_New_Client(self):
        #Add_New_Client
        pass
    def Edit_Client(self):
        #Edit_Client
        pass
    def Delete_Client(self):
        #Delete_Client
        pass
    #################################################################
    ##History
    def Show_History(self):
        #show all history to the admin
        pass

    #################################################################
    ##Books Report

    def All_Books_Report(self):
        #All_Books_Report
        pass
    def Books_Filter_Report(self):
        #Books_Filter_Report
        pass
    def Book_Export_Report(self):
        #Book_Export_Report
        pass
        #################################################################
        ##Books Report

    def All_Client_Report(self):
        # All_Client_Report
        pass

    def Client_Filter_Report(self):
        # show report for filtered clients
        pass

    def Client_Export_Report(self):
        # Clients_Export to excel file
        pass
    #################################################################
    ##Monthly Report

    def Monthly_Report(self):
        # show one month report
        pass

    def Monthly_Report_Export(self):
        # Monthly_Export to excel file
        pass

    #################################################################
    ##Settings
    def Add_Branche(self):
        # Add new branche
        pass
    def Add_Author(self):
        # Add new author
        pass
    def Add_Publisher(self):
        # Add new publisher
        pass
    def Add_Category(self):
        #Add new Category
        pass
        #################################################################
        ##Emplyee
    def Add_Employee(self):
        #Add new Employee
        pass
    def Edit_Employee_Data(self):
        #Edit_Employee_Data
        pass

    #################################################################
    ##Add Employee permetion
    def Add_Employee_Permetion(self):
        #add permession to any employee
        pass

    def Admin_Report(self):
        #send report to the admin
        pass

def main():
    app =QApplication(sys.argv)
    window = Main()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()

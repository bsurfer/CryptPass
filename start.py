#!/usr/bin/python

import os
import getpass
from Shadow import *


class Password():
    def __init__(self, passwd):
        self.data = Shadow(passwd)

    def list(self):
        info = self.data.getInfo()
        for row in info:
            #print row['id'] ,row['name'],row['user'],row['password']
            print row['name']

    def imp(self):
        path = raw_input("Enter the path to database (/home/xpto/chrome_db.sql)> ")
        self.data.importDb(path)
        print 'DB imported with success!'

    def ins(self):
        name = raw_input("Enter the site or name> ")
        user = raw_input("Enter the username> ")
        passwd = getpass.getpass("Enter the password> ")
        passwd1 = getpass.getpass("ReEnter the password> ")

        if passwd == passwd1:
            get = self.data.addInfo(name, user, passwd)
            print get
            print '___________________________________'
            print 'Insert with success'
            print '___________________________________'
        else:
            print '___________________________________'
            print 'Password miss match \n'
            print '___________________________________'
            self.ins()

    def search(self):
        name = raw_input("Enter the name to search> ")
        get = self.data.searchInfo(name)
        print "id \t site \t\t\t\t\t\t\t\t\t user"
        for row in get:
            #print row['id'], row['name'], row['user'], row['password']
            print "%i \t %s \t\t\t\t\t\t\t\t\t %s " % (row['id'], row['name'], row['user'])
            #print row['name']

    def options(self):
            print '___________________________________'
            print '1 - Import Chrome database'
            print '2 - List all information'
            print '3 - Insert new information'
            print '4 - Search information'
            print '5 - Exit'
            print '___________________________________'

    def Menu(self):
            os.system('clear')
            while True:
                self.options()
                value = raw_input("Make a selection> ")
                if '1' in value:
                    self.imp()
                    #self.runSetMenu()
                    #os.system('clear')
                    os.ch
                elif '2' in value:
                    self.list()
                    #os.system('clear')
                elif '3' in value:
                    self.ins()
                    #self.deleteSetMenu()
                    #os.system('clear')
                elif '4' in value:
                    #self.createSetMenu()
                    self.search()
                    #os.system('clear')
                elif '5' in value:
                    print 'Good-bye'
                    quit()
                else:
                    os.system('clear')
                    print 'Invalid menu choice.'

    def run(self):
        print 'Initializing'
        self.Menu()

#___________________________

if __name__ == "__main__":
    os.system('clear')
    passwd = getpass.getpass("Enter the password to desencrypt the database> ")
    #start the session
    f = Password(passwd)
    f.run()

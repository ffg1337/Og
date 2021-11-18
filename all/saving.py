
from main import *

class Saving(MenuScreen):
    global tmp
    global saves
    bool = False
    def save(self,saveGlobal,saveNum,saveEvent,saveMark):
        try:
            saves = open("files/saves.txt", "a", encoding='utf-8')
            saves.writelines(saveGlobal+saveNum+saveEvent+saveMark+"\n")
            #test data save
            saves = open("files/saves.txt", "r")
            print(saves.read())
            saves.close()
        except IOError:
            print("No file saves or new game start")

    def rsave(self,bool):
        if bool:
            try:
                saves = open("files/saves.txt", "w")
                saves.writelines("#Global #Numbers #Events #Marks "+"\n"+"#1 0 0 0"+"\n")
            except IOError :
                print("No file saves")

    def continuesave(self):
        tmpa = '0'
        try:
            saves = open("files/saves.txt", "r", encoding='utf-8')
            for savef in saves :
                open("files/saves.txt", "r")
                lastsaves = savef.split()
                for s in lastsaves:
                    if s == '#1':
                        s = lastsaves[1]
                        tmpa = s
            saves.close()
            tmp = tmpa
            print(tmp)
        except IOError : print("No file saves or new game start")
        return tmp




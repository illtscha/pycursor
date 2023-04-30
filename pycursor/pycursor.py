import winreg as wrg
import Levenshtein
from os import listdir
from os.path import isfile, join
import os
import tkinter
import tkinter.filedialog
import shutil


from itertools import tee, islice, chain

def previous_and_next(some_iterable):
    prevs, items, nexts = tee(some_iterable, 3)
    prevs = chain([None], prevs)
    nexts = chain(islice(nexts, 1, None), [None])
    return zip(prevs, items, nexts)


class pyCursor:
    def __init__(self, folder, name):
        self.location = key = wrg.OpenKey(wrg.HKEY_CURRENT_USER, r"Control Panel\Cursors\Schemes", 0, wrg.KEY_ALL_ACCESS)
        self.folder = folder
        self.name = name
        self.CRSCUR = {"UpArrow": "alternate", "Wait": "busy", "SizeNWSE": "diagonal1",
                      "SizeNESW": "diagonal2", "NWPen": "handwriting", "Help": "help",
                      "AppStarting": "working", "Arrow": "normal", "Crosshair": "precision",
                      "Hand": "link", "IBeam": "text", "No": "unavailable", "SizeAll": "move",
                      "SizeNS": "vertical", "SizeWE": "horizontal", "Pin": "location", "Person": "person"}

    def moveFolder(self):
        destination = r"C:\Windows\Cursors"
        source = self.folder
        if os.path.exists(destination):
            folder_name = os.path.basename(source)
            i = 0
            while os.path.exists(os.path.join(destination, folder_name, "")):
                i += 1
                folder_name = os.path.basename(source) + str(i)
            destination = os.path.join(destination, folder_name)
        # Ordner verschieben
        self.folder = shutil.copytree(source, destination)

    def matchFilesByCRS(self):
        self.cursors = {}
        popl = []
        for file in os.listdir(self.folder):
            if file.endswith(".crs"):
                with open(os.path.join(self.folder, file), "r") as f:
                    for previous, line, next in previous_and_next(f):
                        #print(previous, line, next)
                        wincur = self.CRSCUR
                        for key in wincur.keys():
                            if (f"[{key}]" in line):
                                self.cursors[wincur[key]] = str(os.path.join(self.folder, next.split("=")[1])).strip()
                                popl.append(key)

                        for key in popl:

                            try:
                                wincur.pop(key)
                            except:
                                pass
                        for key in wincur.keys():
                            self.cursors[wincur[key]] = ""
    def matchFilesByName(self):

        self.cursors = {}
        self.win_cursors = ["alternate", "handwriting", "precision", "link", "move", "diagonal1", "diagonal2", "horizontal", "vertical", "unavailable","text", "busy", "working", "help", "normal", "person", "location"]

        self.files = [join(self.folder, f) for f in
         listdir(self.folder) if
         isfile(join(self.folder, f))]
        ofiles = self.files
        for name in self.win_cursors:
            try:
                distances = [Levenshtein.distance((os.path.splitext(os.path.basename(word))[0]).split()[0], name) for word in ofiles]
                closest_match = self.files[distances.index(min(distances))]
                ofiles.pop(distances.index(min(distances)))
                self.cursors[name] = closest_match
            except:
                self.cursors[name] = ""
    def matchFiles(self, alternate="", handwriting="", precision="", link="", move="", diagonal1="", diagonal2="", horizontal="", vertical="", unavailable=" ", text="", busy="", working="", help="", normal="", person="", location=""):

        self.cursors = {}
        self.win_cursors = ["alternate", "handwriting", "precision", "link", "move", "diagonal1", "diagonal2", "horizontal", "vertical", "unavailable","text", "busy", "working", "help", "normal", "person", "location"]
        for name in self.win_cursors:
            self.cursors[name] = eval(name)
    def matchFilesByPath(self, alternate="", handwriting="", precision="", link="", move="", diagonal1="", diagonal2="", horizontal="", vertical="", unavailable=" ", text="", busy="", working="", help="", normal="", person="", location=""):


        self.cursors = {}
        win_cursors = ["alternate", "handwriting", "precision", "link", "move", "diagonal1", "diagonal2", "horizontal", "vertical", "unavailable","text", "busy", "working", "help", "normal", "person", "location"]
        for name in win_cursors:
            try:
                self.cursors[name] = tkinter.filedialog.askopenfilename(initialdir=self.folder, title="Select %s cursor",filetypes=(("cursor files", "*.cur;*.ani"), ("all files", "*.*")))
            except:
                self.cursors[name] = ""

    def writeReg(self):
        content = r"%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s"%(self.cursors["normal"],self.cursors["help"],self.cursors["working"], self.cursors["busy"],self.cursors["precision"],self.cursors["text"],self.cursors["handwriting"],self.cursors["unavailable"], self.cursors["vertical"],self.cursors["horizontal"], self.cursors["diagonal1"],self.cursors["diagonal2"], self.cursors["move"], self.cursors["alternate"], self.cursors["link"], self.cursors["location"], self.cursors["person"])
        wrg.SetValueEx(self.location, self.name, 0, wrg.REG_EXPAND_SZ, content.replace("C:\Windows","%SYSTEMROOT%").strip())
    def close(self):
        if self.location:
            wrg.CloseKey(self.location)

    def openMainCpl(self):
        os.system("control main.cpl")

    def createCRSByPath(self, alternate="", handwriting="", precision="", link="", move="", diagonal1="", diagonal2="", horizontal="", vertical="", unavailable=" ", text="", busy="", working="", help="", normal="", person="", location=""):
        self.matchFilesByPath(alternate, handwriting, precision, link, move, diagonal1, diagonal2, horizontal, vertical, unavailable, text, busy, working, help, normal, person, location)
        with open(join(self.folder, self.name + ".crs"), "w") as f:
            lines = []
            i = 0
            for key in self.CRSCUR.keys():
                #print(self.cursors.keys())
                if self.cursors[self.CRSCUR[key]] != "":
                    lines.append(f"[{key}]")
                    lines.append(f"Path={os.path.basename(self.cursors[self.CRSCUR[key]])}\n")
            for line in lines:
                f.write(line + "\n")
    def createCRSByName(self):
        self.matchFilesByName()
        with open(join(self.folder, self.name + ".crs"), "w") as f:
            lines = []
            i = 0
            for key in self.CRSCUR.keys():
                #print(self.cursors.keys())
                if self.cursors[self.CRSCUR[key]] != "":
                    lines.append(f"[{key}]")
                    lines.append(f"Path={os.path.basename(self.cursors[self.CRSCUR[key]])}\n")
            for line in lines:
                f.write(line + "\n")
    def createCRS(self, alternate="", handwriting="", precision="", link="", move="", diagonal1="", diagonal2="", horizontal="", vertical="", unavailable=" ", text="", busy="", working="", help="", normal="", person="", location=""):
        self.matchFiles(alternate, handwriting, precision, link, move, diagonal1, diagonal2, horizontal, vertical, unavailable, text, busy, working, help, normal, person, location)
        with open(join(self.folder, self.name + ".crs"), "w") as f:
            lines = []
            i = 0
            for key in self.CRSCUR.keys():
                #print(self.cursors.keys())
                if self.cursors[self.CRSCUR[key]] != "":
                    lines.append(f"[{key}]")
                    lines.append(f"Path={os.path.basename(self.cursors[self.CRSCUR[key]])}\n")
            for line in lines:
                f.write(line + "\n")

    def matchByCRS(self):
        self.moveFolder()
        self.matchFilesByCRS()
        self.writeReg()
        self.close()
    def matchByPath(self):
        self.moveFolder()
        self.matchFilesByPath()
        self.writeReg()
        self.close()
    def matchByFile(self, alternate="", handwriting="", precision="", link="", move="", diagonal1="", diagonal2="", horizontal="", vertical="", unavailable=" ", text="", busy="", working="", help="", normal="", person="", location=""):
        self.moveFolder()
        self.matchFiles(alternate, handwriting, precision, link, move, diagonal1, diagonal2, horizontal, vertical, unavailable, text, busy, working, help, normal, person, location)
        self.writeReg()
        self.close()
    def matchByName(self):
        self.moveFolder()
        self.matchFilesByName()
        self.writeReg()
        self.close()








import json
import cmd

KBASE_FILE = ""

class KnowledgeBase():
    def __init__(self):
        tagdict = {}
    def addDot(self, kdot):
        if kdot.tag in self.tagdict:
            self.tagdict[tag].append({"priority": kdot.prio, "content": kdot.content}
        else:
            self.tagdict[tag] = [{"priority": kdot.prio, "content": kdot.content}]
    def saveBase(self):
        with open(KBASE_FILE, "w") as outfile:
            json.dump(self.tagdict, outfile, indent=4)
    
    def loadBase(self):
        with open(KBASE_FILE) as infile:
            self.tagdict = json.load(infile)
            
    def show_in_tag(self, tag):
        for i, kdot in enumerate(self.tagdict[tag]):
            print("%d: %s...", i+1, kdot[content][:20])
        
        
class KDot():
    def __init__(self, tag="general", content="", prio=4):
        self.tag = tag
        self.contentent = content
        self.prio = prio
        
    
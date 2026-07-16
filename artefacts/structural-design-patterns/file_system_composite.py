class FileSystemComponent:
    def show(self):
        pass
 
class File(FileSystemComponent):
    def __init__(self, name):
        self.name = name
    def show(self):
        print(self.name)
 
class Folder(FileSystemComponent):
    def __init__(self, name):
        self.name = name
        self.items = [] 
    def add(self, item):
        self.items.append(item) 
    def show(self):
        print(self.name) 
        for item in self.items:
            item.show()
 
folder = Folder("Documents")
folder.add(File("report.txt"))
folder.show()

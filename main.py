from tkinter import *
from tkinter import ttk
from tkinter.ttk import Checkbutton, Frame
from PIL import Image, ImageTk
from widgets import Checkbar, Table, Logs
from tkinter import messagebox as mb
from functions import Functions, SettingFunctions
import datetime
from ttkthemes import ThemedStyle

class Settings(Frame, SettingFunctions):
    def __init__(self, parent):
        Frame.__init__(self, parent)   
        self.parent = parent
        self.initUI()
        #self.function = SettingFunctions(id = 0)
        
    def initUI(self):
        self.parent.geometry("482x375")
        self.parent.title("Approvers tool - Settings")
        self.parent.resizable(False, False)
        self.parent["bg"] = "#f5f6f7"

        labelframe = ttk.LabelFrame(self.parent, text= "История изображений")
        history = Listbox(labelframe, width = 75, height = 10)
        scroll = ttk.Scrollbar(labelframe, command = history.yview) 
        history.config(yscrollcommand = scroll.set)
        
        labelid = ttk.Label(self.parent, text = "ID апрувера: ")
        self.id = StringVar()
        self.butid = ttk.Entry(self.parent, width = 16, textvariable = self.id)

        labeldisk = ttk.Label(self.parent, text = "Диск: ")

        self.values = []
        for i in range(65,91):
        	self.values.append(chr(i) + ":")

        self.listdisk = ttk.Combobox(self.parent, values = self.values)

        labelmax = ttk.Label(self.parent, text = "Макс. кол. изображений: ")
        self.max = StringVar()
        self.butmax = ttk.Entry(self.parent, width = 4, textvariable = self.max)

        checkdir = ttk.Button(self.parent, text = "Провека структуры", command = self.checkDirs)
    	
        butclearhistory = ttk.Button(self.parent, text = "Очистить историю")

        butsave = ttk.Button(self.parent, text = "Сохранить настройки", command = self.buttonSave)
        
        SettingFunctions.setSettingsInWidgets(self, id = self.id, listdisk = self.listdisk, max_images = self.max, logs = app.tx)
        #self.setSettings()

        butsave.place(x = 335, y = 327)
        butclearhistory.place(x = 347, y = 275)
        self.butmax.place(x = 153, y = 327)
        labelmax.place(x = 5, y = 330)
        self.listdisk.place(x = 44, y = 277)
        labeldisk.place(x = 5, y = 280)
        labelid.place(x = 5, y = 230)
        self.butid.place(x = 80, y = 227)
        scroll.pack(side = RIGHT, fill = Y)
        labelframe.place(x = 5, y = 5)
        history.pack()
        checkdir.place(x = 345, y = 224)
        
        self.pack()

    def back(self):
        self.parent.withdraw()
        #app.mainWindow()
    
    def checkDirs(self):
        list_id = app.get_id()
        SettingFunctions.checkdirs(self, list_id = list_id, logs = app.tx, mode = True)

    def buttonSave(self):
    	SettingFunctions.saveSettings(self, id = self.butid.get(), disk = self.listdisk.get(), max = self.butmax.get(), logs = app.tx)

    def setSettings(self):
    	self.id.set(42)

class App(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)   
        self.parent = parent
        self.function = Functions()
        self.initUI()
        
    def initUI(self):
        self.parent.geometry("1075x560")
        self.parent.title("Approvers tool")
        self.parent.resizable(False, False)
        self.parent["bg"] = "#f5f6f7"
        
        list_id = [] 
        for i in range(3,99):
            if i < 10:
                list_id.append("ID   " + str(i))
            else:    
                list_id.append("ID " + str(i))
        

        menubar = Canvas(self.parent, width = 170, height = 575, bg="#4d59a1", bd = 0, highlightthickness = 0) # Меню бар слева
        
        self.chbutton = Checkbar(self.parent, list_id) # Группа чек кнопок

        self.tx = Logs(self.parent) # Виджет для вывода логов

        self.table = Table(self.parent, headings=('ID', 'Сделано', 'Переделано', 'Жду ответа')) # Виджет таблици
        

        self.img_search = Image.open("img\\icon-search.png")
        img_search = ImageTk.PhotoImage(self.img_search)
        searchButton = Button(self.parent, image = img_search, relief = FLAT, command = self.search, bd = 0, highlightthickness = 0)
        lblsearch = Label(self.parent, text = "Поиск изображений", bg = "#4d59a1", fg = "white")

        self.img_get = Image.open("img\\icon-get.png")
        img_get = ImageTk.PhotoImage(self.img_get)
        getButton = Button(self.parent, image = img_get, relief = FLAT, command = self.get, bd = 0, highlightthickness = 0)
        lblget = Label(self.parent, text = "Загрузить изображения", bg = "#4d59a1", fg = "white")
        

        self.img_upload = Image.open("img\\icon-upload.png")
        img_upload = ImageTk.PhotoImage(self.img_upload)
        uploadButton = Button(self.parent, image = img_upload, relief = FLAT, command = self.function.upload_images, bd = 0, highlightthickness = 0)
        lblupload = Label(self.parent, text = "Выгрузить изображения", bg = "#4d59a1", fg = "white")

        self.img_setting = Image.open("img\\icon-setting.png")
        img_setting = ImageTk.PhotoImage(self.img_setting)
        settingButton = Button(self.parent, image = img_setting, relief = FLAT, command = self.settingsWindow, bd = 0, highlightthickness = 0)
        lblsetting = Label(self.parent, text = "Перейти в настройки", bg = "#4d59a1", fg = "white")
        
        allcheckbox = ttk.Button(self.parent, text = "Выбрать все ID", command = self.set)
        clearcheckbox = ttk.Button(self.parent, text = "Очистить все ID", command = self.clear)

        getButton.image = img_get
        searchButton.image = img_search
        uploadButton.image = img_upload
        settingButton.image = img_setting
        

        allcheckbox.place(x = 170, y = 175)
        clearcheckbox.place(x = 170, y = 213)
        searchButton.place(x = 45, y = 55)
        lblsearch.place(x = 15, y = 115)
        getButton.place(x = 45, y = 175)
        lblget.place(x = 15, y = 235)
        uploadButton.place(x = 45, y = 295)
        lblupload.place(x = 15, y = 355)
        settingButton.place(x = 45, y = 450)
        lblsetting.place(x = 15, y = 510)

        self.table.place(x = 720, y = 250)
        self.chbutton.place(x = 173, y = 20)
        menubar.place(x = -5, y = -5)
        self.tx.place(x=167, y = 250)

        self.pack()

    def get_id(self):
        list_ids = self.chbutton.state()
        list_id = []
        count_id = 1
        for i in range(1,3):
            list_ids.insert(0, 0)
        for i in list_ids:
            if i == 1:
                list_id.append("id" + str(count_id))
            count_id += 1
        if not list_id:
            mb.showerror("Ошибка", "Выберете хотя бы один id!")
            return []
        return list_id

    def search(self):
        search = self.function.search(self.get_id(), self.tx)
        self.table.add(search)


    def set(self):
        self.chbutton.set()

    def clear(self):
        self.chbutton.clear()

    def settingsWindow(self):
        setting = Toplevel(self.parent)
        app = Settings(setting)
        setting.mainloop()

    def get(self):
        self.function.get_images(self.get_id(), self.tx)



if __name__ == '__main__':
    root = Tk()
    app = App(root)
    style = ThemedStyle(app)
    style.set_theme("arc")
    root.mainloop()
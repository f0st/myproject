from tkinter import *
from tkinter.ttk import Checkbutton, Frame
from tkinter import ttk 
from PIL import Image, ImageTk
from tkinter import messagebox as mb
import shutil
import os
import json

# Все основные фуннкции в класе Functions
# Дописати функцію!(Смена директории)

class SettingFunctions():
	def __init__():
		self.id
		self.disk
		self.max_images

	def getSettings(self, logs):
		self.dir = os.getcwd()
		os.chdir(self.dir +  "\\" + "date")
		try:	
			with open('settings.json') as f:
				settingsjson = json.load(f)
				os.chdir(self.dir)
				return settingsjson

		except:
			logs.write("Не удалось загрузить настройки")
			os.chdir(self.dir)
			return False
		
	def saveSettings(self, id, disk, max, logs):
		self.disk = disk
		self.dir = os.getcwd()
		try:
			self.id = int(id)
			self.max_images = int(max)
		except:
			mb.showerror("Ошибка", "Введите коректные значение")
			return False

		settingsjson = {"id_approve": self.id, "disk": self.disk, "max_images": self.max_images}
		os.chdir(self.dir + "\\" + "date")
		try:
			with open('settings.json', 'w') as f:
				json.dump(settingsjson, f, sort_keys=True, indent=2)
			logs.write("Настройки успешно сохранены")
			os.chdir(self.dir)
		except:
			logs.write("Ошибка, настройки не сохранены")
		os.chdir(self.dir)

	def checkdirs(self, list_id, logs, mode):
		list_id_fc = []
		settings = self.getSettings(logs)
		list_dir = []
		path_app = ""

		for dir in os.listdir(str(settings["disk"]) + "\\id" + str(settings["id_approve"])):
			if "Проверяю" in dir:
				path_app = str(settings["disk"]) + "\\id" + str(settings["id_approve"]) + "\\" + str(dir)
				list_dir = os.listdir(path_app)

		logs.write("Проверка структуры папок апрувера")

		if not list_dir:
			for id in list_dir:
				list_id_fc.append(id)

		for id in list_id:
			if id in list_dir:
				continue
			else:
				list_id_fc.append(id)

		if not list_id_fc:
			if mode:
				mb.showinfo("Проверка структуры", "Структура папок в порядке")
			logs.write("Структура успешно проверена")
			return True

		answ = mb.askyesno(title="Проверка структуры", message="Добавить в структуру папок " + str(list_id_fc).replace("[", "").replace("]", "") + " ?")
		if answ:
			path = path_app
			for dir in list_id_fc:

				os.mkdir(path + "\\" + str(dir))
				os.mkdir(path + "\\" + str(dir) + "\\" + "Переделать")
				os.mkdir(path + "\\" + str(dir) + "\\" + "Перепроверить")
			logs.write("Добавленно в структуру: " + str(list_id_fc).replace("[", "").replace("]", ""))
			list_id_fc.clear()	
		return True

	def setSettingsInWidgets(self, id, listdisk, max_images, logs):
		try:
			settings = self.getSettings(logs)
			id.set(settings["id_approve"])
			listdisk.current(25)
			max_images.set(settings["max_images"])
		except:
			logs.write("Не удалось загузить настройки")

class Functions():

	def search(self, list_id, logs):
		self.list_search = []
		settings = SettingFunctions.getSettings(self, logs = logs)
		folders = ["Сделано", "Переделано", "Жду ответа"] # Папки для проверки
		count_file_c = 0	#
		count_file_p = 0	# Счетчики для найденных файлов
		count_file_z = 0	#

		logs.write("==========Начало поиска изображений на сервере==========", mode = False)
		for id in list_id:
			list_search = []
			try:
				logs.write("Проверка папки " + str(id))
				for dir in os.listdir(settings["disk"] + "\\" + str(id)):
					for folder in folders:
						if folder in dir:
							for i in list(os.walk("D:\\" + str(id) + "\\" + dir)):
								if len(i[2]) > 0:
									for j in i[2]:
										if j.endswith(".tif"):
											if folder == "Сделано":
												count_file_c +=1
											if folder == "Переделано":
												count_file_p +=1
											if folder == "Жду ответа":
												count_file_z+=1

				list_search.append(str(id))
				list_search.append(str(count_file_c))
				list_search.append(str(count_file_p))
				list_search.append(str(count_file_z))

				self.list_search.append(list_search)

				count_file_c = 0
				count_file_p = 0
				count_file_z = 0
			except:
				logs.write("Не удалось проверить папку " + str(id))
				
		return list(self.list_search)

	def get_images(self, list_id, logs):
		self.list_id = list_id
		self.logs = logs
		SettingFunctions.checkdirs(self, list_id = self.list_id, logs = self.logs, mode = False)
		folders = ["Сделано", "Переделано"]
		logs.write("==========Начало загузрузки изображений==========", mode = False)
		settings = SettingFunctions.getSettings(self, logs = logs)
		path_app = ""
		for dir in os.listdir(str(settings["disk"]) + "\\id" + str(settings["id_approve"])):
			if "Проверяю" in dir:
				path_app = str(settings["disk"]) + "\\id" + str(settings["id_approve"]) + "\\" + str(dir)

		for id in list_id:
			try:
				for dir in os.listdir("D:\\" + str(id)):
					for folder in folders:
						if folder in dir:
							for i in list(os.walk("D:\\" + str(id) + "\\" + dir)):
								if len(i[2]) > 0:
									for j in i[2]:
										logs.write("Загрузка изображения " + str(id) )
										if j.endswith(".tif"):
											file = str(i[0]) + "\\"+str(j)
											shutil.move(file, path_app + "\\" + id)
			except:
				logs.write("Не удалось загузить изображение " + str(id))

	def upload_images(self):
		pass
		
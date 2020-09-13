from tkinter import *
from tkinter import ttk
from tkinter.ttk import Checkbutton
import datetime

class Checkbar(Frame):
   def __init__(self, parent = None, picks = [], side = LEFT, anchor = W):
      Frame.__init__(self, parent)
      self.vars = []
      columns = 1
      rows = 2
      test_id = ["5", "9", "42", "43", "45"]
      for pick in picks:
         var = IntVar()
         for id in test_id:
            if id == pick.split()[1]:
               var.set(1)
         
         chk = Checkbutton(self, text = pick, variable = var)
         if columns == 17:
            columns = 1
            chk.grid(column = columns, row = rows)
            rows += 1

         chk.grid(column = columns, row = rows)
         columns += 1

         self.vars.append(var)

   def state(self):

         return list(map((lambda var: var.get()), self.vars))

   def set(self):
         for i in self.vars:
            i.set(1)
   def clear(self):
      for i in self.vars:
         i.set(0)

class Table(Frame):
   def __init__(self, parent = None, headings = tuple(), rows = tuple()):
        super().__init__(parent)
  
        self.table = ttk.Treeview(self, show = "headings", selectmode = "browse")
        self.table["columns"] = headings
        self.table["displaycolumns"] = headings
        self.table["height"] = 12

        for head in headings:
            self.table.heading(head, text = head, anchor = CENTER)
            self.table.column(head, anchor = CENTER, width = 75)

        
  
        scrolltable = ttk.Scrollbar(self, command = self.table.yview)
        self.table.configure(yscrollcommand = scrolltable.set)
        scrolltable.pack(side = RIGHT, fill = Y)
        self.table.pack(expand = YES, fill = BOTH)

   def add(self, rows = tuple()):
      self.clear()
      for row in rows:
            self.table.insert('', END, values=tuple(row))

   def clear(self):
      self.table.delete(*self.table.get_children())



class Logs(Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent)

        scrollbar = ttk.Scrollbar(self)
        scrollbar.pack(side = 'right', fill = 'y')
        self._text = Text(self, state = DISABLED, *args, **kwargs)
        self._text.pack(side = "left", fill = 'both', expand = 1)
        self.now = datetime.datetime.now()

        scrollbar['command'] = self._text.yview
        self._text['yscrollcommand'] = scrollbar.set
        self._text['width'] = 65
        self._text['height'] = 18
        self._text['highlightbackground'] =  '#ebecee'
        self._text['highlightthickness'] = 1
       
    def write(self, text, mode = True):
        self._text.configure(state=NORMAL)
        if mode:
          self._text.insert(END, str(self.now.hour) + ":" + str(self.now.minute) + " " + str(text) + "\n")
        else:
          self._text.insert(END, str(text) + "\n")

        self._text.configure(state=DISABLED)
        self._text.yview_moveto('1.0')

    def clear(self):
        self._text.configure(state=NORMAL)
        self._text.delete(0.0, END)
        self._text.configure(state=DISABLED)

    def flush(self):
        # Метод нужен для полного видимого соответствия классу StringIO в части вывода
        pass
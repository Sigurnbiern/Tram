from tkinter import ttk
import customtkinter as ctk
from config import *
from MyDb import  data
from SheduleChange import change_window
from MyRoute import Rwindow
from MyStaff import Swindow



class Mwindow():

    def routetb_open(self):
        tablet = '"Route_TB"'
        request = '''SELECT * FROM public."Route_TB"
        ORDER BY "Route_num", "ID" ASC'''
        Rwindow.widjet_place(request= request, tablet=tablet)

    def routet_open(self):
        tablet = '"Route_T"'
        request = '''SELECT * FROM public."Route_T"
        ORDER BY "Route_num", "ID" ASC'''
        Rwindow.widjet_place(request= request, tablet=tablet)
    
    def staff_open(self):
        request = '''SELECT * FROM public."Staff"
        ORDER BY "ID" ASC'''
        Swindow.widjet_place(request=request)


    def open_insert_window(self):
        change_window.create_window(self.root)

    def open_delete_window(self):
        change_window.create_delete_window(self.root)
    
    def update_table(self):
        self.frame_table.pack_forget()
        self.frame_button.pack_forget()

        self.widjet_place()

    def widjet_place(self):
        '''Общий стиль'''
       

        self.frame_table = ctk.CTkFrame(self.root)
        self.frame_button = ctk.CTkFrame(self.root)

        table = ttk.Treeview(self.frame_table, show='headings') # Таблица
        scrollbar_y = ctk.CTkScrollbar(self.frame_table, command=table.yview) # Скролбары для таблицы
        scrollbar_x = ctk.CTkScrollbar(self.frame_table,orientation='horizontal', command=table.xview)

        button_update = ctk.CTkButton(self.frame_button, text='Обновить', command= self.update_table)

        button_insert_veh =  ctk.CTkButton(self.frame_button, text='Добавить данные', command=self.open_insert_window)
        button_delete_veh =  ctk.CTkButton(self.frame_button, text='Удалить строку', command=self.open_delete_window)

        button_rtbopen = ctk.CTkButton(self.frame_button, text='Мартушруты троллейбусов', command=self.routetb_open)
        button_rtopen = ctk.CTkButton(self.frame_button, text='Мартушруты трамваев', command=self.routet_open)
        button_staff_open = ctk.CTkButton(self.frame_button, text='Сортудники', command = self.staff_open)

       
        # Создаем фрейм с таблицей и кнопку возвращения
        table.configure(yscrollcommand=scrollbar_y.set)
        table.configure(xscrollcommand=scrollbar_x.set)

        # Размещаем скроллбары и таблицу на фрейме
        self.frame_button.pack(side='top',fill='x')
        self.frame_table.pack(side='bottom', fill='both', expand=True)
        
        button_update.pack(side='left',padx=10,pady=10)
        button_insert_veh.pack(side='left')
        button_delete_veh.pack(side='left')
        button_rtbopen.pack(side = 'top')
        button_rtopen.pack(side='top')
        button_staff_open.pack(side='top')

        
        scrollbar_y.pack(side='right', fill='y')
        scrollbar_x.pack(side='bottom', fill='x')
        table.pack(side='left', expand=True, fill='both',padx=10,pady=10)
        
        
        request = 'SELECT * FROM public."Vehicle"'
        
        rows = data.request_data(request= request)

        for row in table.get_children():
            table.delete(row)
        
        # Создание названий столбцов
        heads = ['Номер транспорта', 'Время старта', 'Время окончания', 'Тип транспорта', 'Номер маршрута', 'ID водителя', 'ID кондуктора'] 
        table['columns'] = heads

        # Распределение названий солбцов
        for header in heads:
            table.heading(header, text=header, anchor='center')
            table.column(header,anchor='center')

        # Распределение строк из бд по таблице
        for row in rows:
            table.insert("", "end", values=row)

        


    def __init__(self):

        
        '''Глваное окно'''
        self.root = ctk.CTk()
        self.root.title('Расписание')
        self.root.geometry('900x500')
        self.root.minsize(width=500, height=200)
        self.root.maxsize(width=1400, height=600)

        Mwindow.widjet_place(self)
       

        

        self.root.mainloop()

Mwindow()
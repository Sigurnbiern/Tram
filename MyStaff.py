from tkinter import ttk
import customtkinter as ctk
from config import *
from MyDb import  data
from StaffChange import change_window



class Swindow():

    def open_insert_window():
        change_window.create_window()

    def open_delete_window():
        change_window.create_delete_window()
    
    def update_table(staff_window, request):
        
        staff_window.destroy()

        Swindow.widjet_place(request)

    def widjet_place(request):

       
        staff_window = ctk.CTkToplevel()
        staff_window.title('Окно сотрудников')

        frame_table = ctk.CTkFrame(staff_window)
        frame_button = ctk.CTkFrame(staff_window)

        table = ttk.Treeview(frame_table, show='headings') # Таблица
        scrollbar_y = ctk.CTkScrollbar(frame_table, command=table.yview) # Скролбары для таблицы
        scrollbar_x = ctk.CTkScrollbar(frame_table,orientation='horizontal', command=table.xview)

        

        button_insert =  ctk.CTkButton(frame_button, text='Добавить данные', command=Swindow.open_insert_window)
        button_delete =  ctk.CTkButton(frame_button, text='Удалить строку', command=Swindow.open_delete_window)
        button_update = ctk.CTkButton(frame_button, text='Обновить', command= lambda: Swindow.update_table(staff_window, request))
       
        # Создаем фрейм с таблицей и кнопку возвращения
        table.configure(yscrollcommand=scrollbar_y.set)
        table.configure(xscrollcommand=scrollbar_x.set)

        # Размещаем скроллбары и таблицу на фрейме
        frame_button.pack(side='top',fill='x')
        frame_table.pack(side='bottom', fill='both', expand=True)
        
        
        button_insert.pack(side='left')
        button_delete.pack(side='left')
        button_update.pack(side='right')

        
        scrollbar_y.pack(side='right', fill='y')
        scrollbar_x.pack(side='bottom', fill='x')
        table.pack(side='left', expand=True, fill='both',padx=10,pady=10)
        
        
        
        
        rows = data.request_data(request= request)

        for row in table.get_children():
            table.delete(row)
        
        # Создание названий столбцов
        heads = ['ID', 'Должность', 'Имя', 'Номер телефона'] 
        table['columns'] = heads

        # Распределение названий солбцов
        for header in heads:
            table.heading(header, text=header, anchor='center')
            table.column(header,anchor='center')

        # Распределение строк из бд по таблице
        for row in rows:
            table.insert("", "end", values=row)

        



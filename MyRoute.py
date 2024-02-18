from tkinter import ttk
import customtkinter as ctk
from config import *
from MyDb import  data
from RouteChange import change_window



class Rwindow():

    def open_change_window(tablet):
        change_window.change_window(tablet)
    
    def open_insert_window(tablet):
        change_window.insert_window(tablet)

    def open_delete_window(tablet):
        change_window.create_delete_window(tablet)
    
    def update_table(route_window, request, tablet):
        
        route_window.destroy()

        Rwindow.widjet_place(request, tablet)

    def widjet_place(request, tablet):

       
        route_window = ctk.CTkToplevel()
        route_window.title('Окно маршрутов')

        frame_table = ctk.CTkFrame(route_window)
        frame_button = ctk.CTkFrame(route_window)

        table = ttk.Treeview(frame_table, show='headings') # Таблица
        scrollbar_y = ctk.CTkScrollbar(frame_table, command=table.yview) # Скролбары для таблицы
        scrollbar_x = ctk.CTkScrollbar(frame_table,orientation='horizontal', command=table.xview)

        

        button_insert =  ctk.CTkButton(frame_button, text='Добавить данные', command= lambda : Rwindow.open_insert_window(tablet))
        button_delete =  ctk.CTkButton(frame_button, text='Удалить строку', command=lambda : Rwindow.open_delete_window(tablet))
        button_change = ctk.CTkButton(frame_button, text='Поменять позицию остановки', command=lambda : Rwindow.open_change_window(tablet))
        button_update = ctk.CTkButton(frame_button, text='Обновить', command= lambda: Rwindow.update_table(route_window, request, tablet))
       
        # Создаем фрейм с таблицей и кнопку возвращения
        table.configure(yscrollcommand=scrollbar_y.set)
        table.configure(xscrollcommand=scrollbar_x.set)

        # Размещаем скроллбары и таблицу на фрейме
        frame_button.pack(side='top',fill='x')
        frame_table.pack(side='bottom', fill='both', expand=True)
        
        
        button_insert.pack(side='left')
        button_delete.pack(side='left')
        button_change.pack(side='left')
        button_update.pack(side='right')

        
        scrollbar_y.pack(side='right', fill='y')
        scrollbar_x.pack(side='bottom', fill='x')
        table.pack(side='left', expand=True, fill='both',padx=10,pady=10)
        
        
        
        
        rows = data.request_data(request= request)

        for row in table.get_children():
            table.delete(row)
        
        # Создание названий столбцов
        heads = ['ID', 'Номер маршрута', 'Название остановки'] 
        table['columns'] = heads

        # Распределение названий солбцов
        for header in heads:
            table.heading(header, text=header, anchor='center')
            table.column(header,anchor='center')

        # Распределение строк из бд по таблице
        for row in rows:
            table.insert("", "end", values=row)

        



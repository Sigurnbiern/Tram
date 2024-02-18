import customtkinter as ctk
from MyDb import data

class change_window():
    
    def change_data(label_oid,
            combo_box_name,
            entry_nid,
            combo_box_route,
            tablet,
            insert_window):
        
        oid = label_oid.cget('text')
        oid = int(oid)
        nid = entry_nid.get()
        nid = int(nid)
        name = combo_box_name.get()
        route =  combo_box_route.get()
        
        if nid < oid:
            data.insert_data(request=f'''update {tablet} set "ID" = "ID" + 1
            where "ID" >= {nid} and "ID" <= {oid} and "Route_num" = {route} 
            ''')

            data.insert_data(request=f'''update {tablet} set "ID" = {nid}
            where "Stop" = '{name}' and "Route_num" = {route}
            ''')
        else:
            data.insert_data(request=f'''update {tablet} set "ID" = "ID" - 1 
            where "ID" <= {nid} and "ID" >= {oid} and "Route_num" = {route}
            ''')

            data.insert_data(request=f'''update {tablet} set "ID" = {nid}
            where "Stop" = '{name}' and "Route_num" = {route}
            ''')
        insert_window.destroy()
    def update_label(*args):
        combo_box_name, label_oid, tablet = args
        select_item = combo_box_name.get()

        
        rows = data.request_data(request=f'''select "ID" from {tablet} where "Stop" = '{select_item}'
        ''')
        
        val = str()      
        for item in rows:
            val = item[0]
        
        
        label_oid.configure(text=val)


    def update_name_list(*args):
        
        variable_route, combo_box_name, tablet = args

        item = variable_route.get()

        rows = data.request_data(request=f'''select "Stop" from {tablet}
        where "Route_num" = {item}
        order by "ID" asc''')
        val = []        
        for item in rows:
            val.append(f'{item[0]}')

        combo_box_name.configure(values=val)

    def change_window(tablet):
        
        insert_window = ctk.CTkToplevel()
        insert_window.title('Изменить порядок маршрутов')
        
        label_route =  ctk.CTkLabel(insert_window, text='Ввод маршрута').grid(row=0,column=0)
        label_name =  ctk.CTkLabel(insert_window, text='Ввод названия остановки').grid(row=1,column=0)
        label_nid = ctk.CTkLabel(insert_window, text='Новая позиция').grid(row=2,column=0)
        label_show_oid = ctk.CTkLabel(insert_window, text='Текущая позиция:').grid(row=0, column=3)
        label_oid = ctk.CTkLabel(insert_window, text='')
        label_oid.grid(row=0,column=4)



        variable_route = ctk.StringVar()
        combo_box_route = ctk.CTkOptionMenu(insert_window, variable=variable_route)
        combo_box_route.grid(row=0,column=1)

        variable_name = ctk.StringVar()
        combo_box_name = ctk.CTkOptionMenu(insert_window, variable=variable_name)
        combo_box_name.grid(row=1,column=1)

        entry_nid = ctk.CTkEntry(insert_window)
        entry_nid.grid(row=2, column=1)
        

        rows = data.request_data(request=f'''select distinct "Route_num" from {tablet}
        order by  "Route_num" asc''')
        val = []        
        for item in rows:
            val.append(f'{item[0]}')

        combo_box_route.configure(values=val)

        variable_route.trace("w", lambda *args: change_window.update_name_list(variable_route, combo_box_name,tablet))

        variable_name.trace("w",  lambda *args: change_window.update_label(combo_box_name, label_oid, tablet))

          
        button_commit = ctk.CTkButton(insert_window,text='Сохранить',command=lambda: change_window.change_data(label_oid,
        combo_box_name,
        entry_nid,
        combo_box_route,
        tablet,
        insert_window)).grid(row=8,column=0, columnspan=2)
    
    def insert_data(entry_id, entry_route, entry_name, tablet, insert_window):
        
        id = entry_id.get()
        route = entry_route.get()
        name = entry_name.get()

        data.insert_data(request=f'''update {tablet} set "ID" = "ID" + 1 
        where "ID" >= {id} and "Route_num" = {route}
        
        ''')
        data.insert_data(request=f'''insert into {tablet}("ID", "Route_num", "Stop") values({id}, {route}, '{name}')
        ''')
        insert_window.destroy()
    def insert_window(tablet):
        
        insert_window = ctk.CTkToplevel()
        insert_window.title('Добавить маршрут/оставновку')

        label_id = ctk.CTkLabel(insert_window, text='Введите позицию остановки').grid(row=0,column=0)
        label_route = ctk.CTkLabel(insert_window, text='Введите номер маршрута').grid(row=1,column=0)
        label_name =  ctk.CTkLabel(insert_window, text='Ввод названия остановки').grid(row=2,column=0)
      
        entry_id = ctk.CTkEntry(insert_window)
        entry_id.grid(row=0, column=1)
        entry_route = ctk.CTkEntry(insert_window)
        entry_route.grid(row=1, column=1)
        entry_name = ctk.CTkEntry(insert_window)
        entry_name.grid(row=2, column=1)

        button_commit = ctk.CTkButton(insert_window, text='Сохранить', command= lambda: change_window.insert_data(entry_id, entry_route,
        entry_name, tablet,  insert_window)).grid(row=3,column=0, columnspan=2)



    def delete_data(combo_box_route, combo_box_name, tablet, delelete_window):
        
        route = combo_box_route.get()
        name= combo_box_name.get()
        rows = data.request_data(request=f'''select "ID" from {tablet}
        where "Route_num" = {route} and "Stop" = '{name}'
        ''')
        id = int()
        for item in rows:
            id = item[0]
        
        print(id)

        data.delete_data(request=f'''delete from {tablet}
        where "Route_num" = '{route}' and "Stop" = '{name}'
        ''')
        data.insert_data(request=f'''update {tablet}
        set "ID" = "ID" - 1
        where "Route_num" = {route} and "ID" > {id}
        ''')
        delelete_window.destroy()

    def create_delete_window(tablet):
        
        delelete_window = ctk.CTkToplevel()
        delelete_window.title('Удалить остановку')


        label_route = ctk.CTkLabel(delelete_window, text='Введите номер маршрута').grid(row=0, column=0)
        label_name = ctk.CTkLabel(delelete_window, text='Введите название остановки').grid(row=1, column=0)

        variable_route = ctk.StringVar()
        combo_box_route = ctk.CTkOptionMenu(delelete_window, variable= variable_route)
        combo_box_route.grid(row=0,column=1)

        variable_name = ctk.StringVar()
        combo_box_name = ctk.CTkOptionMenu(delelete_window, variable=variable_name)
        combo_box_name.grid(row=1,column=1)

        rows = data.request_data(request=f'''select distinct "Route_num" from {tablet}
        order by "Route_num" asc
        ''')
        val = []        
        for item in rows:
            val.append(f'{item[0]}')

        combo_box_route.configure(values=val)

        variable_route.trace("w", lambda *args: change_window.update_name_list(variable_route, combo_box_name, tablet))

        button_accept_delete = ctk.CTkButton(delelete_window, text='Применить',command=lambda:change_window.delete_data(combo_box_route, combo_box_name, 
        tablet, delelete_window)).grid(row=2,column=0, columnspan=2)

  
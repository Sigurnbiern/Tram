import customtkinter as ctk
from MyDb import data

class change_window():
    
    def insert_data(entry_nveh, 
        entry_tstart, 
        entry_tstop, 
        combo_box_route, 
        combo_box_typet,
        combo_box_idd, 
        combo_box_idc):

        num_veh = entry_nveh.get()
        time_start = entry_tstart.get()
        time_stop = entry_tstop.get()
        type_veh = combo_box_typet.get()
        route_n = combo_box_route.get()
        id_d = combo_box_idd.get()
        id_c = combo_box_idc.get()
        
        data.insert_data(request=f'''insert into  public."Vehicle"
        values('{num_veh}','{time_start}','{time_stop}','{type_veh}','{route_n}','{id_d}','{id_c}')''')

    def update_route_list(*args):
        variable_typet, combo_box_route = args
        select_item = variable_typet.get()

        

        if select_item == 'Трамвай':
            rows = data.request_data(request='''select distinct "Route_num" from "Route_T"
            group by "Route_num"''')


        elif select_item == 'Троллейбус':
            rows = data.request_data(request='''select distinct "Route_num" from "Route_TB"
            group by "Route_num"''')

        
        val = []        
        for item in rows:
            val.append(f'{item[0]}')
        
        
        combo_box_route.configure(values=val)



    def create_window(root):
        
            insert_window = ctk.CTkToplevel(root)
            insert_window.title('Добавить данные')

            label_nveh = ctk.CTkLabel(insert_window, text='Ввод номера').grid(row=1,column=0)
            label_tstart = ctk.CTkLabel(insert_window, text='Ввод времени выезда').grid(row=2,column=0)
            label_tstop = ctk.CTkLabel(insert_window, text='Ввод времени конца смены').grid(row=3,column=0)
            label_tveh = ctk.CTkLabel(insert_window, text='Ввод типа транспорта').grid(row=4,column=0)
            label_rn = ctk.CTkLabel(insert_window, text='Ввод маршрута').grid(row=5,column=0)
            label_idd = ctk.CTkLabel(insert_window, text='Ввод ID водителя').grid(row=6,column=0)
            label_idc = ctk.CTkLabel(insert_window, text='Ввод ID кондуктора').grid(row=7,column=0)

            entry_nveh = ctk.CTkEntry(insert_window)
            entry_tstart = ctk.CTkEntry(insert_window)
            entry_tstop = ctk.CTkEntry(insert_window)


            
           

            variable_idd = ctk.StringVar()
            combo_box_idd = ctk.CTkOptionMenu(insert_window, variable=variable_idd)
            combo_box_idd.grid(row=6,column=1)

            variable_idc = ctk.StringVar()
            combo_box_idc = ctk.CTkOptionMenu(insert_window, variable=variable_idc)
            combo_box_idc.grid(row=7,column=1)
            
            rows = data.request_data(request='''select "ID" from "Staff" 
            where "Post" = 'Водитель'
            ''')
            val = []        
            for item in rows:
                val.append(f'{item[0]}')

            combo_box_idd.configure(values=val)

            rows = data.request_data(request='''select "ID" from "Staff" 
            where "Post" = 'Кондуктор'
            ''')
            val = []        
            for item in rows:
                val.append(f'{item[0]}')
            combo_box_idc.configure(values=val)

            entry_nveh.grid(row=1,column=1)
            entry_tstart.grid(row=2,column=1)
            entry_tstop.grid(row=3,column=1)
         
            variable_typet = ctk.StringVar()
            combo_box_typet = ctk.CTkOptionMenu(insert_window, variable= variable_typet,values=['Трамвай', 'Троллейбус'])
            combo_box_typet.grid(row=4,column=1)

            variable_route = ctk.StringVar()
            combo_box_route = ctk.CTkOptionMenu(insert_window, variable=variable_route)
            combo_box_route.grid(row=5,column=1)

            variable_typet.trace("w",  lambda *args: change_window.update_route_list(variable_typet, combo_box_route))

            button_commit = ctk.CTkButton(insert_window,text='Сохранить',command=lambda: change_window.insert_data(entry_nveh, 
            entry_tstart, 
            entry_tstop, 
            combo_box_route, 
            combo_box_typet, 
            combo_box_idd, 
            combo_box_idc)).grid(row=8,column=0, columnspan=2)

    def delete_data(combo_box_numv):
        
        data_del = combo_box_numv.get()
        data.delete_data(request=f'''DELETE FROM public."Vehicle"
        WHERE "Num_vehicle" = '{data_del}';''')

    def create_delete_window(root):
        
        delelete_window = ctk.CTkToplevel(root)
        delelete_window.title('Удалить данные')
        
        rows = data.request_data(request='select "Num_vehicle" from "Vehicle"')
       
        

        label_delete = ctk.CTkLabel(delelete_window, text='Введите регистрационный номер').grid(row=0, column=0)
        variable_numv = ctk.StringVar()
        combo_box_numv = ctk.CTkOptionMenu(delelete_window, variable= variable_numv)
        combo_box_numv.grid(row=0,column=1)

        val = []        
        for item in rows:
            val.append(f'{item[0]}')

        combo_box_numv.configure(values=val)

        button_accept_delete = ctk.CTkButton(delelete_window, text='Применить',command=lambda:change_window.delete_data(combo_box_numv)).grid(row=1,column=0)

  
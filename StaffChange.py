import customtkinter as ctk
from MyDb import data

class change_window():
    
    def insert_data(entry_post,
            entry_name,
            entry_phone):

        post= entry_post.get()
        name = entry_name.get()
        phone = entry_phone.get()
        
        data.insert_data(request=f'''insert into  public."Staff"("Post", "Name", "Phone_num")
        values('{post}', '{name}', '{phone}')''')

    def create_window():
        
            insert_window = ctk.CTkToplevel()
            insert_window.title('Добавить сотрудника')

            label_post = ctk.CTkLabel(insert_window, text='Ввод должности').grid(row=0,column=0)
            label_name = ctk.CTkLabel(insert_window, text='Ввод имени').grid(row=1,column=0)
            label_phone = ctk.CTkLabel(insert_window, text='Ввод телефона').grid(row=2,column=0)
          
            entry_post = ctk.CTkEntry(insert_window)
            entry_name = ctk.CTkEntry(insert_window)
            entry_phone = ctk.CTkEntry(insert_window)

            entry_post.grid(row=0,column=1)
            entry_name.grid(row=1,column=1)
            entry_phone.grid(row=2,column=1)
         

            button_commit = ctk.CTkButton(insert_window,text='Сохранить',command=lambda: change_window.insert_data(entry_post,
            entry_name,
            entry_phone)).grid(row=8,column=0, columnspan=2)

    def delete_data(combo_box_numv):
        
        data_del = combo_box_numv.get()
        data.delete_data(request=f'''DELETE FROM public."Staff"
        WHERE "ID" = '{data_del}';''')

    def create_delete_window():
        
        delete_window = ctk.CTkToplevel()
        delete_window.title('Удалить сотрудника')
        rows = data.request_data(request='select "ID" from "Staff"')
       
        

        label_delete = ctk.CTkLabel(delete_window, text='Введите идентификатор').grid(row=0, column=0)
        variable_id = ctk.StringVar()
        combo_box_id = ctk.CTkOptionMenu(delete_window, variable= variable_id)
        combo_box_id.grid(row=0,column=1)

        val = []        
        for item in rows:
            val.append(f'{item[0]}')

        combo_box_id.configure(values=val)

        button_accept_delete = ctk.CTkButton(delete_window, text='Применить',command=lambda:change_window.delete_data(combo_box_id)).grid(row=1,column=0)

  
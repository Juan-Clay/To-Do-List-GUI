import backend as logic

from tkinter import END
#Where the list object will exist
main_list = logic.ToDoList()


#Updates the center display that shows the names of the tasks with the date
#Called when a new object is added
#The two arguments are the two lists to update
def update_Display_List(names, dates):
    names.delete(0, main_list.length)
    dates.delete(0, main_list.length)
    nms, dts = main_list.get_Names_Dates()
    for i in range(0, len(nms)):
        names.insert(END, nms[i])
        dates.insert(END, dts[i])
    return




#Updates the display on the side that shows the description and any other extra info
def update_Display_Side(info, n_list):
    index = n_list.curselection()[0]
    
    info.configure(text = '')
    info.configure(text = main_list.get_desc(index))





#Pass the error label AND the input OBJECTS, need to do .get() to get the strings
def add_task_click(error, nm, pri, desc, dt, name_list, date_list):

    #first validate if priority and date, the other two can say whatever they want

    #List so that if there is an error, the error displays on the error label as a list
    error_msg = ''

    tsk_mesg = main_list.does_task_exist(nm.get())
    pri_mesg = main_list.validate_Priority(pri.get())
    dt_mesg = main_list.validate_Date(dt.get())

    if pri_mesg != "valid":
        error_msg += pri_mesg

    if dt_mesg != "valid":
        if error_msg != '':
            error_msg += "\n"
        error_msg += dt_mesg

    if tsk_mesg != "valid":
        if error_msg != '':
            error_msg += "\n"
        error_msg += tsk_mesg


    
    #Check for if there are any errors in the input. 
    if error_msg != '':
        error.configure(text = error_msg)
    #If there are no errors, clear the error textbox and add the new node to the list
    else:
        error.configure(text = '')
        main_list.addItem(nm.get(), pri.get(), desc.get(), dt.get())
        update_Display_List(name_list, date_list)
        

    
    
    


from tkinter import *
import frontend_functions as actions

#Build the app layout
#Dispay all the info being stored in the front end functions


root = Tk()

#----------------------------------BACKGROUND LAYOUT------------------------------------

root.minsize(750, 600)
root.maxsize(750, 600)

root.configure(bg = "dark grey")
root.title("To-do List App")

#Create center section that will house the list
center = Label(root, bg = "light grey", width = 30, height = 24, font = 30)
center.place(anchor = S, relx = 0.5, rely = 1)


#Create title area
title = Label(root, bg = "grey", text = "To-do List", width = 750, height = 2, font = 30)
title.place(anchor = N, relx = 0.5, rely = 0.0)

#Side section that will contain info on selected task



info = Label(root, bg = "light grey", width = 14, height = 7, font = 30)
info.place(anchor = S, relx = 0.86, rely = 0.85)

#-----------------------------------------------------------------------------------------


#----------------------------------------DISPLAY LIST -------------------------------------------------


name_list = Listbox(root, width = 20, height = 17, justify = CENTER, selectmode = SINGLE, )
name_list.place(anchor = N, relx = 0.44, rely = 0.5)






date_list = Listbox(root, width = 15, height = 17, justify = CENTER, bg = "grey")
date_list.place(anchor = W, relx = 0.52, rely = 0.73)


#------------------------------------------------------------------------------------------------------

#---------------------------------INPUT LAYOUT--------------------------------------------

#Prompt if to add a new task, followed by space to fill out all info needed for new item
add_label = Label(root, bg = "light grey", text = "Enter new task")
add_label.place(anchor = N, relx = 0.5, rely = 0.1) 



#Name of the task-----------------------------------------------------------
task_name = Label(root, bg = "light grey", text = "Name")
task_name.place(anchor = N, relx = 0.4, rely = 0.15)

#Name input
task_name_input = Entry(root)
task_name_input.place(anchor = N, relx = 0.55, rely = 0.15)



#Priority of the task-------------------------------------------------------
task_priority = Label(root, bg = "light grey", text = "Priorirty")
task_priority.place(anchor = N, relx = 0.4, rely = 0.2)

#Priority input
task_priority_input = Entry(root)
task_priority_input.place(anchor = N, relx = 0.55, rely = 0.2)



#Description of the task----------------------------------------------------
task_description = Label(root, bg = "light grey", text = "Description")
task_description.place(anchor = N, relx = 0.4, rely = 0.25)

#Decription input
task_description_input = Entry(root)
task_description_input.place(anchor = N, relx = 0.55, rely = 0.25)



#Due date of the task, formated as mm/dd/yy---------------------------------
task_due_date = Label(root, bg = "light grey", text = "Due date (mm-dd-yyyy)")
task_due_date.place(anchor = N, relx = 0.38, rely = 0.3)

task_due_date_input = Entry(root)
task_due_date_input.place(anchor = N, relx = 0.55, rely = 0.3)

#shows text only when there was an issue with the input, will display which field needs correcting
#(Change background to light grey when add functionalilty)
invalid_input = Label(root, bg = "white", text = "", fg = "red", width = 30)
invalid_input.place(anchor = N, relx = 0.5, rely = 0.4)


#Button to check if input is valid, then update list------------------------

#Command passes the function which takes in all the input strings plus the error label, to validate the inputs and later pass them to the list box
#Passes the lists as well since it needs that access if it will update that list
submit = Button(root, bg = "light grey", text = "Add task", 
                command = lambda : actions.add_task_click(invalid_input, 
                                                          task_name_input, 
                                                          task_priority_input, 
                                                          task_description_input, 
                                                          task_due_date_input, 
                                                          name_list, 
                                                          date_list))
submit.place(anchor = N, relx = 0.5, rely = 0.35) 

open_desc = Button(root, bg = "light grey", text = "Open Description", 
                   command = lambda : actions.update_Display_Side(info, name_list))
open_desc.place(anchor = N, relx = 0.86, rely = 0.5)



#------------------------------------------------------------------------------------------------------







root.mainloop()

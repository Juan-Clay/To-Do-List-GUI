
from datetime import datetime

#Will create a list object, might go ahead and make it a linked list to add a bit of difficulty and to have several properties per item 
#Doubly linked list cause it might come in handy when sorting


#"Node" class for this program
class Item:
    def __init__(self, nm = '', pri = 0, desc = '', due = ''):
        self.next = None
        self.prev = None

        self.name = nm
        self.priority = pri
        self.description = desc
        self.dueBy = due

#Will create the first nodde upon creation and house many different functions in order to give functionality to the list
class ToDoList:

    #Initialize list by creating header node, header node will not be an actual Item in the list
    def __init__(self):
        self.header = Item("head")
        self.trailer = Item("tail")

        self.header.next = self.trailer
        self.trailer.prev = self.header

        self.length = 0


    #Checks if the current task already exists
    def does_task_exist(self, n):
        if self.header == None:
            return "valid"
        else:
            tNode = self.header.next
            while(tNode != None):
                if tNode.name == n:
                    return "Task already exists"
                tNode = tNode.next
        return "valid"
        


        

    #Add specified item, items should be in order of priority, 1 being the most important, no repeated values
    def addItem(self, nm, pri, desc, due):
        

        new_item = Item(nm, int(pri), desc, due)

        #If the list is empty
        if(self.header.next == None):
            self.header.next =  new_item
            self.trailer.prev =  new_item

            new_item.prev = self.header
            new_item.next = self.trailer

            
        #If the list is not empty, Look for where the item will go, check every item in the list if the priority value already exists
        else:
            #Will iterate through the list, starts at first node that is not the header
            tNode = self.header.next

            while True:
                if tNode.priority >= new_item.priority:
                    #Add new node before current node
                    new_item.prev = tNode.prev
                    tNode.prev.next = new_item
                    tNode.prev = new_item
                    new_item.next = tNode
                    self.length += 1
                    return
                else:
                    if tNode.next == None:
                        break
                    else:
                        tNode = tNode.next
            
            #If it reaches this point, the node goes at the end
            tNode.prev.next = new_item
            new_item.prev = tNode.prev
            new_item.next = tNode
            tNode.prev = new_item
        self.length += 1
        return


    #Remove specified item
    def removeItem(self, item_nm):
        if self.header == None:
            print("The list is empty\n\n")
        else:
            tNode = self.header.next
            while(tNode != None):
                if tNode.name == item_nm:
                    tNode.prev.next = tNode.next
                    tNode.next.prev = tNode.prev
                    del tNode
                    self.length -= 1
                    return
                tNode = tNode.next
            print("Item was not found in the list\n\n")
        self.length -= 1
        return
        
            



    #Updates the specified item, might make helper functions in order to do this once since I plan on making it prompt the user what they would like to change (Priority, Name, Description, Due date, ect)
    def updateItem(self):
        pass



    def printList(self):
        if self.header.next == None or self.header.next.next == None:
            print("The list is empty\n\n")

        else:
            tNode = self.header.next
            while(tNode.next != None):
                print("Title: " + tNode.name)
                print("Priority: " + str(tNode.priority))

                #For desc and due date, if they are empty it does not print out the linea
                if tNode.description != '':
                    print("Description: " + tNode.description)

                if tNode.dueBy != '':
                    print("Due date: " + tNode.dueBy)
                print("\n\n")

                tNode = tNode.next
            print("\n\n")
        return
    
    #Validate the date in the format mm-dd-yyyy
    def validate_Priority(self, pri):
        
        if pri.isnumeric():
            if int(pri) > 0:
                return "valid"
            else:
                return "Priority less than one"
        return "Not a number"
    
    #Validate the date using datetime, code from geeks for geeks
    def validate_Date(self, dt):
        format = "%m-%d-%Y"
      
        res = True
        
        try:
            res = bool(datetime.strptime(dt, format))
        except ValueError:
            res = False
        if res == False:
            return "Date invalid mm-dd-yyyy"
        else:
            return "valid"
        
    def get_Names_Dates(self):
        if self.header.next == None or self.header.next.next == None:
            return ["Invalid"], ["Invalid"]

        else:
            nms = []
            dts = []
            tNode = self.header.next
            while(tNode.next != None):
                nms.append(tNode.name)
                dts.append(tNode.dueBy)


                tNode = tNode.next
        return nms, dts
   
    #Gets the description of the specified index of the list
    def get_desc(self, index):
        if self.header == None:
            print("The list is empty\n\n")
        else:
            counter = 0
            tNode = self.header.next
            while(tNode != None):
                if counter == index:
                    return tNode.description
                counter += 1
                tNode = tNode.next
            print("Item was not found in the list\n\n")
        return





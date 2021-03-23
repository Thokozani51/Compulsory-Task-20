from datetime import date #importing of an automatic setting of the current date

user_name = ""
user_name = input("Enter your user_name: ") #user_name input
user_password = input("Enter your user_password: ") #user_password input



while True:#using the while loop for the process of noting messages of when the user enters the wrong or right user_name/user_password inputs
    user =  open("user.txt", "r") #open the user.txt file
    flag = False #if the credentials are false the programme will request the correct credentials 
    for user_read in user: #reading of lines from the file
        new_user = user_read.split(", ") #splitting the coma and the spacing inbetween the user_name and the user_password 
        
        if user_name == new_user[0]: #if the user_name is the same with the new_user to be entered by the new_user                
            if user_password == new_user[1].strip("\n"): #displaying the stripping of the new line(\n)
                print("Correct credentials!") #printing out of the outcome message when the user_name == new_user
                flag = True #if the credentials are true,the programme will move forward to the menu
                break #breaking of the process 
    if flag:
        break
    
    print("You've entered the wrong password or user name") # the error message will be displayed when the user has entered the wrong password or user_name
    user_name = input("Enter your user_name: ") #user_name input
    user_password = input("Enter your user_password: ") #user_password input
    user.close()#closing of the file

while True: #using the while loop for the user to move on to the menu list if all their loggin credentials are correct           
    print("Please enter one of the following options") #printing the options noted below for the users to select from
    print("r-register user")
    print("a-add task")
    print("va-view all tasks")
    print("vm-view my tasks")
    print("ds - Displaying statistics")
    print("e-exit")

    selection = input() #the users input from the selected option above

    if selection =='r': #if the user's input is 'r' from the options provided
        output_file = open("user.txt","a") #open the user.txt file with the append mode for inserting the input of logging in details
        user_nam = input("Please enter a new username") #input of the new user_name from the user
        user_password = input("Please enter a new password") #input of the new password from the user
        confirmed_user_password = input("Please confirm password") #confirmation of the password
        if user_password == confirmed_user_password :#if the user_password is the same as the confirmed_user_password the user can move on to the next stage selected
            output_file.write(f"\n{user_nam}, {user_password}") #code for writing the user_name and user_password into the user.txt file
            
        else:
            print("Passwords not the same") #error message to be displayed if the user has entered the wrong password   
        
    if selection == 'a': #if the user's input is 'a' from the options provided above
        
        output_file = open("tasks.txt","a") #opening the tasks.txt file with the append mode
        user_nam = input("Enter your username")#requesting the user_name input after they have selected the adding a task option 'a'
        user_task = input("Enter title of task")#requesting the title of task the user wants to include
        task_description = input("Enter description of task")#requesting the task description to be noted by the user
        task_completion = "No" #noting that the task noted on the task file is incompleted
        date_assigned = date.today()#displaying the date assigned for the task noted
        due_date = input("Enter due date of task") #displaying the due date of the task
        print("write in tasks.txt") #allowing the details noted by the user in the tasks txt file
        output_file.write(f"\n{user_nam}, {user_task}, {task_description}, {date_assigned}, {due_date}, {task_completion} ")#add the code that will open task.txt and write the data to the file
        output_file.close() #closing of file 
    if selection == 'va': # if the user's input is 'va' from the options provided above
        f = open("tasks.txt", "r") #opening the tasks.txt file with the read only mode
        
        for text in f: #reading a line from the text file
            taskList = text.split(", ") #separate the string when ever we come across a commer and a space
            print(f"Task: {taskList[1]}") #Displaying task title to the console
            print(f"Assigned to: {taskList[0]}")#Displaying the user name of the person assigned that task 
            print(f"Date assigned: {taskList[3]}")# Displaying the date the was assigned to the user to con6sole 
            print(f"Due date: {taskList[4]}")#Displaying the due date of the task to the console 
            print(f"Task complete: {taskList[5]}")#Displaying the Yes/No idicating whether a task is completed of not
            print(f"Task Description: {taskList[2]}")#Displaying the description of the task on the console
        f.close()#closing of the file
        
        
    if selection == 'vm': #if the user's input is 'vm' from the options above
        f = open("tasks.txt", "r") #opening the tasks.txt file with the read only mode
        
        for text in f: #reading a line from the text file
            taskList = text.split(", ") #separate the string when ever we come across a comma and a space
            if taskList[0] == user_name:#if the user_name noted by the user is the same as the user_name on the file
                print(f"Task: {taskList[1]}") #Displaying task title to the console
                print(f"Assigned to: {taskList[0]}")#Displaying the user name of the person assigned that task 
                print(f"Date assigned: {taskList[3]}")# Displaying the date the was assigned to the user to con6sole 
                print(f"Due date: {taskList[4]}")#Displaying the due date of the task to the console 
                print(f"Task complete: {taskList[5]}")#Displaying the Yes/No idicating whether a task is completed of not
                print(f"Task Description: {taskList[2]}")#Displaying the description of the task on the console
        f.close() #closing the tasks file


        
    if selection == "ds":#if the user's selection is displaying statistics 'ds'
        f = open("tasks.txt", "r") #opening the tasks.txt file with the read only mode
        num_tasks = 0 #count number of tasks in the file
        for line in f: #reading a line from the text file
            num_tasks += 1 #incrementing number of tasks in the task file.
            
    
        user = open("user.txt", "r") #opening the user.txt file with the read only mode
        num_users = 0 #count number of users in the file
        for line in user: #reading a line from the text file
            num_users += 1 #incrementing number of user in the task file.
            
        print(f"The total number of users is {num_users}")#calling out the function of finding the total number of users in users text file
        print(f"The total number of tasks is {num_tasks}")#calling out the function of finding the total number of tasks in the tasks text file
    
    
    if selection =='e':#if the user selects the exit 'e' option 
        break  #the end of the programme after the user selects the exit 'e' option     
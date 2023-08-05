"""this will contain all the main functionalities and like running the main program and screen printing functions"""

import os
import criteria
import brand
import shoe
#PRINTING FUNCTIONS STARTS HERE



def print_header(menu_name):
    """gets the name of the Menu

    param:
    menu_name: title of the current menu
    """
    message_width = 82
    
    white_spaces=" "
    line = "="
    for i in range(int((message_width+2-len(menu_name))/2)):
        white_spaces += " "
    for i in range(message_width+2):
        line += "="
    print(line)
    print("{0}|{1}|{2}".format(white_spaces,menu_name,white_spaces))
    print(line)

def print_header_lower(menu_name):
    """gets the name of the Menu and prints the Sub Menu lower Header on the screen

    param:
    menu_name: title of the current menu
    """
    message_width = 82
    
    white_spaces=" "
    line = "."
    for i in range(int((message_width+2-len(menu_name))/2)):
        white_spaces += " "
    for i in range(message_width+2):
        line += "."
    print(line)
    print("{0}|{1}|{2}".format(white_spaces,menu_name,white_spaces))
    print(line)

def print_criteria_menu_ingredient_line(criteria, modification = False, length = 85):
    """Takes a criteria as an input
    formats and prints it to screen as a menu item
    
    param: 
    modification: If this criteria is choosen for modification or not
    criteria: criteria as criteria class
    """
    menu_line =[]
    menu_item = "[{0}] {1}".format(str(criteria.id),criteria.text.upper())
    if modification:
        selection_indicator_head = ">>>"
        selection_indicator_tail = "<<<"
        menu_item = "{0}[{1}] {2}{3}".format(selection_indicator_head,str(criteria.id),criteria.text.upper(),selection_indicator_tail)
    menu_item_list = list(menu_item)
     
    if modification == False:
        for i in range(length):
            menu_line.append("-")
        menu_line[0] = ":"
        for i in range(2,len(menu_item_list)+2):
            menu_line[i] = menu_item_list[i-2]
        index = len(menu_line)-2
        for choice in criteria.choices:
            if criteria.current_value == None or criteria.current_value.lower() != choice.lower():
                choice_list = list(choice)
            else:
                selection_string = "[{0}]".format(choice)
                choice_list = list(selection_string)
            for i in range(len(choice_list)-1,-1,-1):
                menu_line[index] = choice_list[i]
                index -= 1
            menu_line[index]="|"
            index -= 1
    else:
        #length = length-(len(selection_indicator_head)+len(selection_indicator_tail))-4*len(criteria.choices)-1
        for i in range(length):
            menu_line.append("-")
        menu_line[0] = ":"
        for i in range(2,len(menu_item_list)+2):
            menu_line[i] = menu_item_list[i-2]
        last_index = len(menu_line)-2
        choice_list = []
        for choice_index in range(len(criteria.choices)):
            corrected_choice_text =  "[{0}] {1} ".format(choice_index, criteria.choices[choice_index])
            corrected_choice_text_list = list(corrected_choice_text)
            for letter_index in range(len(corrected_choice_text_list)-1,-1,-1):
                menu_line[last_index] = corrected_choice_text_list[letter_index]
                last_index -= 1
        menu_line[last_index]="|"
        
    menu_line[-1]=":"

    
    print("".join(menu_line))
    
def print_welcome_screen(welcome_message = "Running Shoe Advisor", height=9, length=86):
    """prints the initial screen to terminal
    param:
    height: number of the characters in vertical axis
    length: number of characters in horizontal axis
    """
    outer_boundary = ""
    welcome_message = " " + welcome_message + " "
    outer_frame_char = "|"
    inner_frame_char = "O"
    inner_frame_upper_boundry_index = int((height-3)/2)
    inner_frame_text_index = inner_frame_upper_boundry_index + 1
    inner_frame_lower_boundry_index = inner_frame_upper_boundry_index + 2
    
    inner_frame_left_boundry_index = int((length - (len(welcome_message)))/2)
    inner_frame_right_boundry_index = inner_frame_left_boundry_index + len(welcome_message)
    
    welcome_screen_chars_array = [[" "] * length for i in range(height)] 
    for horizontal_index in range(length):
        welcome_screen_chars_array[0][horizontal_index] = outer_frame_char
        welcome_screen_chars_array[-1][horizontal_index] = outer_frame_char
    for vertical_index in range(height):
        welcome_screen_chars_array[vertical_index][0] = outer_frame_char
        welcome_screen_chars_array[vertical_index][-1] = outer_frame_char

    #creating inner frames
    for row_index in range(height):
        if  row_index == inner_frame_upper_boundry_index or row_index == inner_frame_lower_boundry_index:
            for column in range(inner_frame_left_boundry_index,inner_frame_right_boundry_index+1):
                welcome_screen_chars_array [row_index][column] = inner_frame_char
        if row_index == inner_frame_text_index:
            column = inner_frame_left_boundry_index + 1
            for letters in welcome_message:
                welcome_screen_chars_array [row_index][column] = letters
                column += 1
    for row_index in range(height):
        current_line = ""
        for column_index in range(length):
            current_line += welcome_screen_chars_array[row_index][column_index]
        print(current_line)
    
            

     
    
    #print_header("Running Shoe Advisor V1")
    
    
    
    

def print_main_menu():
    """
    prints main menu to the screen
    """
    print_header("Main Menu")
    print_header("[M] = Modify Criterias [F] = Find Shoes with current criterias [Q] = Quit Program")
    
    
    

def print_criteria_screen(selectedCriteria = None):
    """
    Prints CRTIERIA MODIFICATION menu to the secreen and ask user for an input
    returns the user input
    
    param:
    current_menu_choices: list of possible menu choices until this function is called
    """
    print_header("MODIFY CRITERIAS")
    print_current_criteria_selections(selectedCriteria)
    
    
     

def print_current_criteria_selections(selectedCriteria = None):
    """
    prints current possible choices List to the screen
    and modifies current_menu_choices list by adding current criterias' shortcuts
    
    param: 
    current_menu_choices: list of possible menu choices until this function is called
    """
    criteria_menu_choices = []
    print_header_lower("Here are the current Criteria Selections")
    for crit in criteria.Criteria.criteria_db:
        if selectedCriteria != None and selectedCriteria == crit:
            print_criteria_menu_ingredient_line(crit, True)
        else:
            print_criteria_menu_ingredient_line(crit)
            

def print_navigation_menu_screen():
    print_header("Navigation Menu")
    print_header("[H] = Return Home [Q] = Quit Program")      

def print_criteria_modification_screen(criteria):
    os.system('cls')
    print_header(criteria.text.upper()) 
    print_criteria_modification_choices(criteria)       

def print_criteria_modification_choices(criteria):
    """
    criteria modification screen is printed on the screen
    first it shows the possible choices (non-numeric criterias)
    and then shows the current selection and asks for the Update
    """
    if criteria.is_numeric == False:
        print("---------------------------")
        print("Possible Choices: ")
        choice_line =""
        current_selection = "None"
        if criteria.current_value != None:
            current_selection = criteria.current_value
        for choice in criteria.choices:
            choice_line += " | " + choice
        print(choice_line)
        print("---------------------------")
    
        print("Current selection is: " + current_selection)
        print("\n")
        user_choice = input("Enter the ID of the choice you want to make")
    else:
        current_selection = "None"
        if criteria.current_value != None:
            current_selection = criteria.current_value
        print("---------------------------")
        print("Current value is: " + current_selection)

    

    


#PRINTING FUNCTIONS ENDS HERE



#MAIN PROGRAM FUNCTIONS STARTS HERE
def main_menu_screen(current_menu_choices=[]):
    """
    All the operations related to main/opening screen is in this function
    """
    print_main_menu()
    update_possible_choices(current_menu_choices, main_menu_shortcuts())
    user_choice = get_user_choice("Please Select an option from the Main Menu items: ")
    while user_choice.lower() not in current_menu_choices:
        os.system('cls')
        current_menu_choices = []
        print_welcome_screen()
        main_menu_screen(current_menu_choices)
        print("You have made an INVALID selection")
        user_choice = get_user_choice("Please Select an option from the Main Menu items: ")


    if user_choice.lower() == "m":
        os.system('cls')
        criteria_menu_screen()
    if user_choice.lower() == "f":
        pass                                 
    if user_choice.lower() == "q":
        print("BYE, hope to see you again!")
        return    
def program_navigation_menu_screen(current_menu_choices):
    "This screen will be printed all the menus so user turn back to main main or quit etc."
    navigation_shortcuts = ["h", "q"]
    update_possible_choices(current_menu_choices, navigation_shortcuts)
    print_navigation_menu_screen()

def criteria_menu_screen():
    """
    All the operations related to criteria menu screen is here
    """
    current_menu_choices = []
    print_criteria_screen()
    program_navigation_menu_screen(current_menu_choices)
        
    update_possible_choices(current_menu_choices,criteria_screen_shortcuts())
    user_choice = get_user_choice("Please Enter The Shortcut of the item you are interested: ")
    while check_user_choice_validity(user_choice,current_menu_choices) == False:
        os.system('cls')
        user_choice = criteria_menu_screen()    
    if  user_choice.lower() == "h":
        os.system('cls')
        current_menu_choices = []
        print_welcome_screen()
        main_menu_screen(current_menu_choices)
        return
    elif  user_choice.lower() == "q":
        print("BYE, hope to see you again!")
        return 
    else:
        os.system('cls')
        current_criteria = criteria.Criteria.find_criteria_with_id(int(user_choice))
        
        print_criteria_screen(current_criteria)
        print("\n\n")
        
        if current_criteria.is_numeric:  
           user_choice = get_user_choice("Please Enter {0}: ".format(current_criteria.text.upper())) 
           input_Float = is_user_input_float(user_choice)
           while input_Float == False:
               os.system('cls')
               
               print_criteria_screen(current_criteria)
               print("!!! This is an INVALID VALUE!!!")
               print("\n\n")
               user_choice = get_user_choice("Please Enter {0}: ".format(current_criteria.text.upper())) 
               input_Float = is_user_input_float(user_choice)
           user_choice = float(user_choice)
           #below the selected value of this criteria is assigned 
           criteria.Criteria.change_numeric_criteria_current_value(current_criteria,user_choice)
        else:
            current_menu_choices = []
            for index in range(len(current_criteria.choices)):
                current_menu_choices.append(str(index).lower())
            user_choice = get_user_choice("Please Select The Choice to Apply: ")
            while check_user_choice_validity(user_choice,current_menu_choices) == False:
                os.system('cls')
                print_criteria_screen(current_criteria)
                print("!!! You have made an INVALID selection!!!")
                print("\n\n")
                user_choice = get_user_choice("Please Select The Choice to Apply: ") 
            #below the selected value of this criteria is assigned    
            criteria.Criteria.change_non_numeric_criteria_current_value_by_index(current_criteria,int(user_choice) )
    os.system('cls')
    criteria_menu_screen()
    return
def criteria_screen_shortcuts():
    """"returns a list wich contains list of id's of criterias"""
    criteria_choices= []
    for crit in criteria.Criteria.criteria_db:
        criteria_choices.append(str(crit.id))
    return criteria_choices

def criteria_modification_screen(criteria):
    print_criteria_modification_screen(criteria)

def main_menu_shortcuts():
    """
    Returns the list of main menu shortcuts
    """
    main_menu_choices=["m","f","q"]
    return main_menu_choices
def update_possible_choices(current_menu_choices, items_to_add):
    """
    updates the current possible menu selection list with new items 
    if the new items are not in the list already
    param:
    current_menu_choices_list: menu selection shortcuts before this function was called (list)
    items_to_add: list of the shortcuts that will be added to menu selection list
    """
    for item in items_to_add:
        if len(current_menu_choices) == 0:
            current_menu_choices.append(item)
        else:
            if item not in current_menu_choices:
                current_menu_choices.append(item)
def get_user_choice(message):
    """Asks user's input choice and keeps asking until a valid input is entered
    returns it
    param:
    message: message which will be shown to user while asking for input
    
    """
    user_choice = input(message)
    
    return user_choice

def is_user_input_float(user_choice):
    
    try:
        float(user_choice)
        return True
    except ValueError:
        return False

def check_user_choice_validity(user_choice,current_menu_choices):
    if user_choice.lower() in current_menu_choices:
        return True
    else:
        return False
def initialize_program():
    """"
    initializes program by creating necessariy databases and prints welcome screen
    """
    shoe.Shoe.initialize_program_shoes("shoe_db.csv")
    criteria.Criteria.initialize_program_criterias()
    
    
    
def run_program():
    """
    all the program functionality runs through this function
    """
    os.system('cls')
    current_menu_choices = []
    initialize_program()
    print_welcome_screen()
    main_menu_screen(current_menu_choices)
        
    
    

    
    
    
    

#MAIN PROGRAM FUNCTIONS ENDS HERE

run_program()
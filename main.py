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

def print_criteria_menu_ingredient_line(criteria):
    """Takes a criteria as an input
    formats and prints it to screen as a menu item
    
    param: 
    current_menu_choices: possible choices before this function is called (list)
    criteria: criteria as criteria class
    """
    menu_line =[]
    menu_item = "[{0}] {1}".format(str(criteria.id),criteria.text.upper())
    menu_item_list = list(menu_item)
    for i in range(85):
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
        
    menu_line[-1]=":"

    
    print("".join(menu_line))
    
    

    
    
def print_welcome_screen():
    """prints the initial screen to terminal"""
    print_header("Running Shoe Advisor V1")
    
    
    
    

def print_main_menu():
    """
    prints main menu to the screen
    """
    print_header("Main Menu")
    print_header("[M] = Modify Criterias [F] = Find Shoes with current criterias [Q] = Quit Program")
    
    
    

def print_criteria_screen():
    """
    Prints CRTIERIA MODIFICATION menu to the secreen and ask user for an input
    returns the user input
    
    param:
    current_menu_choices: list of possible menu choices until this function is called
    """
    print_header("MODIFY CRITERIAS")
    print_current_criteria_selections()
    
    
     

def print_current_criteria_selections():
    """
    prints current possible choices List to the screen
    and modifies current_menu_choices list by adding current criterias' shortcuts
    
    param: 
    current_menu_choices: list of possible menu choices until this function is called
    """
    criteria_menu_choices = []
    print_header_lower("Here are the current Criteria Selections")
    for crit in criteria.Criteria.criteria_db:
        
        print_criteria_menu_ingredient_line(crit)
       
        
    

    


#PRINTING FUNCTIONS ENDS HERE



#MAIN PROGRAM FUNCTIONS STARTS HERE
def main_menu_screen(current_menu_choices):
    """
    All the operations related to main/opening screen is in this function
    """
    print_main_menu()
    update_possible_choices(current_menu_choices, main_menu_shortcuts())
     
def criteria_menu_screen():
    """
    All the operations related to criteria menu screen is here
    """
    current_menu_choices = []
    print_criteria_screen()
    print_main_menu()
    update_possible_choices(current_menu_choices, main_menu_shortcuts())
    update_possible_choices(current_menu_choices,criteria_screen_shortcuts())
    user_choice = get_user_choice("Please Enter The Shortcut of the item you are interested: ")
    while check_user_choice_validity(user_choice,current_menu_choices) == False:
        os.system('cls')
        user_choice = criteria_menu_screen()    
    return user_choice     
def criteria_screen_shortcuts():
    """"returns a list wich contains list of id's of criterias"""
    criteria_choices= []
    for crit in criteria.Criteria.criteria_db:
        criteria_choices.append(str(crit.id))
    return criteria_choices
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
    current_menu_choices: vurrent possible menu slection shortcuts
    print_funct(): function that calls this get_user_function
    """
    user_choice = input(message)
    
    return user_choice
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
    
    

    
    
    
    

#MAIN PROGRAM FUNCTIONS ENDS HERE

run_program()
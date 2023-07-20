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

def print_criteria_menu_ingredient_line(possible_choices, criteria):
    """Takes a message as a string input
    formats and prints it to screen as a menu item
    
    param: 
    possible_choices: possible choices before this function is called (list)
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

    possible_choices.append(str(criteria.id))
    print("".join(menu_line))
    
    

    
    
def print_welcome_screen():
    """prints the initial screen to terminal"""
    print_header("Running Shoe Advisor V1")
    possible_choices=print_main_menu()
    return possible_choices
    

def print_main_menu():
    """
    prints main menu to the screen
    """
    print_header("Main Menu")
    print_header("[M] = Modify Criterias [F] = Find Shoes with current criterias [Q] = Quit Program")
    possible_choices=["m","f","q"]
    return possible_choices

def print_modify_criterias_screen(possible_choices):
    print_header("MODIFY CRITERIAS")
    print_current_criteria_selections(possible_choices,criteria.Criteria.criteria_db)

def print_current_criteria_selections(possible_choices,criteria_db):
    """
    prints current possible choices List to the screen
    """

    print_header_lower("Here are the current Criteria Selections")
    for crit in criteria_db:
        
        print_criteria_menu_ingredient_line(possible_choices, crit)
        possible_choices.append(str(crit.id))
    possible_choices.append(print_main_menu())    
    

    


#PRINTING FUNCTIONS ENDS HERE



#MAIN PROGRAM FUNCTIONS STARTS HERE
def get_user_choice(message):
    """Asks user's input choice and returns it
    param:
    message: message which will be shown to user while asking for input
    """
    user_coice = input(message)
    return user_coice

def initialize_program():
    """"
    initializes program by creating necessariy databases and prints welcome screen
    """
    shoe.Shoe.initialize_program_shoes("shoe_db.csv")
    criteria_list=criteria.Criteria.initialize_program_criterias()
    
    possible_choices = print_welcome_screen()
    return possible_choices
def run_program():
    """
    all the program functionality runs through this function
    """
    os.system('cls')
    
    possible_choices = initialize_program()
    user_choice = get_user_choice("Please Select an option from the Main Menu items: ")
    if user_choice.lower() == "q":
        print("BYE, hope to see you again!")
        return
    if user_choice.lower() == "m":
        os.system('cls')
        print_modify_criterias_screen(possible_choices)
    if user_choice.lower() == "f":
        pass
    

    
    
    
    

#MAIN PROGRAM FUNCTIONS ENDS HERE

run_program()
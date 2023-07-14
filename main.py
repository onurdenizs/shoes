"""this will contain all the main functionalities and like running the main program and screen printing functions"""

import os
import criteria
import brand
import shoe
#PRINTING FUNCTIONS STARTS HERE
def print_welcome_screen():
    """This function  prints the initial screen to terminal"""
    
    message_width = 82
    welcome_string="Welcome to Running Shoe Adviser"
    white_spaces=" "
    line = "="
    for i in range(int((message_width+2-len(welcome_string))/2)):
        white_spaces += " "
    for i in range(message_width+2):
        line += "="
    print("{0}|{1}|{2}".format(white_spaces,welcome_string,white_spaces))
    print(line)
    
    

def print_main_menu():
    message_width = 82
    menu_string="Main Menu"
    white_spaces=" "
    line = "="
    for i in range(int((message_width+2-len(menu_string))/2)):
        white_spaces += " "
    for i in range(message_width+2):
        line += "="
    print("\n\n")
    print(line)
    print("{0}|{1}|{2}".format(white_spaces,menu_string,white_spaces))
    print(line)
    menu_string="[A] = Add/Change Criteria [F] = Find Shoes with current criterias [Q] = Quit Program"
    
    
    print(menu_string)
    print(line)
#PRINTING FUNCTIONS ENDS HERE



#MAIN PROGRAM FUNCTIONS STARTS HERE
def initialize_program():
    print("Initializing Program")
    criteria_list=criteria.Criteria.initialize_program_criterias()
    shoe.Shoe.initialize_program_shoes()

def run_program():
    os.system('cls')
    initialize_program()
    print_welcome_screen()
    print_main_menu()
    
    

#MAIN PROGRAM FUNCTIONS ENDS HERE

run_program()
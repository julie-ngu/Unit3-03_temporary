# Created by: Julie Nguyen
# Created on: Oct 2017
# Created for: ICS3U
# This program is a rock, paper, scissors game where the user is playing against the computer

import ui
from numpy import random

def see_results_button_touch_up_inside(sender):
    # shows user results of rock, paper, scissors game
    
    #input
    user_choice = view['rock_paper_scissors_segmented_control'].selected_index
    comp_number = random.randint(1, 3)
    
    # variables
    if comp_number == 1:
        comp_ans = "rock"
    elif comp_number == 2:
        comp_ans = "paper"
    elif comp_number == 3:
        comp_ans = "scissors"
    
    # process
    if user_choice == 0 and comp_number == 2:
        view['results_label'].text = "You lose!"
        view['computer_choice_label'].text = "The computer chose " + str(comp_ans) 
        if comp_number == 3:
            view['results_label'].text = "You win!"
            view['computer_choice_label'].text = "The computer chose " + str(comp_ans)
    elif user_choice == 1 and comp_number == 3:
        view['results_label'].text = "You lose!"
        view['computer_choice_label'].text = "The computer chose " + str(comp_ans)
        if comp_number == 1:
            view['results_label'].text = "You win!"
            view['computer_choice_label'].text = "The computer chose " + str(comp_ans)
    elif user_choice == 2 and comp_number == 3:
        view['results_label'].text = "You lose!"
        view['computer_choice_label'].text = "The computer chose " + str(comp_ans)
        if comp_number == 1:
            view['results_label'].text = "You win!"
            view['computer_choice_label'].text = "The computer chose " + str(comp_ans)
    elif user_choice == comp_number:
        view['results_label'].text = "It's a draw!"
        view['computer_choice_label'].text = "The computer chose " + str(comp_ans)

view = ui.load_view()
view.present('full_view')

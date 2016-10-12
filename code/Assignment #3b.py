# Created by: Hamza Salman
# Course: ICS3U
# Created: October 2016
# This program is used to calculate the cost of a large or an extra large pizza with 1-4 toppings and tax

import ui

# Constants
HST = 0.13
TAX = 1.13


number_of_toppings = 0
subtotal = 0
cost_of_pizza = 0

def large_touch_up_inside(sender):
    # This function gets input for number of toppings if size of pizza is large.
    global cost_of_pizza
    cost_of_pizza = 6
    global number_of_toppings
    number_of_toppings = int(view['toppings_textfield'].text)
    view['size_output_label'].text = 'Size of pizza : Large'
    if number_of_toppings < 4:
        number_of_toppings = number_of_toppings
    if number_of_toppings <= 0:
        view['error_label'].text = 'Sorry, We only sell upto 4 toppings!'
    elif number_of_toppings > 4:
        view['error_label'].text = 'Sorry, We only sell upto 4 toppings!'
    
def extra_large_touch_up_inside(sender):
    # This function gets input for number of toppings if size of pizza is extra large.
    global cost_of_pizza
    cost_of_pizza = 10
    global number_of_toppings
    number_of_toppings = int(view['toppings_textfield'].text)
    view['size_output_label'].text = 'Size of pizza : Extra Large'
    if number_of_toppings < 4:
        number_of_toppings = number_of_toppings
    if number_of_toppings <= 0:
        view['error_label'].text = 'Sorry, We only sell upto 4 toppings!'
    elif number_of_toppings > 4:
        view['error_label'].text = 'Sorry, We only sell upto 4 toppings!'

def calculate_touch_up_inside(sender):
# This function is used to calculate the hst, subtotal and total amount using the provided information
    if number_of_toppings <= 0:
        pass
    elif number_of_toppings >= 5:
        pass
    else:
        subtotal = (1 + number_of_toppings * 0.75 - 0.75) + cost_of_pizza
        total = subtotal * TAX
        hst = subtotal * HST
        view['subtotal_label'].text = 'subtotal: ' + '${:,.2f}'.format(subtotal);
        view['total_label'].text = 'total: ' + '${:,.2f}'.format(total);
        view['hst_label'].text = 'HST: ' + '${:,.2f}'.format(hst);


view = ui.load_view()
view.present('full_screen')


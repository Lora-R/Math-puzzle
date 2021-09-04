from tkinter import *
import random
import time
from threading import *
from tkinter import messagebox

list_entry_data_col = []
list_new = []

# list of numbers the player can use
list_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# shuffling the numbers every single game for new results
random.shuffle(list_numbers)
a, b, c, d, e, f, g, h, i = list_numbers[0], list_numbers[1], list_numbers[2], list_numbers[3], list_numbers[4], list_numbers[5], list_numbers[6], list_numbers[7], list_numbers[8]

# main logic for the results displayed on the screen
a_result = a * b + c
b_result = d + e * f
c_result = g + h + i

a_a = a * d + g
b_b = b + e * h
c_c = c - f + i

list_results = [a_result, b_result, c_result, a_a, b_b, c_c]
# list with the correct numbers in the game, which to compare with the players numbers
list_correct_nums = [a, b, c, d, e, f, g, h, i]
print(list_correct_nums)

def clear_view():
    # clear everything on the window
    for slave in tk.grid_slaves():
        slave.destroy()

def render_main_view():
    clear_view()
    # first page
    lbl = Label(tk, text="Solve the puzzle\n    "
                         "You can use the numbers from 1 to 9 just once to fill every single missing peace\n"
                         "Good luck!\n Please fill all the empty boxes!")
    lbl.grid(column=0, row=0)
    # Start button to start the game
    start_button = Button(tk, text="Start", height=1, width=7, bg="light green", command=render_create_view)
    start_button.grid(column=0, row=3, pady= 20)

def popup_won():
    global pop
    pop = Toplevel(tk)
    pop.title("Message")
    w = 250
    h = 200
    screen_w = pop.winfo_screenwidth()
    screen_h = pop.winfo_screenheight()
    x = (screen_w / 2) - (w / 2)
    y = (screen_h / 2) - (h / 2)

    # tk.geometry(f"{w}x{h}+{int(x)}+{int(y)}")
    pop.geometry(f"{w}x{h}+{int(x)}+{int(y)}")
    # popup which appears if the player solved the puzzle
    if list_new == list_correct_nums:
        pop.config(bg="green")
        pop_label = Label(pop, text="Evala! You won !\n Good job ! ! !")
        pop_label.grid(column=1, row=1, pady=50, padx=80)
        # new_game_button = Button(pop, text="New game", height=1, width=9, bg="light green", command=render_main_view)
        # new_game_button.grid(column=1, row=2)
        quit_button = Button(pop, text="Quit", height=1, width=7, bg="white", command=tk.quit)
        quit_button.grid(column=1, row=3)

    # popup which appears if the player Couldn't solve the puzzle
    else:
        pop.config(bg="red")
        pop_label = Label(pop, text=f"You couldn't solve the puzzle!\nYou can try again!\n \n *_*    *_*    *_*\n")
        pop_label.grid(column=1, row=1, pady=50, padx=45)
        # refresh_game_button = Button(pop, text="Try again", height=1, width=9, bg="light green", command=render_create_view)
        # refresh_game_button.grid(column=1, row=2)

def create_data(list_entry_data_col):
    list_new.clear()
    # to get the entry data
    for check in list_entry_data_col:
        num = check.get()
        list_new.append(int(num))
    print(list_new)
    print(list_correct_nums)
    # call function to check the answers from the player with the correct ones
    popup_won()

def timer():
    # timer logic
    sec = 600
    label = Label(tk, text="10:00")
    label.grid(column=5, row=0, padx=10, pady=10)
    while sec:
        mins = sec // 60
        second = sec % 60
        label.config(text=f"{mins}:{second}", font=("calibri", 14, 'bold'), bg="white")
        time.sleep(1)
        sec -= 1
        # the timer will stop if the player solve the puzzle
        if list_new == list_correct_nums:
            break
        else:
            continue

    # when the time finish the player will receive error message
    if sec == 0:
        messagebox.showerror("Error Message", "Time is Up")
        tk.quit()

def render_create_view():
    clear_view()
    start_index = -1
    list_entry_data_col = []
    list_new = []

    # start the timer
    t1 = Thread(target=timer)
    t1.start()

    # list with the operators
    list_symbols = ["*", "+", "*", " ", "+", " ", "-", "+", "*", "+", " ", "*", " ", "+", "+", "+"]
    # loops to visualize the empty boxes for entries/where the layer writes his numbers to solve the puzzle
    for row in range(1, 6):
        if row % 2 != 0:
            enter_data = Entry(tk, width=6)
            enter_data.grid(column=3, row=row, pady=3, padx=3)

        for col in range(3, 8):
            if col % 2 != 0 and row % 2 != 0:
                enter_data = Entry(tk, width=6)
                enter_data.grid(column=col, row=row, pady=3, padx=3)
                list_entry_data_col.append(enter_data)
            if col % 2 == 0 or row % 2 == 0:
                start_index = start_index + 1
                symbol = Label(tk, text=list_symbols[start_index])
                symbol.grid(column=col, row=row, pady=1, padx=1)
                if col % 2 == 0 and row % 2 == 0:
                    symbol = Label(tk, text=" ")
                    symbol.grid(column=col, row=row, pady=1, padx=1)

    start_result_index = -1
    for equal_row in range(1, 7):
        for equal_col in range(9, 11):
            if equal_col % 2 != 0 and equal_row % 2 != 0:
                equal_label = Label(tk, text="=").grid(column=equal_col, row=equal_row, pady=1, padx=1)
            elif equal_col % 2 == 0 and equal_row % 2 != 0:
                start_result_index = start_result_index + 1
                result = Label(tk, text=list_results[start_result_index])
                result.grid(column=equal_col, row=equal_row, pady=1, padx=1)

    for equal_col in range(3, 8):
        for equal_row in range(7, 9):
            if equal_row % 2 != 0 and equal_col % 2 != 0:
                equal_label = Label(tk, text="=")
                equal_label.grid(column=equal_col, row=equal_row, pady=1, padx=1)
            elif equal_row % 2 == 0 and equal_col % 2 != 0:
                start_result_index = start_result_index + 1
                result = Label(tk, text=list_results[start_result_index])
                result.grid(column=equal_col, row=equal_row, pady=1, padx=1)

    # button => calls function which get the information from the entry boxes
    done_button = Button(tk, text="Done", height=2, width=8, bg="light blue", command=lambda: create_data(list_entry_data_col))
    done_button.grid(column=11, row=15, padx=10, pady=20)

    refresh_game_button = Button(tk, text="Quit\n game", height=2, width=8, bg="white", command=tk.quit)
    refresh_game_button.grid(column=0, row=15, padx=30, pady=20)
    # quit_button = Button(tk, text="Quit", height=1, width=7, bg="white", command=tk.quit)
    # quit_button.grid(column=0, row=19)

    print(list_entry_data_col)

if __name__=='__main__':
    # main visualization
    tk = Tk()
    tk.title("Math puzzle")
    w = 450
    h = 300
    screen_w = tk.winfo_screenwidth()
    screen_h = tk.winfo_screenheight()
    x = (screen_w / 2) - (w / 2)
    y = (screen_h / 2) - (h / 2)

    tk.geometry(f"{w}x{h}+{int(x)}+{int(y)}")
    # => the function with explanation and "Start" button
    render_main_view()
    # loop to keep the window visible
    tk.mainloop()


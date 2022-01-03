from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
TEST_MIN = 0.1

symbols_sum = 0
words_sum = 0

window = Tk()
window.title("Speed test")
window.config(padx=50, pady=50, bg=YELLOW)
window.minsize(300, 300)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def result(text_typed):
    global symbols_sum
    global words_sum
    for num in range(len(text_typed)):
        if text[num] == text_typed[num]:
            symbols_sum +=1
            if text[num] == ' ':
                words_sum += 1
    result_symbols.config(text=f"Correct CPM: {symbols_sum}")
    result_words.config(text=f"Words per minute: {words_sum}")


def count_down(count):
    if count > 0:
        window.after(1000, count_down, count - 1)
    else:
        result_label.config(text=f"All symbols per minute = {input_text.count('1.0', END)[0]}")
        text_typed = input_text.get('1.0', END)
        result(text_typed)
        input_text.config(bg='red', state=DISABLED)

def reset():
    global symbols_sum
    global words_sum
    input_text.config(bg='white', state=NORMAL)
    symbols_sum = 0
    words_sum = 0
    input_text.delete('1.0', END)
    result_label.config(text=f"All symbols per minute = 0")
    result_symbols.config(text=f"Correct CPM: {symbols_sum}")
    result_words.config(text=f"Words per minute: {words_sum}")
    count_down(TEST_MIN * 60)


# ---------------------------- UI SETUP ------------------------------- #

text = "In the coming months, we're planning a number of additions to the course. \n" \
       "Course updates and text to video lesson conversions are on the way. \n" \
       "We're also looking to employ a number of students who have completed \n" \
       "the course to work on improving the course. We'll finalise the job spec \n" \
       "and hiring requirements in the coming weeks, but most importantly we want \n" \
       "to hire a group of people who have completed our Python and Web courses. "

text_label = Label(text=text, font=(FONT_NAME, 12, "bold"), bg=YELLOW, fg="black")
text_label.grid(column=0, row=0)

input_text = Text(width=70, height=6, takefocus=True)
input_text.grid(column=0, row=1)

result_label = Label(text='All symbols per minute = 0', font=(FONT_NAME, 12, "bold"), bg=YELLOW, fg="black")
result_label.grid(column=0, row=3)

result_symbols = Label(text=f"Correct CPM: {symbols_sum}", font=(FONT_NAME, 12, "bold"), bg=YELLOW, fg="black")
result_symbols.grid(column=0, row=4)

result_words = Label(text=f"Words per minute: {words_sum}", font=(FONT_NAME, 12, "bold"), bg=YELLOW, fg="black")
result_words.grid(column=0, row=5)

my_button = Button(text='Reset', command=reset)
my_button.grid(column=0, row=6)

starting = False
while not starting:
    input_text.update()
    starting = input_text.edit_modified()

count_down(TEST_MIN * 60)

window.mainloop()

from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 10
LONG_BREAK_MIN = 30
timer = None
reps = 0


# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    global timer
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer")
    check_marks.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps, RED, GREEN, PINK
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60
    if reps % 2 != 0 and reps < 8:
        counter(work_sec)
        timer_label.config(text="Work Time", fg=GREEN)
    elif reps % 2 == 0 and reps < 8:
        counter(short_break_sec)
        timer_label.config(text="Break Time", fg=PINK)
    elif reps == 8:
        counter(long_break)
        timer_label.config(text="Leisure Time", fg=RED)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def counter(count):
    global timer
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec == 0:
        count_sec = "00"
    elif len(str(count_sec)) == 1:
        count_sec = "0" + str(count_sec)
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, counter, count - 1)
    else:
        start_timer()
        mark = ""
        for i in range(math.floor(reps / 2)):
            mark += "✔"
            check_marks.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro App")
window.config(padx=100, pady=69, bg=YELLOW)

fg = GREEN
check_marks = Label(fg=fg, bg=YELLOW, highlightthickness=0)
check_marks.grid(column=1, row=3)
timer_label = Label(text="Timer", fg=fg, font=("Comic Sans Fonts", 20, "bold"), bg=YELLOW, highlightthickness=0)
timer_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill='white', font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)
reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

window.mainloop()

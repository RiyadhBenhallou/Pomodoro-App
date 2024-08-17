import tkinter as tk

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
marks = ''
timer_counter = ''

# ---------------------------- TIMER RESET ------------------------------- # 
def restart_timer():
  global marks, reps
  window.after_cancel(timer_counter)
  canvas.itemconfig(timer, text='00:00')
  title.config(text='Timer', font=(FONT_NAME, 24, 'bold'), bg=YELLOW, fg=GREEN)
  check.config(text='')
  reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
  global reps
  reps += 1
  if reps % 8 == 0:
    countdown(LONG_BREAK_MIN * 60)
    title.config(text='Break', fg=RED)
  elif reps % 2 == 0:
    countdown(SHORT_BREAK_MIN * 60)
    title.config(text='Break', fg=PINK)
  else:
    countdown(WORK_MIN * 60)
    title.config(text='WORK', fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
  global reps, marks, timer_counter
  mins = count // 60
  if mins < 10:
    mins = f'0{mins}'
  secs = count % 60
  if secs < 10:
    secs = f'0{secs}'
  canvas.itemconfig(timer, text=f'{mins}:{secs}')
  if count > 0:
    timer_counter = window.after(1000, countdown, count-1)
  else:
    start_timer()
    if reps % 2 == 0:
      marks += '✔'
      check.config(text=marks)
      
# ---------------------------- UI SETUP ------------------------------- #


window = tk.Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)





tomato_image = tk.PhotoImage(file='tomato.png')

# Canvas Setup
canvas = tk.Canvas(width=200, height=244, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=tomato_image)
timer = canvas.create_text(100, 130, text='00:00', font=(FONT_NAME, 28, 'bold'), fill='white')
canvas.grid(column=1, row=1)

title = tk.Label(text='Timer', font=(FONT_NAME, 24, 'bold'), bg=YELLOW, fg=GREEN)
title.grid(column=1, row=0)

# Buttons Setup
start = tk.Button(text='Start', highlightthickness=0, command=start_timer)
start.grid(column=0, row=2)

restart = tk.Button(text='Restart', highlightthickness=0, command=restart_timer)
restart.grid(column=2, row=2)

check = tk.Label(fg=GREEN, bg=YELLOW, font=('Arial', 24, 'bold'))
check.grid(column=1, row=3)





window.mainloop()
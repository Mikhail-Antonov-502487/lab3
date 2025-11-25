import tkinter as tk
import random
import pygame


def change_color():
    st_color = "#{:06x}".format(random.randint(0, 0xFFFFFF))
    end_color = "#{:06x}".format(random.randint(0, 0xFFFFFF))
    r1 = int(st_color[1:3], 16)
    g1 = int(st_color[3:5], 16)
    b1 = int(st_color[5:7], 16)

    r2 = int(end_color[1:3], 16)
    g2 = int(end_color[3:5], 16)
    b2 = int(end_color[5:7], 16)

    ST = 30
    for i in range(ST + 1):
        r = int(r1 + (r2 - r1) * i / ST)
        g = int(g1 + (g2 - g1) * i / ST)
        b = int(b1 + (b2 - b1) * i / ST)
        inter_color = f"#{r:02x}{g:02x}{b:02x}"

        gen_but.config(bg=inter_color)

        window.update()
        window.after(50)

    window.after(100, change_color)

def gen_key():
    s = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    word_input = input_entry.get().strip().upper()
    if len(word_input) != 6 or not all(c in s for c in word_input):
        key_entry.delete(0, tk.END)
        key_entry.insert(0, "False (6 items)")
        return
    first_3 = word_input[:3]
    last_3 = word_input[-3:]
    x = ''
    for i in range(len(word_input)):
        x += str((s.find(word_input[i])+1)%10)
    key = f"{''.join(random.choices(first_3, k=3))}-" \
          f"{x}-" \
          f"{''.join(random.choices(last_3, k=3))}"
    key_entry.delete(0, tk.END)
    key_entry.insert(0, key)

def close_app():
    window.destroy()

def play_music():
    pygame.mixer.init()
    pygame.mixer.music.load("abracadabra.mp3")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)

play_music()

window = tk.Tk()
window.title("Keygen")
window.geometry("1024x768")

bg_img = tk.PhotoImage(file="game_screen.png")

lbl_bg = tk.Label(window, image=bg_img)
lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)

frame = tk.Frame(window, bg="lightblue", bd=5)
frame.place(relx=0.5, rely=0.5, anchor="center")

input_label = tk.Label(frame, text="Input word:", font=("Verdana", 12),
                       bg="lightblue")
input_label.grid(row=0, column=0, padx=10, pady=5)
input_entry = tk.Entry(frame, width=20, font=("Verdana", 12))
input_entry.grid(row=0, column=1, padx=10, pady=5)

key_label = tk.Label(frame, text="Get a key:", font=("Verdana", 12),
                    bg="lightblue" )
key_label.grid(row=1, column=0, padx=10, pady=5)
key_entry = tk.Entry(frame, width=25, font=("Verdana", 12))
key_entry.grid(row=1, column=1, padx=10, pady=5)

gen_but = tk.Button(frame, text="Generate key", font=("Verdana", 10), 
                    command=gen_key)
gen_but.grid(row=2, column=0, columnspan=2, pady=10)

exit_but = tk.Button(window, text="Exit", font=("Verdana", 10), 
                     command=close_app)
exit_but.place(relx=0.85, rely=0.9, anchor="center")

change_color()

window.mainloop()


import tkinter as tk
import random
class Kartya:
  
  def __init__(self):
    mylist = ["ut", "mezo", "varos"]
    self.bal = random.choices(mylist, weights = [1, 1, 1], k = 1)
    self.fent = random.choices(mylist, weights = [1, 1, 1], k = 1)
    self.jobb = random.choices(mylist, weights = [1, 1, 1], k = 1)
    self.lent = random.choices(mylist, weights = [1, 1, 1], k = 1)

  def forgat(self):
    tmp=self.bal
    self.bal=self.fent
    self.fent=self.jobb
    self.jobb=self.lent
    self.lent=tmp

    

kartyalist=[]
k1 = Kartya()
print(k1.bal, k1.fent,k1.jobb,k1.lent)
k1.forgat()
print(k1.bal, k1.fent,k1.jobb,k1.lent)

def draw_cube(canvas, x, y, size, value):
    canvas.create_rectangle(x, y, x+size, y+size, fill="white")  # Fehér négyzet rajzolása
    canvas.create_text(x+size/2, y+size/2, text=str(value))  # Szöveg megjelenítése a négyzet közepén

def update_matrix(event):
    global matrix
    if event.char == 'w':
        matrix[0][0] = "Szia"
        draw_matrix(canvas, size, matrix)
    if event.char == 'r':
        matrix[2][1]=matrix[1][2]
        matrix[1][2]=matrix[2][3]
        matrix[2][3]=matrix[3][2]
        matrix[3][2]=matrix[2][1]
        draw_matrix(canvas, size, matrix)

def draw_matrix(canvas, size, matrix):
    for i in range(5):
        for j in range(5):
            x = j * size
            y = i * size
            draw_cube(canvas, x, y, size, matrix[i][j])

# Üres 5x5 méretű mátrix létrehozása, és a 0,0 indexű elem beállítása "Hello" értékre
matrix = [[None for _ in range(5)] for _ in range(5)]
matrix[0][0] = "Hello"
matrix[1][2] = k1.fent
matrix[2][1] = k1.bal
matrix[2][3] = k1.jobb
matrix[3][2] = k1.lent
matrix[0][1] = ("")
matrix[0][2] = ("")
matrix[0][3] = ("")
matrix[0][4] = ("")
matrix[1][1] = ("")
matrix[1][0] = ("")
matrix[1][3] = ("")
matrix[1][4] = ("")
matrix[2][0] = ("")
matrix[2][2] = ("Pygame")
matrix[2][4] = ("")
matrix[3][0] = ("")
matrix[3][1] = ("")
matrix[3][3] = ("")
matrix[3][4] = ("")
matrix[4][0] = ("")
matrix[4][1] = ("")
matrix[4][2] = ("")
matrix[4][3] = ("")
matrix[4][4] = ("")

# Ablak létrehozása és konfigurálása
root = tk.Tk()
root.title("Matrix")
root.geometry("300x300")

# Vászon létrehozása és konfigurálása
canvas = tk.Canvas(root, width=250, height=250, bg="gray")
canvas.pack(side="top", padx=25, pady=25)

# A mátrix négyzeteinek rajzolása a vászonra
size = 50
draw_matrix(canvas, size, matrix)

# Billentyűesemények figyelése
root.bind("<Key>", update_matrix)

# Az ablak megjelenítése
root.mainloop()
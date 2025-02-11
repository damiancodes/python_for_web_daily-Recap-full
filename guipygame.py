import tkinter as tk
import random
import pygame
import os

# Initialize pygame mixer for sound effects
pygame.init()
pygame.mixer.init()

# Get the base directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
point_sound_path = os.path.join(BASE_DIR, "point.wav")
collision_sound_path = os.path.join(BASE_DIR, "collision.wav")
background_path = os.path.join(BASE_DIR, "background.png")

# Load sound files safely
if os.path.exists(point_sound_path) and os.path.exists(collision_sound_path):
    point_sound = pygame.mixer.Sound(point_sound_path)
    collision_sound = pygame.mixer.Sound(collision_sound_path)
else:
    print("Warning: Sound files missing! Ensure 'point.wav' and 'collision.wav' exist in the directory.")
    point_sound = None
    collision_sound = None

# Game Constants
WIDTH, HEIGHT = 500, 500
PLAYER_SIZE = 20
OBSTACLE_SIZE = 30
POINT_SIZE = 15
SPEED = 10
OBSTACLE_SPEED = 5


class Game:
    def __init__(self, root):
        self.root = root
        self.root.title("Exciting GUI Game")

        self.canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg='black')
        self.canvas.pack()

        if os.path.exists(background_path):
            self.background = tk.PhotoImage(file=background_path)
            self.canvas.create_image(0, 0, anchor=tk.NW, image=self.background)
        else:
            print("Warning: 'background.png' is missing. Running with a plain background.")

        self.player = self.canvas.create_oval(WIDTH // 2, HEIGHT // 2, WIDTH // 2 + PLAYER_SIZE,
                                              HEIGHT // 2 + PLAYER_SIZE, fill='blue', outline='white')
        self.point = self.create_point()
        self.obstacle = self.create_obstacle()

        self.score = 0
        self.score_label = tk.Label(root, text=f"Score: {self.score}", fg='white', bg='black', font=('Arial', 16))
        self.score_label.pack()

        self.root.bind("<KeyPress>", self.move_player)
        self.update_obstacle()

    def create_point(self):
        x, y = random.randint(0, WIDTH - POINT_SIZE), random.randint(0, HEIGHT - POINT_SIZE)
        return self.canvas.create_oval(x, y, x + POINT_SIZE, y + POINT_SIZE, fill='gold', outline='white')

    def create_obstacle(self):
        x, y = random.randint(0, WIDTH - OBSTACLE_SIZE), random.randint(0, HEIGHT - OBSTACLE_SIZE)
        return self.canvas.create_rectangle(x, y, x + OBSTACLE_SIZE, y + OBSTACLE_SIZE, fill='red', outline='black')

    def move_player(self, event):
        x1, y1, x2, y2 = self.canvas.coords(self.player)
        if event.keysym == 'Up' and y1 > 0:
            self.canvas.move(self.player, 0, -SPEED)
        elif event.keysym == 'Down' and y2 < HEIGHT:
            self.canvas.move(self.player, 0, SPEED)
        elif event.keysym == 'Left' and x1 > 0:
            self.canvas.move(self.player, -SPEED, 0)
        elif event.keysym == 'Right' and x2 < WIDTH:
            self.canvas.move(self.player, SPEED, 0)

        self.check_collision()

    def check_collision(self):
        px1, py1, px2, py2 = self.canvas.coords(self.player)
        ox1, oy1, ox2, oy2 = self.canvas.coords(self.obstacle)
        tx1, ty1, tx2, ty2 = self.canvas.coords(self.point)

        if px1 < tx2 and px2 > tx1 and py1 < ty2 and py2 > ty1:
            if point_sound:
                pygame.mixer.Sound.play(point_sound)
            self.canvas.delete(self.point)
            self.point = self.create_point()
            self.score += 1
            self.score_label.config(text=f"Score: {self.score}")

        if px1 < ox2 and px2 > ox1 and py1 < oy2 and py2 > oy1:
            if collision_sound:
                pygame.mixer.Sound.play(collision_sound)
            self.canvas.create_text(WIDTH // 2, HEIGHT // 2, text="Game Over!", fill="white", font=('Arial', 24))
            self.root.unbind("<KeyPress>")

    def update_obstacle(self):
        x_move = random.choice([-OBSTACLE_SPEED, OBSTACLE_SPEED])
        y_move = random.choice([-OBSTACLE_SPEED, OBSTACLE_SPEED])
        self.canvas.move(self.obstacle, x_move, y_move)
        self.root.after(300, self.update_obstacle)


if __name__ == "__main__":
    root = tk.Tk()
    game = Game(root)
    root.mainloop()

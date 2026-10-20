import random
import tkinter as tk


CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
SIZE = 20
DELAY = 180
GRID_WIDTH = CANVAS_WIDTH // SIZE
GRID_HEIGHT = CANVAS_HEIGHT // SIZE


class SnakeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Snake")
        self.canvas = tk.Canvas(
            root,
            width=CANVAS_WIDTH,
            height=CANVAS_HEIGHT,
            background="white",
            highlightthickness=0,
        )
        self.canvas.pack()
        self.canvas.bind("<Button-1>", self.handle_click)
        self.root.bind("<Left>", lambda event: self.set_direction((-1, 0)))
        self.root.bind("<Right>", lambda event: self.set_direction((1, 0)))
        self.root.bind("<Up>", lambda event: self.set_direction((0, -1)))
        self.root.bind("<Down>", lambda event: self.set_direction((0, 1)))

        self.state = "waiting"
        self.draw_message("Click to Start!")

    def draw_message(self, message):
        self.canvas.delete("all")
        self.canvas.create_text(
            CANVAS_WIDTH / 2,
            CANVAS_HEIGHT / 2,
            text=message,
            font=("Courier New", 24),
            fill="black",
            justify="center",
        )

    def handle_click(self, _event):
        if self.state in ("waiting", "game_over"):
            self.start_game()

    def start_game(self):
        self.state = "playing"
        self.snake = [(5, 10)]
        self.direction = (1, 0)
        self.next_direction = self.direction
        self.score = 0
        self.food = self.spawn_food()
        self.draw_game()
        self.root.after(DELAY, self.update)

    def set_direction(self, direction):
        if self.state != "playing":
            return
        if direction != (-self.direction[0], -self.direction[1]):
            self.next_direction = direction

    def spawn_food(self):
        occupied = set(self.snake)
        available = [
            (x, y)
            for x in range(GRID_WIDTH)
            for y in range(GRID_HEIGHT)
            if (x, y) not in occupied
        ]
        return random.choice(available) if available else None

    def draw_game(self):
        self.canvas.delete("all")
        if self.food is not None:
            self.draw_cell(self.food, "red")
        for cell in self.snake:
            self.draw_cell(cell, "light blue")
        self.canvas.create_text(
            8,
            8,
            anchor="nw",
            text=f"Score: {self.score}",
            font=("Courier New", 12),
            fill="black",
        )

    def draw_cell(self, cell, color):
        x, y = cell
        self.canvas.create_rectangle(
            x * SIZE,
            y * SIZE,
            (x + 1) * SIZE,
            (y + 1) * SIZE,
            fill=color,
            outline="white",
        )

    def update(self):
        if self.state != "playing":
            return

        self.direction = self.next_direction
        head_x, head_y = self.snake[-1]
        new_head = (
            head_x + self.direction[0],
            head_y + self.direction[1],
        )
        ate_food = new_head == self.food

        if not (0 <= new_head[0] < GRID_WIDTH and 0 <= new_head[1] < GRID_HEIGHT):
            self.end_game("Game over! You hit a wall.")
            return

        body_to_check = self.snake if ate_food else self.snake[1:]
        if new_head in body_to_check:
            self.end_game("Game over! You bit your tail.")
            return

        self.snake.append(new_head)
        if ate_food:
            self.score += 1
            print("Yum! Snake length:", len(self.snake))
            self.food = self.spawn_food()
            if self.food is None:
                self.end_game("You win! Click to play again.")
                return
        else:
            self.snake.pop(0)

        self.draw_game()
        self.root.after(DELAY, self.update)

    def end_game(self, message):
        self.state = "game_over"
        print(message)
        self.draw_game()
        self.canvas.create_text(
            CANVAS_WIDTH / 2,
            CANVAS_HEIGHT / 2,
            text=f"{message}\nClick to play again",
            font=("Courier New", 18),
            fill="black",
            justify="center",
        )


def main():
    root = tk.Tk()
    SnakeGame(root)
    root.mainloop()


if __name__ == "__main__":
    main()

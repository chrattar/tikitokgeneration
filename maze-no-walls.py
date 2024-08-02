import pygame
import numpy as np
import random
import time

# Initialize pygame
pygame.init()

# Screen dimensions
width, height = 21, 21
cell_size = 20
screen = pygame.display.set_mode((width * cell_size, height * cell_size))
pygame.display.set_caption("Maze Generation")

# Colors
wall_color = (0, 0, 0)         # Black
path_color = (255, 255, 255)   # White
bg_color = (200, 200, 200)     # Light gray
active_cell_color = (255, 0, 0)  # Red

# Maze generation using DFS
def generate_maze(width, height, draw_speed=0.02):
    maze = np.ones((height, width), dtype=bool)
    stack = []
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def is_valid_move(x, y):
        return 0 <= x < width and 0 <= y < height and maze[y, x]

    def dfs(x, y):
        stack.append((x, y))
        maze[y, x] = False
        draw_maze(maze, x, y, draw_speed)
        while stack:
            x, y = stack[-1]
            neighbors = [(x + dx, y + dy) for dx, dy in directions if is_valid_move(x + dx, y + dy)]
            if neighbors:
                nx, ny = random.choice(neighbors)
                maze[(y + ny) // 2, (x + nx) // 2] = False
                maze[ny, nx] = False
                stack.append((nx, ny))
                draw_maze(maze, nx, ny, draw_speed)
            else:
                stack.pop()
    dfs(1, 1)
    return maze

# Draw maze
def draw_maze(maze, cx, cy, draw_speed):
    screen.fill(bg_color)  # Fill the screen with background color
    for y in range(height):
        for x in range(width):
            color = path_color if not maze[y, x] else wall_color
            pygame.draw.rect(screen, color, (x * cell_size, y * cell_size, cell_size, cell_size))
    # Highlight the current cell
    if cx >= 0 and cy >= 0:
        pygame.draw.rect(screen, active_cell_color, (cx * cell_size, cy * cell_size, cell_size, cell_size))
    pygame.display.flip()
    time.sleep(draw_speed)

# Main function
def main():
    draw_speed = 0.02  # Adjust the speed of drawing
    maze = generate_maze(width, height, draw_speed)
    draw_maze(maze, -1, -1, 0)  # Final draw without highlighting the current cell
    # Wait for user to close the window
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    pygame.quit()

if __name__ == "__main__":
    main()

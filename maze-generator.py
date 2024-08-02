import pygame
import numpy as np
import random
import time
import os

# Initialize pygame
pygame.init()

# Screen dimensions and maze sizing criteria
width, height = 51, 51
cell_size = 10
wall_thickness = 2
screen = pygame.display.set_mode((width * cell_size + (width + 1) * wall_thickness,
                                  height * cell_size + (height + 1) * wall_thickness))
pygame.display.set_caption("Maze Generation")

# Colors
wall_color = (0, 0, 0)         # Black
path_color = (255, 255, 255)   # White
bg_color = (200, 200, 200)     # Light gray
active_cell_color = (255, 0, 0)  # Red

# Frame folder for saving images
frame_folder = "frames"
if not os.path.exists(frame_folder):
    os.makedirs(frame_folder)
frame_count = 0

# Depth first Search -- Generate Maze
def generate_maze(width, height, draw_speed=0.02):
    maze = np.ones((height, width), dtype=bool)
    stack = []
    directions = [(0, 2), (2, 0), (0, -2), (-2, 0)]

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

# Draw maze and save each frame
def draw_maze(maze, cx, cy, draw_speed):
    global frame_count
    screen.fill(wall_color)  # Fill the screen with wall color
    for y in range(height):
        for x in range(width):
            if not maze[y, x]:
                color = path_color
                rect = pygame.Rect(x * (cell_size + wall_thickness) + wall_thickness,
                                   y * (cell_size + wall_thickness) + wall_thickness,
                                   cell_size, cell_size)
                pygame.draw.rect(screen, color, rect)
    # Tracking Current Cell
    if cx >= 0 and cy >= 0:
        rect = pygame.Rect(cx * (cell_size + wall_thickness) + wall_thickness,
                           cy * (cell_size + wall_thickness) + wall_thickness,
                           cell_size, cell_size)
        pygame.draw.rect(screen, active_cell_color, rect)
    pygame.display.flip()
    # Save the current frame
    pygame.image.save(screen, os.path.join(frame_folder, f"frame_{frame_count:04d}.png"))
    frame_count += 1
    time.sleep(draw_speed)

### MAIN
def main():
    draw_speed = 0.02  # Render drawing speed
    maze = generate_maze(width, height, draw_speed)
    draw_maze(maze, -1, -1, 0)  # Last drawing scene
    # USER WILL END
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    pygame.quit()

if __name__ == "__main__":
    main()

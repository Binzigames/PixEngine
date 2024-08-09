import pygame
import sys
import data

ScreenX = data.ScreenX
ScreenY = data.ScreenY

Screen = pygame.display.set_mode((ScreenX, ScreenY))
pygame.display.set_caption(data.GameName + " Made by PixEngine")
running = True

def draw_map():
    cell_size = data.cell_size
    map_data = data.Map
    if not isinstance(map_data, list):
        print("Map data is not a list!")
        return

    for y in range(len(map_data)):
        if not isinstance(map_data[y], list):
            print(f"Row {y} is not a list!")
            continue

        for x in range(len(map_data[y])):
            pos_x = x * cell_size
            pos_y = y * cell_size

            if map_data[y][x] == 1:
                pygame.draw.rect(Screen, data.grass, (pos_x, pos_y, cell_size, cell_size))
            else:
                pygame.draw.rect(Screen, (0, 0, 0), (pos_x, pos_y, cell_size, cell_size))

map_data = data.Map
PlayerPos = None

for y in range(len(map_data)):
    for x in range(len(map_data[y])):
        if map_data[y][x] == 2:
            PlayerPos = (x, y)
            break
    if PlayerPos is not None:
        break

if PlayerPos is not None:
    data.player_pos = [PlayerPos[0] * data.cell_size, PlayerPos[1] * data.cell_size]
else:
    print("Гравець не знайдений на карті.")

player_pos = data.player_pos
player_speed = data.player_speed
player_size = data.player_size
player_colour = data.player_color

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and player_pos[0] > 0:
        player_pos[0] -= player_speed
    if keys[pygame.K_RIGHT] and player_pos[0] < ScreenX - player_size:
        player_pos[0] += player_speed
    if keys[pygame.K_UP] and player_pos[1] > 0:
        player_pos[1] -= player_speed
    if keys[pygame.K_DOWN] and player_pos[1] < ScreenY - player_size:
        player_pos[1] += player_speed

    Screen.fill((0, 0, 0))
    draw_map()
    pygame.draw.rect(Screen, player_colour, (player_pos[0], player_pos[1], player_size, player_size))

    pygame.display.flip()
pygame.quit()
sys.exit()

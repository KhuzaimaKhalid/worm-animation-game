import pygame
import math

# Initialize pygame
pygame.init()
screen = pygame.display.set_mode((700, 400))
pygame.display.set_caption("Worm Follows Cursor")
clock = pygame.time.Clock()

# Worm parameters
SEGMENTS = 30
LENGTH = 12
worm = []
for i in range(SEGMENTS):
    # Start worm straight at center
    worm.append([screen.get_width() // 2 - i * LENGTH, screen.get_height() // 2])

def draw_worm(surface, worm):
    for i in range(len(worm) - 1):
        x, y = worm[i]
        nx, ny = worm[i + 1]
        pygame.draw.line(surface, (255, 255, 255), (x, y), (nx, ny), 2)
        # Draw legs
        angle = math.atan2(ny - y, nx - x)
        leg_len = 6
        leg_angle = math.pi / 2
        leg1_x = x + int(leg_len * math.cos(angle + leg_angle))
        leg1_y = y + int(leg_len * math.sin(angle + leg_angle))
        leg2_x = x + int(leg_len * math.cos(angle - leg_angle))
        leg2_y = y + int(leg_len * math.sin(angle - leg_angle))
        pygame.draw.line(surface, (255, 255, 255), (x, y), (leg1_x, leg1_y), 1)
        pygame.draw.line(surface, (255, 255, 255), (x, y), (leg2_x, leg2_y), 1)

def update_worm(worm, target):
    # Move head toward mouse
    hx, hy = worm[0]
    tx, ty = target
    angle = math.atan2(ty - hy, tx - hx)
    hx += math.cos(angle) * LENGTH
    hy += math.sin(angle) * LENGTH
    worm[0][0], worm[0][1] = hx, hy
    # Each segment follows the previous one
    for i in range(1, len(worm)):
        px, py = worm[i-1]
        cx, cy = worm[i]
        angle = math.atan2(py - cy, px - cx)
        cx = px - math.cos(angle) * LENGTH
        cy = py - math.sin(angle) * LENGTH
        worm[i][0], worm[i][1] = cx, cy

def draw_mouse_status(surface, left, middle, right):
    font = pygame.font.SysFont(None, 24)
    text = f"Left: {left}  Middle: {middle}  Right: {right}"
    img = font.render(text, True, (0, 255, 0))
    surface.blit(img, (20, 20))

mouse_left = False
mouse_middle = False
mouse_right = False

running = True
while running:
    screen.fill((0, 0, 0))
    # Follow mouse
    mx, my = pygame.mouse.get_pos()
    update_worm(worm, (mx, my))
    draw_worm(screen, worm)
    draw_mouse_status(screen, mouse_left, mouse_middle, mouse_right)
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_left = True
            elif event.button == 2:
                mouse_middle = True
            elif event.button == 3:
                mouse_right = True
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                mouse_left = False
            elif event.button == 2:
                mouse_middle = False
            elif event.button == 3:
                mouse_right = False

    clock.tick(60)

pygame.quit()
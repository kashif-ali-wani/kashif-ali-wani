import pygame
import pygame_gui
import math
import random

pygame.init()

# Window
WIDTH, HEIGHT = 1200, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Advanced Double Pendulum Simulation (Glow + Trails + Controls)")

clock = pygame.time.Clock()

# UI Manager
manager = pygame_gui.UIManager((WIDTH, HEIGHT))

# ======== UI CONTROLS ===========
ui_panel = pygame.Rect(WIDTH - 300, 0, 300, HEIGHT)

mass1_slider = pygame_gui.elements.UIHorizontalSlider(
    relative_rect=pygame.Rect(WIDTH - 280, 40, 260, 20),
    start_value=20,
    value_range=(5, 80),
    manager=manager,
)

mass2_slider = pygame_gui.elements.UIHorizontalSlider(
    relative_rect=pygame.Rect(WIDTH - 280, 80, 260, 20),
    start_value=20,
    value_range=(5, 80),
    manager=manager,
)

len1_slider = pygame_gui.elements.UIHorizontalSlider(
    relative_rect=pygame.Rect(WIDTH - 280, 120, 260, 20),
    start_value=200,
    value_range=(50, 350),
    manager=manager,
)

len2_slider = pygame_gui.elements.UIHorizontalSlider(
    relative_rect=pygame.Rect(WIDTH - 280, 160, 260, 20),
    start_value=200,
    value_range=(50, 350),
    manager=manager,
)

gravity_slider = pygame_gui.elements.UIHorizontalSlider(
    relative_rect=pygame.Rect(WIDTH - 280, 200, 260, 20),
    start_value=1,
    value_range=(0.1, 5),
    manager=manager,
)

pause_btn = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect(WIDTH - 280, 260, 120, 40),
    text="Pause",
    manager=manager,
)

resume_btn = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect(WIDTH - 140, 260, 120, 40),
    text="Resume",
    manager=manager,
)

reset_btn = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect(WIDTH - 280, 310, 260, 40),
    text="Reset",
    manager=manager,
)

# ========= Pendulum State ==========

def reset_state():
    return {
        "a1": math.pi / 2,
        "a2": math.pi / 2 + 0.5,
        "a1_v": 0,
        "a2_v": 0,
        "trail1": [],
        "trail2": [],
        "max_trail": 6000,
        "paused": False,
    }

state = reset_state()

# ======= Glow Rendering ==========

def draw_glow(surface, x, y, radius, color):
    for i in range(6):
        alpha = 255 - (i * 40)
        glow_surf = pygame.Surface((radius * 4, radius * 4), pygame.SRCALPHA)
        pygame.draw.circle(glow_surf, (*color, alpha), (radius * 2, radius * 2), radius + i*3)
        surface.blit(glow_surf, (x - radius*2, y - radius*2), special_flags=pygame.BLEND_ADD)

# ======= Simulation Update =========

def update_pendulum():
    if state["paused"]:
        return

    m1 = mass1_slider.get_current_value()
    m2 = mass2_slider.get_current_value()
    l1 = len1_slider.get_current_value()
    l2 = len2_slider.get_current_value()
    g = gravity_slider.get_current_value()

    a1, a2 = state["a1"], state["a2"]
    a1_v, a2_v = state["a1_v"], state["a2_v"]

    # Double pendulum equations
    num1 = -g * (2 * m1 + m2) * math.sin(a1)
    num2 = -m2 * g * math.sin(a1 - 2 * a2)
    num3 = -2 * math.sin(a1 - a2) * m2
    num4 = (a2_v*a2_v*l2 + a1_v*a1_v*l1*math.cos(a1 - a2))
    den = l1 * (2*m1 + m2 - m2*math.cos(2*a1 - 2*a2))
    a1_a = (num1 + num2 + num3*num4) / den

    num1 = 2 * math.sin(a1 - a2)
    num2 = (a1_v*a1_v*l1*(m1 + m2))
    num3 = g * (m1 + m2) * math.cos(a1)
    num4 = a2_v*a2_v*l2*m2*math.cos(a1 - a2)
    den = l2 * (2*m1 + m2 - m2*math.cos(2*a1 - 2*a2))
    a2_a = (num1 * (num2 + num3 + num4)) / den

    a1_v += a1_a
    a2_v += a2_a

    a1 += a1_v
    a2 += a2_v

    # Store back
    state["a1"], state["a2"] = a1, a2
    state["a1_v"], state["a2_v"] = a1_v, a2_v

# ========= Color-changing Function =========

def rainbow_color(t):
    return (
        int(127 * math.sin(t) + 128),
        int(127 * math.sin(t + 2) + 128),
        int(127 * math.sin(t + 4) + 128)
    )

# ========== Drawing ==========

def draw():
    WIN.fill((255, 255, 255))

    # axes
    pygame.draw.line(WIN, (200,200,200), (WIDTH//2,0), (WIDTH//2, HEIGHT), 2)
    pygame.draw.line(WIN, (200,200,200), (0, HEIGHT//2), (WIDTH, HEIGHT//2), 2)

    # Pendulum coordinates
    m1 = mass1_slider.get_current_value()
    m2 = mass2_slider.get_current_value()
    l1 = len1_slider.get_current_value()
    l2 = len2_slider.get_current_value()

    x1 = WIDTH//2 + l1 * math.sin(state["a1"])
    y1 = HEIGHT//2 + l1 * math.cos(state["a1"])

    x2 = x1 + l2 * math.sin(state["a2"])
    y2 = y1 + l2 * math.cos(state["a2"])

    # Add to trails, avoiding overlap
    if len(state["trail1"]) == 0 or (abs(state["trail1"][-1][0] - x1) > 1 or abs(state["trail1"][-1][1] - y1) > 1):
        state["trail1"].append((x1, y1))

    if len(state["trail2"]) == 0 or (abs(state["trail2"][-1][0] - x2) > 1 or abs(state["trail2"][-1][1] - y2) > 1):
        state["trail2"].append((x2, y2))

    # crop length
    if len(state["trail1"]) > state["max_trail"]:
        state["trail1"].pop(0)
    if len(state["trail2"]) > state["max_trail"]:
        state["trail2"].pop(0)

    # Draw trails with neon glow + color shifting
    t = pygame.time.get_ticks() / 400

    for i, (tx, ty) in enumerate(state["trail1"]):
        col = rainbow_color(t + i * 0.02)
        draw_glow(WIN, tx, ty, 3, col)
        pygame.draw.circle(WIN, col, (int(tx), int(ty)), 2)

    for i, (tx, ty) in enumerate(state["trail2"]):
        col = rainbow_color(t + i * 0.03 + 3)
        draw_glow(WIN, tx, ty, 3, col)
        pygame.draw.circle(WIN, col, (int(tx), int(ty)), 2)

    # Draw rods
    pygame.draw.line(WIN, (0, 0, 0), (WIDTH//2, HEIGHT//2), (x1, y1), 2)
    pygame.draw.line(WIN, (0, 0, 0), (x1, y1), (x2, y2), 2)

    # Draw masses with glow
    c1 = rainbow_color(t)
    c2 = rainbow_color(t + 2)

    draw_glow(WIN, x1, y1, int(m1/4), c1)
    draw_glow(WIN, x2, y2, int(m2/4), c2)

    pygame.draw.circle(WIN, c1, (int(x1), int(y1)), int(m1/5))
    pygame.draw.circle(WIN, c2, (int(x2), int(y2)), int(m2/5))

# ========== MAIN LOOP ==========

running = True
while running:
    dt = clock.tick(60) / 1000
    time = pygame.time.get_ticks()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        manager.process_events(event)

        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == pause_btn:
                state["paused"] = True
            if event.ui_element == resume_btn:
                state["paused"] = False
            if event.ui_element == reset_btn:
                state = reset_state()

    update_pendulum()
    draw()

    manager.update(dt)
    manager.draw_ui(WIN)

    pygame.display.update()

pygame.quit()

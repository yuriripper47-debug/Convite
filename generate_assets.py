from PIL import Image, ImageDraw, ImageFilter
import os

BASE = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(BASE, 'assets')
CREATURES = os.path.join(ASSETS, 'creatures')
os.makedirs(CREATURES, exist_ok=True)


def draw_circle(draw, xy, radius, fill):
    x, y = xy
    draw.ellipse((x - radius, y - radius, x + radius, y + radius), fill=fill)


def draw_fish(draw, size, body_color, accent_color, eye_color=(20, 30, 50)):
    w, h = size
    body = (20, 20, w - 20, h - 20)
    draw.ellipse(body, fill=body_color)
    tail = [(w - 18, h // 2), (w - 2, h // 3), (w - 2, 2 * h // 3)]
    draw.polygon(tail, fill=accent_color)
    fin = [(w // 2, 20), (w // 3, 0), (w // 3 + 25, 20)]
    draw.polygon(fin, fill=accent_color)
    eye = (w - 40, h // 2 - 8)
    draw.ellipse((eye[0], eye[1], eye[0] + 8, eye[1] + 8), fill=eye_color)


def draw_whale(draw, size):
    w, h = size
    draw.ellipse((30, 90, w - 30, h - 40), fill=(76, 145, 210))
    draw.polygon([(w - 50, 90), (w - 10, 50), (w - 10, 130)], fill=(64, 124, 190))
    draw.ellipse((100, 40, 180, 100), fill=(114, 174, 230))
    draw.ellipse((w - 110, h // 2 - 20, w - 90, h // 2), fill=(40, 70, 100))


def draw_turtle(draw, size):
    w, h = size
    draw.ellipse((25, 45, w - 25, h - 25), fill=(86, 168, 90))
    draw.ellipse((50, 70, w - 50, h - 30), fill=(120, 202, 125))
    draw.polygon([(w // 2 - 30, 54), (w // 2, 15), (w // 2 + 30, 54)], fill=(65, 123, 82))
    for x in [w // 2 - 55, w // 2 - 15, w // 2 + 25, w // 2 + 65]:
        draw.ellipse((x, 100, x + 18, 130), fill=(65, 123, 82))
    draw.ellipse((w // 2 - 20, h // 2 - 18, w // 2 - 4, h // 2 - 2), fill=(35, 60, 48))
    draw.ellipse((w // 2 + 8, h // 2 - 18, w // 2 + 24, h // 2 - 2), fill=(35, 60, 48))


def draw_crab(draw, size):
    w, h = size
    draw.ellipse((20, 50, w - 20, h - 10), fill=(214, 65, 48))
    draw.ellipse((35, 100, w - 35, h - 40), fill=(255, 130, 98))
    for x in [55, 110, 165, 220]:
        draw.arc((x, 60, x + 80, 120), start=180, end=360, fill=(150, 40, 30), width=8)
    for x in [75, 130, 185]:
        draw.line((x, 120, x - 15, h - 10), fill=(160, 48, 36), width=8)
        draw.line((x + 30, 120, x + 45, h - 10), fill=(160, 48, 36), width=8)
    draw.ellipse((w // 2 - 18, h // 2 - 15, w // 2 - 2, h // 2 + 1), fill=(35, 35, 35))
    draw.ellipse((w // 2 + 18, h // 2 - 15, w // 2 + 34, h // 2 + 1), fill=(35, 35, 35))
    draw.arc((w // 2 - 22, h // 2 + 8, w // 2 + 22, h // 2 + 28), start=200, end=340, fill=(255, 210, 180), width=5)


def draw_octopus(draw, size):
    w, h = size
    draw.ellipse((30, 30, w - 30, h - 40), fill=(153, 104, 218))
    draw.ellipse((80, 20, w - 80, 100), fill=(175, 133, 233))
    for i in range(8):
        x = 35 + i * 20
        draw.line((x, h - 40, x + 12, h), fill=(175, 133, 233), width=10)
    draw.ellipse((w // 2 - 18, h // 2 - 24, w // 2 - 4, h // 2 - 10), fill=(50, 30, 80))
    draw.ellipse((w // 2 + 8, h // 2 - 24, w // 2 + 22, h // 2 - 10), fill=(50, 30, 80))
    draw.arc((w // 2 - 20, h // 2 + 10, w // 2 + 20, h // 2 + 30), start=200, end=340, fill=(255, 255, 255), width=4)


def draw_seahorse(draw, size):
    w, h = size
    draw.arc((30, 30, w - 30, h - 30), start=20, end=200, fill=(245, 132, 66), width=12)
    draw.line((w // 2, h // 2 - 10, w // 2 + 50, h // 2 + 30), fill=(245, 132, 66), width=10)
    draw.line((w // 2 + 50, h // 2 + 30, w // 2 + 80, h // 2 + 90), fill=(245, 132, 66), width=10)
    draw.ellipse((w // 2 - 40, h // 2 - 40, w // 2 + 40, h // 2 + 10), fill=(255, 185, 110))
    draw.ellipse((w // 2 - 12, h // 2 - 22, w // 2 + 12, h // 2), fill=(50, 60, 70))
    draw.ellipse((w // 2 + 18, h // 2 - 22, w // 2 + 28, h // 2 - 12), fill=(50, 60, 70))


def draw_starfish(draw, size):
    w, h = size
    points = []
    for i in range(5):
        angle = -90 + i * 72
        x1 = w // 2 + int(50 * __import__('math').cos(__import__('math').radians(angle)))
        y1 = h // 2 + int(50 * __import__('math').sin(__import__('math').radians(angle)))
        x2 = w // 2 + int(90 * __import__('math').cos(__import__('math').radians(angle + 18)))
        y2 = h // 2 + int(90 * __import__('math').sin(__import__('math').radians(angle + 18)))
        points.append((x1, y1))
        points.append((x2, y2))
    draw.polygon(points, fill=(255, 164, 90))
    draw.circle((w // 2, h // 2), 20, fill=(245, 234, 166))


def draw_pufferfish(draw, size):
    w, h = size
    draw.ellipse((30, 35, w - 30, h - 30), fill=(251, 170, 86))
    draw.ellipse((50, 60, w - 50, h - 60), fill=(245, 215, 132))
    draw.ellipse((w // 2 - 15, h // 2 - 18, w // 2 + 15, h // 2 + 12), fill=(255, 255, 255))
    draw.ellipse((w // 2 - 8, h // 2 - 12, w // 2 + 8, h // 2 + 4), fill=(35, 35, 35))
    for x in [50, 110, 170, 230]:
        draw.ellipse((x, 80, x + 12, 100), fill=(255, 210, 120))


def create_background(path):
    img = Image.new('RGB', (1600, 900), '#d8f3ff')
    draw = ImageDraw.Draw(img)
    for y in range(0, 900, 70):
        shade = 180 + (y // 10) % 60
        draw.rectangle((0, y, 1600, y + 70), fill=(168 + (y // 20), 220 + (y // 20), 255))
    # reef pattern
    for i in range(0, 1600, 110):
        draw.ellipse((i, 650, i + 90, 760), fill=(44, 169, 198))
    # bubbles
    for _ in range(120):
        x = __import__('random').randint(0, 1600)
        y = __import__('random').randint(0, 900)
        r = __import__('random').randint(10, 38)
        alpha = __import__('random').randint(60, 170)
        bubble = Image.new('RGBA', (r * 2, r * 2), (255, 255, 255, 0))
        bdraw = ImageDraw.Draw(bubble)
        bdraw.ellipse((0, 0, r * 2, r * 2), outline=(255, 255, 255, alpha), width=3)
        img.paste(bubble, (x - r, y - r), bubble)
    img.save(path, quality=95)


def create_creature(path, drawer):
    img = Image.new('RGBA', (320, 240), (255, 255, 255, 0))
    draw = ImageDraw.Draw(img)
    drawer(draw, (320, 240))
    img.save(path)


create_background(os.path.join(ASSETS, 'fundo-mar.jpg'))
create_creature(os.path.join(CREATURES, 'crab.png'), draw_crab)
create_creature(os.path.join(CREATURES, 'turtle.png'), draw_turtle)
create_creature(os.path.join(CREATURES, 'octopus.png'), draw_octopus)
create_creature(os.path.join(CREATURES, 'whale.png'), draw_whale)
create_creature(os.path.join(CREATURES, 'seahorse.png'), draw_seahorse)
create_creature(os.path.join(CREATURES, 'fish.png'), lambda d, s: draw_fish(d, s, (46, 149, 211), (245, 165, 43)))
create_creature(os.path.join(CREATURES, 'starfish.png'), draw_starfish)
create_creature(os.path.join(CREATURES, 'pufferfish.png'), draw_pufferfish)

print('Assets generated in', ASSETS)

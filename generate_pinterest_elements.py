from PIL import Image

src = 'assets/origem-pinterest.jpg'
out_dir = 'assets/pinterest-elements'

img = Image.open(src).convert('RGBA')

items = {
    'jellyfish': (40, 40, 430, 530),
    'seahorse': (430, 70, 760, 540),
    'octopus': (650, 80, 1010, 570),
    'whale': (150, 600, 720, 1110),
    'coral-blue': (620, 620, 1005, 1025),
    'starfish': (260, 1030, 565, 1460),
    'crab': (600, 1200, 1015, 1625),
    'coral-pink': (30, 1470, 330, 1870),
    'turtle': (390, 1340, 810, 1820),
    'fish': (520, 1700, 1030, 1905),
    'anchor': (720, 1520, 1010, 1895),
}

import os
os.makedirs(out_dir, exist_ok=True)

for name, box in items.items():
    crop = img.crop(box)
    datas = list(crop.getdata())
    new = []
    for r, g, b, a in datas:
        if r > 245 and g > 245 and b > 245:
            a = 0
        new.append((r, g, b, a))
    crop.putdata(new)
    alpha = crop.getchannel('A')
    bbox = alpha.getbbox()
    if bbox is not None:
        crop = crop.crop(bbox)
    filename = os.path.join(out_dir, f'{name}.png')
    crop.save(filename)
    print(filename, crop.size)

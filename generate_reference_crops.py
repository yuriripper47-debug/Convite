from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parent
SRC = ROOT / 'assets' / 'reference-pin.jpg'
OUT = ROOT / 'assets' / 'reference-crops'
OUT.mkdir(exist_ok=True)

img = Image.open(SRC).convert('RGBA')

crops = {
    'crop_1.png': (30, 55, 310, 430),
    'crop_2.png': (340, 70, 700, 430),
    'crop_3.png': (30, 470, 330, 980),
    'crop_4.png': (345, 500, 705, 980),
}

for name, box in crops.items():
    crop = img.crop(box)
    crop.save(OUT / name)
    print(f'saved {name} {crop.size}')

print('done')

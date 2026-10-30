# python3 -I comparar.py <carpeta_original> <carpeta_final> <salida.png>
# Hoja de comparación: fila 1 original, fila 2 nuevo, 360x450 cada slide.
import glob, os, sys
from PIL import Image, ImageDraw
orig, fin, out = sys.argv[1:4]
o = sorted(glob.glob(os.path.join(orig, 'slide_*.*'))); n = sorted(glob.glob(os.path.join(fin, 'slide_*.png')))
W, H, G = 360, 450, 12
cols = max(len(o), len(n))
sheet = Image.new('RGB', (cols*(W+G)+G, 2*(H+G)+G+40), '#222')
d = ImageDraw.Draw(sheet)
for r, files in enumerate([o, n]):
    for i, f in enumerate(files):
        sheet.paste(Image.open(f).convert('RGB').resize((W, H), Image.LANCZOS), (G+i*(W+G), 40+G+r*(H+G)))
d.text((G, 12), 'Fila 1: original  |  Fila 2: nuevo', fill='white')
sheet.save(out); print(out, sheet.size)

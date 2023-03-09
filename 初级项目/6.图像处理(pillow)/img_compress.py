import glob
from PIL import Image


def compress_image(source_path, dest_path):
    with Image.open(source_path) as img:
        if img.mode != "RGB":
            img = img.convert("RGB")
        img.save(dest_path, "JPEG", optimize=True, quality=80)


paths = glob.glob("*.png")
for path in paths:
    compress_image(path, path[:-4] + ".jpg")
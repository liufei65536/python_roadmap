from PIL import ImageFont, ImageDraw, Image

img_path = 'pic.jpg'
img = Image.open(img_path)
img.thumbnail((128,128))
img.show()
from PIL import Image

image_raw = Image.open("./img/IMG_0286.JPG")
image_black_white = image_raw.convert('1')
image_black_white.save('./img/black_white_IMG_0286.JPG')
image_black_white.show()








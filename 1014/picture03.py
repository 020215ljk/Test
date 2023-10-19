

from PIL import Image
import matplotlib.pyplot as plt

image_raw = Image.open("./img/IMG_0286.JPG")
image_gray = image_raw.convert('L')
plt.figure('sunflower')
plt.imshow(image_gray, cmap='gray')
plt.show()




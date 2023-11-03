from PIL import Image
import numpy as np
from imageio.v2 import imsave

img = Image.open('img/Squirtle.jpg')
img = np.array(img)

print(img.dtype, img.shape)

img_tinted = img * [1, 0.95, 0.9]

img_tinted = np.array(Image.fromarray(np.uint8(img_tinted)).resize((300, 300)))

imsave('img/Squirtle_change.jpg', img_tinted)





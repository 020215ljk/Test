from scipy.misc import imread, imsave, imresize

img = imread('img/Squirtle.jpg')
print(img.dtype, img.shape)

img_tinted = img * [1, 0.95, 0.9]

img_tinted = imresize(img_tinted, (300, 300))

imsave('img/Squirtle_change.jpg', img_tinted)







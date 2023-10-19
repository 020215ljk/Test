# 使用cv2库将图片改为灰度图
import cv2

image = cv2.imread('./img/IMG_0286.JPG', cv2.IMREAD_GRAYSCALE)
cv2.imwrite('./img/grayIMG_0286.JPG', image)

# import cv2
#
# # image = cv2.imread('./images/sunflower.jpg', cv2.IMREAD_GRAYSCALE)
#
# # cv2.imwrite('./images/gray_sunflower.jpg', image)
#
# #  进一步探索图片格式
# image = cv2.imread('./img/IMG_0286.JPG')
# print(image.shape)
# imageGray = cv2.imread('./img/grayIMG_0286.JPG')
# print(imageGray.shape)
# imageGray2 = cv2.imread('./img/IMG_0286.JPG', cv2.IMREAD_GRAYSCALE)
# print(imageGray2.shape)

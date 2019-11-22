import cv2
import numpy as np

image1 = np.zeros([250,500,3] , dtype=np.uint8)
image2 = np.zeros([250,500,3] , dtype=np.uint8)

image1 =  cv2.rectangle(image1 , (200,0) , (300,100) , (255,255,255) , -1)
image2 =cv2.rectangle(image2 , (0,0) , (250,500) , (255,255,255) , -1)

cv2.imshow("img" , image1)
cv2.waitKey(0)
cv2.imshow("img" , image2)

cv2.waitKey(0)


bitand = cv2.bitwise_and(image1 , image2)
cv2.imshow("Bitwise AND" , bitand)
cv2.waitKey(0)

bitor = cv2.bitwise_or(image1 , image2)
cv2.imshow("bitwise OR" , bitor)
cv2.waitKey(0)

bitxor = cv2.bitwise_xor(image1 , image2)
cv2.imshow("bitwise XOR" , bitxor)
cv2.waitKey(0)


bitnot = cv2.bitwise_not(image1)
cv2.imshow("bitwise NOT" , bitnot)
cv2.waitKey(0)


cv2.destroyAllWindows()


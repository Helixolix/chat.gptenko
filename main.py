import cv2

imgOfCapybara = cv2.imread("./data/capybara840x600.jpg") 
imgCpBlure = cv2.GaussianBlur(imgOfCapybara, (19, 19), 0)



cv2.imshow("Test", imgCpBlure)
cv2.waitKey(0)
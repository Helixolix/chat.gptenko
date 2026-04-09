import cv2

imgOfCapybara = cv2.imread("./data/capybara840x600.jpg")

cv2.imshow("Test", imgOfCapybara)
cv2.waitKey(0)
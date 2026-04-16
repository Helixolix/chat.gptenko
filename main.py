import cv2

imgOfCapybara = cv2.imread("./data/capybara840x600.jpg") 
imgCpBlure = cv2.GaussianBlur(imgOfCapybara, (19, 19), 0)
imgOfCapybara_resize = cv2.resize(imgOfCapybara, (512, 512))
imgOfCapybara_BW = cv2.cvtColor(imgCpBlure, cv2.COLOR_RGB2GRAY)


cv2.imshow("Trooll Face", imgOfCapybara_BW)
cv2.waitKey(0)
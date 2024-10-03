import cv2 as cv
img = cv.imread('C:\\Users\\megha\\OneDrive\\Desktop\\CV Python\\Cats\\pexels-kowalievska-1170986.jpg')

cv.imshow('Cat',img)
k=cv.waitKey(0)
if k==ord('m'):
    cv.imwrite('C:\\Users\\megha\\OneDrive\\Desktop\\CV Python\\Cats\\Cat3.jpg', img, [cv.IMWRITE_JPEG_QUALITY, 90])

cv.destroyAllWindows()




import cv2 as cv 
def rescale(frame,scale=0.50):
    width=int(frame.shape[1]*scale)
    length=int(frame.shape[0]*scale)

    dimensions = (width,length) 
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

capture=cv.VideoCapture(r"C:\\Users\\megha\\OneDrive\\Desktop\\CV Python\\Dogs\\1182756-hd_1920_1080_25fps.mp4")
while True:
    isTrue, frame = capture.read()
    
    # Check if frame is successfully captured
    if not isTrue:
        print("Failed to capture frame. Exiting...")
        break
    
    frame_resized = rescale(frame)
    img =cv.imread("Cat2.jpg")
    img_rescale=rescale(img)
    cv.imshow("image",img_rescale)

    cv.imshow('Video2', frame)
    cv.imshow('Video', frame_resized)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()
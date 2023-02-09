 import cv2
 img=cv2.imread("solar-system.jpg")
 cv2.imshow("solar-system.jpg")
 cv2.waitKey(0)
 cv2.putText(IMG,
 "SUN",
 (20,300)
 cv2.FONT_HERSEY_COMPLEX,
 0,5
 (255,255,255)
 )
 cm2.imWrite("Solar_systemwithname.jpg",img)
import cv2
import numpy as np


# img = cv2.imread("img/bicycle.jpg")   #file ka part batane ke liye


#how to convert rbg into a grey scale image
# img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# print(img_gray.shape)

# img[:,:,0]=0 #yellow color ka dikhyi degi image
# imgBlue=img[:,:,0]
# imgRed=img[:,:,1]
# imgGreen=img[:,:,2]
#
# new_img=np.hstack((imgBlue,imgRed,imgGreen)) #teen images side by side dikhayi dengi with different colors


#resize image using open cv
# img_resize=cv2.resize(img,(256,256))
# img_resize=cv2.resize(img,(img.shape[1]/2,img.shape[0]/2))

# #image flipping
# img_flip=cv2.flip(img,0) #180 flip 1 doge to horizontal axis me flip ho jayega reduce overfitting
# #data organization -1 is combined effect of both of these horizontal+vertical
#
# img_crop=img[100:300,200:500]#image slicing first part height next part width top left se cropping
#
# #how to save an image
# cv2.imwrite("bicycle_small.png",img_crop)
#

# flag=False
# ix=-1
# iy=-1
#
# def crop(event,x,y,flags,params):
#     global flag,ix,iy
#     if event==1:
#         flag=True
#         ix=x
#         iy=y
#
#     elif event==4:
#         fx=x
#         fy=y
#
#         flag=False
#         cv2.rectangle(img,pt1=(ix,iy),pt2=(x,y),color=(0,0,0),thickness=1)
#
#         cropped=img[iy:fy,ix:fx]
#         cv2.imshow("cropped",cropped)
#         cv2.waitKey(0)
#
# cv2.namedWindow(winname="window")
# cv2.setMouseCallback("window", crop)
# cv2.imshow("window", img_crop) #image show krne ke liye lekin woh screen se turant udd jayega
# cv2.waitKey(0) #induce infinte delay for photo

# apni khud ki image banao rectangle circle line aur text
 # img=np.zeros((512,512,3))
#
# while True:
#     cv2.imshow("window",img)
#     if cv2.waitKey(1)&0xFF==ord('x'):
#         break
#
# cv2.destroyAllWindows()

import time
cap=cv2.VideoCapture('output.avi')
# fourcc=cv2.VideoWriter_fourcc(*'XVID')
# out=cv2.VideoWriter('output.avi',fourcc,20.0,(640,480))
# while True:
#     ret,frame=cap.read()
#     out.write(frame)
#     img_gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
#     cv2.imshow("webcam",img_gray)
#     if cv2.waitKey(1) & 0xFF == ord('x'):
#         break
# out.release()

while True:
    ret,frame=cap.read()
    time.sleep(1/20)
    cv2.imshow("webcam",frame)
    if cv2.waitKey(1) & 0xFF == ord('x'):
        break

cv2.destroyAllWindows()

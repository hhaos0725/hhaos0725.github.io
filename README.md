# 黄浩珅厉害厉害厉害厉害厉害厉害厉害

牛牛牛牛牛牛牛牛牛牛牛牛

飒飒飒

import cv2 as cv
import time

cap=cv.VideoCapture(0)
cap.set(3,900)
cap.set(4,900)

while(cap.isOpened()):
    ret_flag, Vshow = cap.read()
    cv.imshow('Capture', Vshow)
    k=cv.waitKey(1)
    if k==ord('s'):
        print('222222')
        print(cap.get(3))
        print(cap.get(4))
    elif k==ord('q'):
        print('完成')
        break
    print('摄像头捕获成功')
    # pass
    # time.sleep(1)
cap.release()
cv.destoryAllWindows()
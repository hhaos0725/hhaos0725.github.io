# 黄浩珅厉害厉害厉害厉害厉害厉害厉害

牛牛牛牛牛牛牛牛牛牛牛牛
<img src="https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1574182861017&di=180520abd4a3a41d21af1fa9096316ea&imgtype=0&src=http%3A%2F%2Fhbimg.b0.upaiyun.com%2Ffaad29c6643c88d8736be3846c791624725bb492e447-Han5mr_fw658">

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
<a href="https://github.com/hhaos0725/hhaos0725.github.io">1.PYTHON开发环境搭建</a>
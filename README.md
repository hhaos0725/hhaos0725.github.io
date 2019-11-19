# 黄浩珅厉害厉害厉害厉害厉害厉害厉害
<html xmlns="http://www.w3.org/1999/xhtml"><head>
    <title>欢迎来到王一刚老师的课程主页</title>
    <link href="style.css" rel="stylesheet" type="text/css">
    <script src="//hm.baidu.com/hm.js?39dcd5bd05965dcfa70b1d2457c6dcae"></script><script type="text/x-mathjax-config">
        MathJax.Hub.Config({tex2jax: {inlineMath: [['$','$'], ['\\(','\\)']]}});
</script>
    <script type="text/javascript" src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML">
   </script>

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
<a href="https://github.com/hhaos0725/hhaos0725.github.io">1.PYTHON开发环境搭建</a>
#include <iostream>  
#include <string>  
#include <opencv2/core/core.hpp>  
#include <opencv2/highgui/highgui.hpp>  
#include <opencv2/imgproc/imgproc.hpp>  
#include <opencv2/objdetect/objdetect.hpp>  
#include <opencv2/ml/ml.hpp>  

using namespace std;
using namespace cv;
CV_WRAP HOGDescriptor() :   
     winSize(64,128),          // detect window   
     blockSize(16,16),         // block 大小   
     blockStride(8,8),         // overlap block的滑动步长   
     cellSize(8,8),            // cell 大小    
     nbins(9),                 // 直方图的bin个数   
     derivAperture(1),          // 微分算子核   
     winSigma(-1),              // 在window上进行高斯加权   
     histogramNormType(HOGDescriptor::L2Hys), // 直方图归一化类型   
     L2HysThreshold(0.2),  
     // L2-norm followed by clipping (limiting the maximum values of v to 0.2) and renormalising 
     gammaCorrection(true), // Gamma校正，去除光照影响  
     nlevels(HOGDescriptor::DEFAULT_NLEVELS)   // 分层数  
void detectMultiScale(constGpuMat& img, vector<Rect>& found_locations, double hit_threshold= 0,
 Sizewin_stride = Size(), Size padding = Size(), double scale0=1.05,intgroup_threshold=2 );

int mainHog()
{
    Mat src = imread("5.jpg");
    // 1. 定义HOG对象  
    HOGDescriptor hog;//HOG特征检测器  
    // 2. 设置SVM分类器  
    hog.setSVMDetector(HOGDescriptor::getDefaultPeopleDetector());//设置SVM分类器为默认参数  
    // 3. 在测试图像上检测行人区域
    vector<Rect> found, found_filtered;//矩形框数组  
    hog.detectMultiScale(src, found, 0, Size(8, 8), Size(32, 32), 1.05, 2);//对图像进行多尺度检测，检测窗口移动步长为(8,8)  

    cout << "矩形个数：" << found.size() << endl;
    //4.找出所有没有嵌套的矩形框r,并放入found_filtered中,如果有嵌套的话,则取外面最大的那个矩形框放入found_filtered中  
    for (int i = 0; i < found.size(); i++)
    {
        Rect r = found[i];
        int j = 0;
        for (; j < found.size(); j++)
            if (j != i && (r & found[j]) == r)
                break;
        if (j == found.size())
            found_filtered.push_back(r);
    }
    cout << "过滤后矩形的个数：" << found_filtered.size() << endl;

    //5.画矩形框，因为hog检测出的矩形框比实际人体框要稍微大些,所以这里需要做一些调整
    for (int i = 0; i<found_filtered.size(); i++)
    {
        Rect r = found_filtered[i];
        r.x += cvRound(r.width*0.1);
        r.width = cvRound(r.width*0.8);
        r.y += cvRound(r.height*0.07);
        r.height = cvRound(r.height*0.8);
        rectangle(src, r.tl(), r.br(), Scalar(0, 255, 0), 3);
    }
    imwrite("ImgProcessed.jpg", src);
    namedWindow("src", 0);
    imshow("src", src);
    waitKey();
    system("pause");
    return 0;
}
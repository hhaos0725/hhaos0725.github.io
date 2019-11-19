coding=utf-8
from aip import AipFace
from aip import AipBodyAnalysis
import pymysql # 导入 pymysql
from PIL import Image
import base64

fenXiResult = {}

#‘’‘人体分析’’’
def RenTiFenXi():
    client = RenTi()
#“”" 读取图片 “”"
def get_file_content():
    with open(filePath, 'rb') as fp:
                              return fp.read()
image = get_file_content("11.jpg")
#“”" 如果有可选参数 “”"
options = {}
options["type"] = '''gender,age,lower_wear,headwear,glasses,upper_color,lower_color,upper_wear_fg,
upper_wear_texture,bag,smoke,vehicle,carrying_item,cellphone,umbrella'''
#“”" 带参数调用人体属性识别 “”"
result = client.bodyAttr(image, options)
return result

#‘’‘人脸分析’’’
def RenLianFenXi(tupian):
    client = RenLian()
f = open(tupian, 'rb') # 以二进制读方式打开图片
image = base64.b64encode(f.read()) # 将二进制串转为base64编码格式的字符串
f.close()
image64 = str(image, 'utf-8')
imageType = "BASE64"
#“”" 如果有可选参数 “”"
options = {}
options["face_field"] = "age,beauty,expression,gender,glasses,race,quality,face_type,faceshape"
options["max_face_num"] = 10 # 最多处理人脸的数目，默认值为1，仅检测图片中面积最大的那个人脸；最大值10，检测图片中面积最大的几张人脸。
#“”" 带参数调用人脸检测 “”"
result = client.detect(image64, imageType, options)
return result

#‘’‘人脸人体处理’’’
def RenLianRenTiChuLi(tupian):
    fenxi = RenLianFenXi(tupian)
#‘’’
#裁剪：传入一个元组作为参数
#元组里的元素分别是：（距离图片左边界距离x， 距离图片上边界距离y，距离图片左边界距离+裁剪框宽度x+w，距离图片上边界距离+裁剪框高度y+h）
#’’
im = Image.open(tupian) # 传入图片
# 图片的宽度和高度
img_size = im.size
i = 0
for num in fenxi['result']['face_list']:
        if num['face_probability'] > 0.3:
         if num['location']['left'] - num['location']['width'] <= 0:
          x = 0
        else:
         x = num['location']['left'] - num['location']['width']
        if num['location']['top'] - 40 <= 0:
         y = 0
        else:
         y = num['location']['top'] - 40
         w = x + num['location']['width'] * 3
         h = y + img_size[1] - y
         region = im.crop((x, y, w, h))
         filename = 'images/' + tupian[0:-4] + '_' + str(i) + '.jpg'
         i += 1
         region.save(filename)
renLianSouSu = RenLianSouSuo(filename)
for renLianSouSuo in renLianSouSu[‘result’][‘user_list’]:
if renLianSouSuo[‘score’] <= 50:
RenLianZhuCe(filename)
fenXiResult[‘age’] = num[‘age’] # 年龄
fenXiResult[‘beauty’] = num[‘beauty’] # 美丑打分，范围0-100，越大表示越美
fenXiResult[‘expression’] = num[‘expression’][‘type’] # 表情
fenXiResult[‘face_shape’] = num[‘face_shape’][‘type’] # 脸型
fenXiResult[‘gender’] = num[‘gender’][‘type’] # 性别
fenXiResult[‘race’] = num[‘race’][‘type’] # 人种
fenXiResult[‘glasses’] = num[‘glasses’][‘type’] # 是否带眼镜
renT = RenTiFenXi(filename)
for ren in renT[‘person_info’]:
renTi = ren[‘attributes’]
fenXiResult[‘upper_color’] = renTi[‘upper_color’][‘name’] # 上半身衣着颜色
fenXiResult[‘lower_color’] = renTi[‘lower_color’][‘name’] # 下半身衣着颜色
fenXiResult[‘cellphone’] = renTi[‘cellphone’][‘name’] # 是否使用手机
fenXiResult[‘lower_wear’] = renTi[‘lower_wear’][‘name’] # 半身服饰
fenXiResult[‘headwear’] = renTi[‘headwear’][‘name’] # 是否戴帽子
fenXiResult[‘upper_wear_fg’] = renTi[‘upper_wear_fg’][‘name’] # 上身服饰细分类
fenXiResult[‘upper_wear_texture’] = renTi[‘upper_wear_texture’][‘name’] # 上身服饰纹理
fenXiResult[‘bag’] = renTi[‘bag’][‘name’] # 背包
fenXiResult[‘umbrella’] = renTi[‘umbrella’][‘name’] # 是否撑伞
fenXiResult[‘smoke’] = renTi[‘smoke’][‘name’] # 是否吸烟
fenXiResult[‘vehicle’] = renTi[‘vehicle’][‘name’] # 交通工具
#‘’‘存入数据库’’’
db = pymysql.connect(host=“localhost”, user=“root”, password=“1998720”, db=“fenxi”, port=3306)
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()
# SQL 插入语句
sql = “”“INSERT INTO result(age,beauty,expression,face_shape,gender,glasses,race,upper_color,lower_color,cellphone,lower_wear,headwear,upper_wear_fg,upper_wear_texture,umbrella,bag,smoke,vehicle)
VALUES (’%s’,’%s’,’%s’,’%s’,’%s’,’%s’,’%s’,’%s’,’%s’,’%s’,’%s’,’%s’,’%s’,’%s’,’%s’,’%s’,’%s’,’%s’)”"" % (fenXiResult[‘age’],fenXiResult[‘beauty’],fenXiResult[‘expression’],fenXiResult[‘face_shape’],fenXiResult[‘gender’],fenXiResult[‘glasses’],fenXiResult[‘race’],fenXiResult[‘upper_color’],fenXiResult[‘lower_color’],fenXiResult[‘cellphone’],fenXiResult[‘lower_wear’],fenXiResult[‘headwear’],fenXiResult[‘upper_wear_fg’],fenXiResult[‘upper_wear_texture’],fenXiResult[‘umbrella’], fenXiResult[‘bag’],fenXiResult[‘smoke’],fenXiResult[‘vehicle’])
try:
# 执行sql语句
cursor.execute(sql)
# 提交到数据库执行
db.commit()
except:
# 如果发生错误则回滚
db.rollback()
else:
print(‘人脸已存在’)
continue

#‘’‘人脸注册’’’
def RenLianZhuCe(filename):
client = RenLian()
f = open(filename, ‘rb’) # 以二进制读方式打开图片
image = base64.b64encode(f.read()) # 将二进制串转为base64编码格式的字符串
f.close()
image64 = str(image, ‘utf-8’)
imageType = “BASE64”
groupId = “group1”
userId = “user1”
#“”" 调用人脸注册 “”"
client.addUser(image64, imageType, groupId, userId)
#‘’‘人脸搜索’’’
def RenLianSouSuo(filename):
client = RenLian()
f = open(filename, ‘rb’) # 以二进制读方式打开图片
image = base64.b64encode(f.read()) # 将二进制串转为base64编码格式的字符串
f.close()
image64 = str(image, ‘utf-8’)
imageType = “BASE64”
groupIdList = “group1”

""" 调用人脸搜索 """
result = client.search(image64, imageType, groupIdList)
return result
if name == ‘main’:
tupian = ‘xie.jpg’
RenLianRenTiChuLi(tupian)

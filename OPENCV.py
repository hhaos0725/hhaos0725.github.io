import cv2
def is_inside(o, i):
     ox, oy, ow, oh = o
     ix, iy, iw, ih = i
     return ox > ix and ox + ow < ix + iw and oy + oh < iy + ih
 

def draw_person(image, person):
     x, y, w, h = person
     cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 255), 2)


img = cv2.imread("D:\photo/CYC6.jpg")
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
found, w = hog.detectMultiScale(img)
found_filtered = []
for ri, r in enumerate(found):
     for qi, q in enumerate(found):
         if ri != qi and is_inside(r, q):
             break
         else:
             found_filtered.append(r)
 
for person in found_filtered:
     draw_person(img, person)

 
cv2.imshow("person detection", img)
cv2.waitKey()
cv2.destroyAllWindows()
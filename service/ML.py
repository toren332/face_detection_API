import numpy as np
import cv2
from django.conf import settings
from PIL import Image
import PIL
import service.models as models


class FaceDetector():

    def __init__(self, faceCascadePath):
        self.faceCascade = cv2.CascadeClassifier(faceCascadePath)

    def detect(self, image, scaleFactor=1.1,
               minNeighbors=5,
               minSize=(30, 30)):
        # function return rectangle coordinates of faces for given image
        rects = self.faceCascade.detectMultiScale(image,
                                                  scaleFactor=scaleFactor,
                                                  minNeighbors=minNeighbors,
                                                  minSize=minSize)
        return rects


def detect_face(image, obj, scaleFactor=1.15, minNeighbors=20, minSize=(30, 30), ):
    fd = FaceDetector(settings.MEDIA_ROOT + "/haarcascade_frontalface_default.xml")

    # face will detected in gray image
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    faces = fd.detect(image_gray,
                      scaleFactor=scaleFactor,
                      minNeighbors=minNeighbors,
                      minSize=minSize)

    for x, y, w, h in faces:
        # detected faces shown in color image
        cv2.rectangle(image, (x, y), (x + w, y + h), (127, 255, 0), 3)
        print()
        models.FaceBorder.objects.create(x=x, y=y, w=w, h=h, obj=obj)
    return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)


def get_img(way):
    return np.copy(cv2.imread(settings.MEDIA_ROOT+'/'+way))


def edited_img(img_way):
    obj = models.Obj.objects.get(original_photo=str(img_way))

    _ = Image.fromarray(detect_face(image=get_img(img_way), obj=obj))
    print(obj)

    _.save(settings.MEDIA_ROOT+'/edited/'+str(img_way).split('/')[1])
    return '/edited/'+str(img_way).split('/')[1]
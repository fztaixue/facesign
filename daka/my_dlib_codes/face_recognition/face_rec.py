import cv2
import dlib
import numpy as np


def comparePersonData(data1, data2, deviation=0.50):
    # if data1 == None or data2 == None:
    #     print("It's not the same person")
    #     return
    diff = 0
    for i in range(len(data1)):
        diff += (data1[i] - data2[i]) ** 2
    diff = np.sqrt(diff)
    if (diff < deviation):
        return True
    else:
        return False


def savePersonData(face_rec_class, face_descriptor):
    if face_rec_class.name == None or face_descriptor == None or face_descriptor == 0:
        return
    filePath = face_rec_class.dataPath + face_rec_class.name + '.npy'
    vectors = np.array([])
    for i, num in enumerate(face_descriptor):
        vectors = np.append(vectors, num)
    np.save(filePath, vectors)
    return vectors


def loadPersonData(filePath):
    vectors = np.load(filePath)
    return vectors


class face_recognition(object):
    def __init__(self):
        # self.current_path = str(os.path.abspath(os.path.join(os.getcwd(), "../..")))  # 获取上上级的路径
        self.current_path = "/mnt/weChatApplet/face_recognition"  # 获取上上级的路径
        self.predictor_path = self.current_path + "/my_dlib_codes/face_recognition/models/shape_predictor_68_face_landmarks.dat"
        self.face_rec_model_path = self.current_path + "/my_dlib_codes/face_recognition/models/dlib_face_recognition_resnet_model_v1.dat"
        self.faces_folder_path = self.current_path + "/my_dlib_codes/face_recognition/faces/"
        self.dataPath = self.current_path + "/my_dlib_codes/daka/data/"
        self.detector = dlib.get_frontal_face_detector()
        self.shape_predictor = dlib.shape_predictor(self.predictor_path)
        self.face_rec_model = dlib.face_recognition_model_v1(self.face_rec_model_path)
        self.name = None
        self.img_bgr = None
        self.img_rgb = None
        self.detector = dlib.get_frontal_face_detector()
        self.shape_predictor = dlib.shape_predictor(self.predictor_path)
        self.face_rec_model = dlib.face_recognition_model_v1(self.face_rec_model_path)

    def inputPerson(self, name='people', img_path=None):
        if img_path == None:
            RuntimeError("No file!\n")
            return

            # img_name += self.faces_folder_path + img_name
        self.name = name
        self.img_bgr = cv2.imread(img_path)
        # opencv的bgr格式图片转换成rgb格式
        b, g, r = cv2.split(self.img_bgr)
        self.img_rgb = cv2.merge([r, g, b])

    def create128DVectorSpace(self):
        dets = self.detector(self.img_rgb, 1)
        if len(dets) == 0:
            return 0
        for index, face in enumerate(dets):
            shape = self.shape_predictor(self.img_rgb, face)
            face_descriptor = self.face_rec_model.compute_face_descriptor(self.img_rgb, shape)
            return face_descriptor

# if __name__ == '__main__':
#     print(os.path.abspath(os.path.join(os.getcwd(), "../..")))

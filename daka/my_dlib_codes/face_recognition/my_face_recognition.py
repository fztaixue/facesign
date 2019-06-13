import pprint
import os
from daka.my_dlib_codes.face_recognition.face_rec import *


def my_face_recognition(input_images_paths, output_images_paths, python_result_model):
    # 创建对象
    face_rec = face_recognition()
    for i in range(0, len(input_images_paths)):
        # name中写第一个人名字，img_name为图片名字，注意要放在faces文件夹中
        face_rec.inputPerson(name='people1', img_path=input_images_paths[i])
        # 提取128维向量，是dlib.vector类的对象
        vector = face_rec.create128DVectorSpace()
        # 将提取出的数据保存到data文件夹，为便于操作返回numpy数组，内容还是一样的
        person_data1 = savePersonData(face_rec, vector)
        if vector == 0:
            flag = False
        else:
            # 导入第二张图片，并提取特征向量
            face_rec.inputPerson(name='people2', img_path=output_images_paths[i])
            vector = face_rec.create128DVectorSpace()  # 提取128维向量，是dlib.vector类的对象
            if vector == 0:
                flag = False
            else:
                person_data2 = savePersonData(face_rec, vector)
                # 计算欧式距离，判断是否是同一个人
                flag = comparePersonData(person_data1, person_data2)
        python_result_model['success'] = 'true'
        python_result_model['same_people'] = str(flag)


# 录入员工 input_images_paths 输入图片
def insert_persion(input_images_path, input_data_path, data_name):
    # 创建对象
    face_rec = face_recognition()
    # 设置npy文件保存的地方
    face_rec.dataPath = input_data_path
    # name中写第一个人名字，img_name为图片名字，注意要放在faces文件夹中
    face_rec.inputPerson(name=data_name, img_path=input_images_path)
    # 提取128维向量，是dlib.vector类的对象
    vector = face_rec.create128DVectorSpace()
    # 将提取出的数据保存到data文件夹，为便于操作返回numpy数组，内容还是一样的
    savePersonData(face_rec, vector)
    if vector == 0:
        return False
    else:
        return True


# 获取人脸额数据的值
def load_persion_data(npy_path):
    return loadPersonData(npy_path)


# 对比人脸比
def find_match_persion(input_npy_path, input_other_npy_paths):
    person_data_input = loadPersonData(input_npy_path)
    for npy_path in input_other_npy_paths:
        if os.path.exists(npy_path) == False:
            continue
        persion_data = load_persion_data(npy_path)
        flag = comparePersonData(persion_data, person_data_input)
        if flag:
            return npy_path

    return ''


if __name__ == '__main__':
    insert_persion('/mnt/facephoto/0399763d-8fcc-4cfe-b974-e140f05e8741.jpg', '/mnt/facenpy/',
                   'f1fe5ae7-3152-46a5-b628-c29780a648bf')
    print("--------------------")
    print(loadPersonData('/tmp/pycharm_project_12/daka/my_dlib_codes/daka/data/xiaoming.npy'))

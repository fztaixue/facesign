import os
import sys
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
import json
from flask import Flask, request, json, jsonify
from daka.my_dlib_codes.face_recognition import my_face_recognition



app = Flask(__name__)
# 设置编码
app.config['JSON_AS_ASCII'] = False


@app.route("/")
def index():
    return "hellow"


# 插入用户数据
@app.route('/insertpersion', methods=['POST'])
def insert_persion():
    result = {
        "success": False,
        "message": "",
        "havepersion": ""
    }
    try:
        input_images_path = request.form.get("input_images_path")
        input_data_path = request.form.get("input_data_path")
        data_name = request.form.get("data_name")
        flag = my_face_recognition.insert_persion(input_images_path, input_data_path, data_name)
        result['success'] = True
        result['havepersion'] = ~flag
        return json.dumps(result, ensure_ascii=False)
    except BaseException as e:
        result['success'] = False
        result['message'] = e
        return json.dumps(result, ensure_ascii=False)


# 人脸比对
@app.route('/facecompare', methods=['POST'])
def find_match_persion():
    result = {
        "success": False,
        "message": "",
        "havepersion": ""
    }
    try:
        input_npy_path = request.form.get("input_npy_path")
        input_other_npy_paths = str(request.form.get("input_other_npy_paths")).split(',')
        data = my_face_recognition.find_match_persion(input_npy_path, input_other_npy_paths)
        result['success'] = True
        if data != '':
            result['havepersion'] = True
            result['data'] = data
        else:
            result['havepersion'] = False
        return json.dumps(result, ensure_ascii=False)
    except BaseException as e:
        result['success'] = False
        result['message'] = e
        return json.dumps(result, ensure_ascii=False)


@app.route('/face', methods=['POST'])
def hello_world():
    try:
        path = request.form.get("path")
        data = my_face_recognition.load_persion_data(path)
        return jsonify(str(data))
    except BaseException as e:
        print(e)
        return jsonify(e)


if __name__ == '__main__':
    app.run(port=4999, debug=True)

import json
import subprocess
import shlex
import base64
from loguru import logger
import cv2
import numpy as np


PREDICT_API = "http://0.0.0.0:3000/predict"
ORI_IMG_PATH = './bus.jpeg'

data = subprocess.run(shlex.split(f"curl -F 'fileobj=@{ORI_IMG_PATH};type=image/jpeg' {PREDICT_API}"), stdout=subprocess.PIPE).stdout
dict = json.loads(data)  

def decode_image(input_img):
    output_img = np.frombuffer(base64.b64decode(input_img.encode('utf8')), np.uint8)
    output_img = cv2.imdecode(output_img, cv2.IMREAD_COLOR)
    
    return output_img

out_img = decode_image(dict['enc_out_img'])
cv2.imwrite('./recv_out_img.jpg', out_img)

for coord, cls, conf in zip(dict['coord'], dict['cls'], dict['conf']):
    print(f'bbox: {[int(x) for x in coord ]}, class: {int(cls)}, confidence: {conf:.2f}')


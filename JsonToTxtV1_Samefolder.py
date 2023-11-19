'''
json 파일을 Yolo Segmentation을 위해 txt 형식으로 변경하는 프로그램
동일 폴더에 확장자만 바뀌어 저장됩니다.
20231119 by KH.Lim

폴더 명은 직접 수정해줘야 합니다.
'''

import os
import json

folder_path = '020310'  # 폴더의 실제 경로로 변경해야 합니다.

# 폴더 내의 모든 파일 가져오기
file_list = os.listdir(folder_path)

# JSON 파일 필터링
json_files = [file for file in file_list if file.endswith('.json')]

for json_file in json_files:
    file_name = os.path.join(folder_path, json_file)
    output_file = os.path.splitext(file_name)[0] + '.txt'  # 출력할 파일 이름

    with open(file_name, 'r') as file:
        json_data = json.load(file)

    with open(output_file, 'w') as output:
        for annotation in json_data['annotations']:
            category_id = annotation['category_id']
            segmentation = annotation['segmentation'][0]  # segmentation은 리스트 안에 리스트 형태로 주어졌으므로 첫 번째 요소만 사용합니다

            output.write(str(category_id) + ' ')
            for point in segmentation:
                output.write(str(point) + ' ')
            output.write('\n')  # 줄바꿈

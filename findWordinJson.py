'''
특정 폴더의 json 파일에서 특정단어 찾아 파일명 출력하기
20231120 by KH.Lim
'''

import os
import json

folder_path = '01'  # 폴더의 실제 경로로 변경해야 합니다.

# 폴더 내의 모든 파일 가져오기
file_list = os.listdir(folder_path)

# JSON 파일 중 'flood' 또는 'river'가 들어있는 파일 찾기
found_files = []
for file_name in file_list:
    if file_name.endswith('.json'):
        with open(os.path.join(folder_path, file_name), 'r') as file:
            json_data = json.load(file)
            description = json_data['info']['description'].lower()
            if 'flood' in description or 'river' in description:
                found_files.append(file_name)

# 찾은 파일 이름 출력
if found_files:
    print("Files containing 'flood' or 'river':")
    for file_name in found_files:
        print(file_name)
else:
    print("No files containing 'flood' or 'river' found in the folder.")

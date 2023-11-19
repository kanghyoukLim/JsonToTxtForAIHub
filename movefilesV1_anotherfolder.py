'''
원본 파일을 새로운 폴더로 랜덤 갯수만큼 이동시키기
단, 원본파일은 txt와 jpg 가 쌍으로 존재하고 쌍으로 이동된다.
Yolo Segmentation을 위한 프로그램
20231119 by KH.Lim
'''


import os
import random
import shutil

# 랜덤하게 선택할 파일의 수
num_pairs_to_copy = 3

# 원본 폴더와 목적지 폴더 경로 설정
source_folder = '020310txt'
destination_folder = '020310txt_moved'

# 만약 목적지 폴더가 없으면 새로 생성
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# 원본 폴더 내의 파일 목록 가져오기
all_files = os.listdir(source_folder)

# 파일 이름이 동일한 쌍 찾기
file_pairs = {}
for file_name in all_files:
    base_name, extension = os.path.splitext(file_name)
    if base_name in file_pairs:
        file_pairs[base_name].append(file_name)
    else:
        file_pairs[base_name] = [file_name]

# 동일한 이름을 가진 쌍 중 랜덤하게 선택하여 복사하기
selected_pairs = [pair for pair in file_pairs.values() if len(pair) >= 2]
random.shuffle(selected_pairs)
selected_pairs = selected_pairs[:min(num_pairs_to_copy, len(selected_pairs))]

for pair in selected_pairs:
    txt_file = [file for file in pair if file.endswith('.txt')][0]
    jpg_file = [file for file in pair if file.endswith('.jpg')][0]

    # 파일 복사
    shutil.copy(os.path.join(source_folder, txt_file), destination_folder)
    shutil.copy(os.path.join(source_folder, jpg_file), destination_folder)

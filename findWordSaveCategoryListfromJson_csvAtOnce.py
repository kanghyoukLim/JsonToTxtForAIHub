'''
폴더내 json파일에서 특정단어 찾아, 해당 단어 있으면
파일명과 카테고리 값 등 저장하기
231120 by KH.Lim
'''


import os
import json
import csv

root_folder = '03'  # 최상위 폴더명
output_file = f"{root_folder}.csv"  # 결과를 저장할 파일 이름
search_words = ['flood', 'river']  # 검색할 단어 리스트

# CSV 파일 열기 및 헤더 작성
with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['File Name', 'Supercategory', 'Category ID', 'Category']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    # 최상위 폴더 내의 모든 하위 폴더 탐색
    for dirpath, dirnames, filenames in os.walk(root_folder):
        for file_name in filenames:
            if file_name.endswith('.json'):
                file_path = os.path.join(dirpath, file_name)
                with open(file_path, 'r') as file:
                    json_data = json.load(file)
                    for annotation in json_data.get('annotations', []):
                        supercategory = annotation.get('supercategory')
                        category_id = annotation.get('category_id')
                        category = annotation.get('category')
                        description = json_data['info']['description'].lower()

                        # 특정 단어가 파일명 또는 파일 내용에 있는지 확인
                        if any(word in description for word in search_words):
                            writer.writerow({
                                'File Name': file_name,
                                'Supercategory': supercategory,
                                'Category ID': category_id,
                                'Category': category
                            })

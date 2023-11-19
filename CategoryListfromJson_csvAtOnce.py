'''
특정 폴더의 json 파일에서 supercategory와 category_id, category 찾아 파일명 출력하기
20231120 by KH.Lim
'''
#
# import os
# import json
#
# folder_path = '030308'  # 폴더의 실제 경로로 변경해야 합니다.
#
# # 폴더 내의 모든 파일 가져오기
# file_list = os.listdir(folder_path)
#
# # JSON 파일에서 파일 이름과 supercategory, category_id, category 출력
# for file_name in file_list:
#     if file_name.endswith('.json'):
#         with open(os.path.join(folder_path, file_name), 'r') as file:
#             json_data = json.load(file)
#             print(f"File Name: {file_name}")
#             for annotation in json_data.get('annotations', []):
#                 supercategory = annotation.get('supercategory')
#                 category_id = annotation.get('category_id')
#                 category = annotation.get('category')
#                 print(f"Supercategory: {supercategory}, Category ID: {category_id}, Category: {category}")
#             print('-' * 20)  # 구분선

'''
특정 폴더의 json 파일에서 supercategory와 category_id, category 찾아 csv로 저장하기
231120 by KH.Lim
'''
# import os
# import json
# import csv
#
# folder_path = '030308'  # 폴더의 실제 경로로 변경해야 합니다.
# folder_name = os.path.basename(folder_path)  # 폴더 이름 추출
# output_file = f"{folder_name}.csv"  # 결과를 저장할 파일 이름
#
# # CSV 파일 열기 및 헤더 작성
# with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
#     fieldnames = ['File Name', 'Supercategory', 'Category ID', 'Category']
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#     writer.writeheader()
#
#     # 폴더 내의 모든 파일 가져오기
#     file_list = os.listdir(folder_path)
#
#     # JSON 파일에서 정보를 읽어와 CSV 파일에 쓰기
#     for file_name in file_list:
#         if file_name.endswith('.json'):
#             with open(os.path.join(folder_path, file_name), 'r') as file:
#                 json_data = json.load(file)
#                 for annotation in json_data.get('annotations', []):
#                     supercategory = annotation.get('supercategory')
#                     category_id = annotation.get('category_id')
#                     category = annotation.get('category')
#                     writer.writerow({
#                         'File Name': file_name,
#                         'Supercategory': supercategory,
#                         'Category ID': category_id,
#                         'Category': category
#                     })

'''
특정 폴더의 하위 폴더의 json 파일에서 파일명, supercategory, categoryID, category 찾아 csv로 저장하기
한 번에 처리됨
231120 by KH.Lim
'''
import os
import json
import csv

root_folder = '01'  # 최상위 폴더명
output_file = f"{root_folder}.csv"  # 결과를 저장할 파일 이름

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
                        writer.writerow({
                            'File Name': file_name,
                            'Supercategory': supercategory,
                            'Category ID': category_id,
                            'Category': category
                        })

'''
카테고리_id 바꿔주기
'''

import os


# 변환 함수
def transform_number(number):
    # 숫자 변환 딕셔너리
    number_mapping = {
        '20310': '1',
        '20319': '2',
        '20320': '3',
        '20610': '4',
        '10101': '5'
    }
    return number_mapping.get(number, number)  # 변환된 숫자 반환 or 그대로 유지


# 원본 폴더 및 대상 폴더 설정
original_folder = '01txt'  # 원본 폴더 경로 입력
target_folder = '01_01'  # 대상 폴더 경로 입력

# 폴더 내의 모든 파일을 반복적으로 처리
for filename in os.listdir(original_folder):
    if filename.endswith(".txt"):
        file_path = os.path.join(original_folder, filename)
        target_file_path = os.path.join(target_folder, filename)

        # 파일 열기
        with open(file_path, 'r') as file:
            lines = file.readlines()

        # 변환된 내용을 담을 리스트
        transformed_lines = []

        # 각 행의 첫 번째 5자리 숫자를 변환하여 리스트에 추가
        for line in lines:
            # 공백을 기준으로 첫 번째 숫자를 추출
            first_number = line.split()[0]
            transformed_number = transform_number(first_number)
            # 변환된 숫자와 기존 숫자를 바꿔서 새로운 행 생성
            transformed_line = line.replace(first_number, transformed_number, 1)
            transformed_lines.append(transformed_line)

        # 변환된 내용 파일에 쓰기
        with open(target_file_path, 'w') as file:
            file.writelines(transformed_lines)

print("변환 완료!")

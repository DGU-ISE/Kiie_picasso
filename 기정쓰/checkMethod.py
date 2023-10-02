import cv2
import numpy as np
import csv

# 색깔에 따라 등급 분류(색깔은 직접 지정)
def checkColor(h,s,v): 
    if h==30:
        return 1
    elif h==0:
        if s==0 and v == 0:
            return 2
        elif s!= 0:
            return 4
        else:
            return 0
    elif h==105 or h == 106:
        return 3 
    else:
        return 0
    





#CSV파일로 추출    
def TurnCSV(img_path,columnName):
    img = cv2.imread(img_path)
    # 원하는 크기로 이미지 크기 조절
    new_width = 900  # 새로운 폭
    new_height = 800  # 새로운 높이
    resized_image = cv2.resize(img, (new_width, new_height))
    #이미지의 크기 확인
    height, width, _ = resized_image.shape

    #CSV파일 경로 설정
    csv_file_path = columnName + "_output.csv"


    with open(csv_file_path, mode='w', newline='', encoding='utf-8') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow(['x', 'y', '등급'])  # 칼럼 이름을 변경합니다.

        for x in range(width):
            for y in range(height):
                pixel_color = resized_image[y,x]
                hsv_color = cv2.cvtColor(np.uint8([[pixel_color]]), cv2.COLOR_BGR2HSV)[0][0]
                grade = checkColor(hsv_color[0],hsv_color[1],hsv_color[2])
                if grade == 0:
                    continue
                else:
                    csv_writer.writerow([x, y, grade])  # 데이터 행 쓰기
                    print(f'{x}, {y}, {grade}')

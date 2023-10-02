import cv2
import numpy as np

# 마우스 클릭 이벤트 핸들러 함수
def get_rgb(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:  # 왼쪽 마우스 버튼 클릭 시
        pixel_color = img[y, x]# 클릭한 지점의 BGR 색상을 가져옴
        hsv_color = cv2.cvtColor(np.uint8([[pixel_color]]), cv2.COLOR_BGR2HSV)[0][0]
        print(f"클릭한 지점의 HSV 값: {hsv_color}")
        # print(f"클릭한 지점의 BGR 값: {pixel_color}")
# 이미지 열기
image_path = "강도.jpg"  # 이미지 파일 경로를 여기에 입력하세요
img = cv2.imread(image_path)

# 윈도우를 생성하고 이미지 표시
cv2.imshow("Image", img)

# 마우스 클릭 이벤트를 위한 콜백 함수 연결
cv2.setMouseCallback("Image", get_rgb)

while True:
    key = cv2.waitKey(1)
    if key == 27:  # ESC 키를 누르면 종료
        break

cv2.destroyAllWindows()

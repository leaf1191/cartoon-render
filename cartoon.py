import cv2 as cv
import numpy as np

# 이미지 샤프닝
def sharpen_image(image):
    kernel = np.array([[0, -1, 0],
                       [-1, 5,-1],
                       [0, -1, 0]])
    sharpened = cv.filter2D(image, -1, kernel)
    return sharpened
    

def cartoonize_image(input_path, output_path):
    # 이미지 읽기
    img = cv.imread(input_path)
    if img is None:
        print("이미지를 찾을 수 없습니다.")
        return

    # 이미지 크기 조정(확인하기 쉽게)
    img = cv.resize(img, (0, 0), fx=1.5, fy=1.5)

    # 이미지 샤프닝
    sharpened = sharpen_image(img)

    # 1. 명암 처리
    gray = cv.cvtColor(sharpened, cv.COLOR_BGR2GRAY)
    clahe = cv.createCLAHE(clipLimit=1.5, tileGridSize=(5,5))
    gray = clahe.apply(gray)  # 명암 대비 강화
    
    # 2. 잡티 제거
    gray = cv.fastNlMeansDenoising(gray, None, 10, 7, 21)
    
    # 3. 엣지 검출
    edges = cv.adaptiveThreshold(gray, 255, 
                                cv.ADAPTIVE_THRESH_MEAN_C, 
                                cv.THRESH_BINARY, 11, 11)

    # 4. 컬러 사진 블러링
    color = cv.bilateralFilter(sharpened, 9, 300, 300)

    # 5. 카툰 효과 적용
    cartoon = cv.bitwise_and(color, color, mask=edges)

    # 결과 저장
    cv.imwrite(output_path, cartoon)

    # 결과 이미지 표시
    cv.imshow("Original", img)
    cv.imshow("Cartoon", cartoon)
    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == "__main__":
    input_path = "input.jpg"  # 입력 이미지 파일명
    output_path = "cartoon_output.jpg"  # 출력 파일명
    cartoonize_image(input_path, output_path)
# cartoon-render
OpenCV를 이용한 이미지 카툰 렌더링 프로그램

# 만화 같은 느낌이 드는 이미지 데모
**원본**

![Image](https://github.com/user-attachments/assets/d2d55c1d-262a-4fb6-a038-4ae9741d6269)

**카툰**

![Image](https://github.com/user-attachments/assets/87f41ef2-f99d-4ea1-af32-f4e53e7fe3a1)

# 만화 같은 느낌이 들지 않는 이미지 데모
**원본**

![Image](https://github.com/user-attachments/assets/0d8cdcfb-ac4f-4928-b0b3-09944a8a3af9)

**카툰**

![Image](https://github.com/user-attachments/assets/f9f59a34-23dd-421b-a16d-7a7719a7d2b1)

# 코드의 한계점 분석
- CLAHE를 이용하여 이미지의 명암 차이를 키웠으나, adaptiveThreshold의 한계점에 의해 명암 차이가 뚜렷하지 않는 이미지에서는 edge가 선명하게 나타나지 않는다.


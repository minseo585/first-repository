# 데이터 리스트
data = [1, 3, 2, 4, 4, 5, 1, 3, 2, 1, 5, 5, 3, 4, 2, 1]

# 각 값의 빈도를 저장할 빈도수 딕셔너리
frequency = {}

# 데이터의 빈도 계산
for num in data:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

# 최대 빈도 구하기
max_freq = max(frequency.values())

# 도수 히스토그램 세로로 출력
print("세로 도수 히스토그램:")
for i in range(max_freq, 0, -1):
    for num in sorted(frequency.keys()):
        if frequency[num] >= i:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()  # 줄바꿈

# 하단에 값 출력
for num in sorted(frequency.keys()):
    print(num, end=" ")

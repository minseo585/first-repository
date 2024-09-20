# ������ ����Ʈ
data = [1, 3, 2, 4, 4, 5, 1, 3, 2, 1, 5, 5, 3, 4, 2, 1]

# �� ���� �󵵸� ������ �󵵼� ��ųʸ�
frequency = {}

# �������� �� ���
for num in data:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

# �ִ� �� ���ϱ�
max_freq = max(frequency.values())

# ���� ������׷� ���η� ���
print("���� ���� ������׷�:")
for i in range(max_freq, 0, -1):
    for num in sorted(frequency.keys()):
        if frequency[num] >= i:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()  # �ٹٲ�

# �ϴܿ� �� ���
for num in sorted(frequency.keys()):
    print(num, end=" ")

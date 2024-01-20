# ???
# 좌표 압축 : 여러 곳에 흩뿌려진 좌표들을 연속된 수들로 모아 압축하는 것
#
# 예를 들어, 다음과 같은 좌표가 있다고 하자.
# [1, 10, 10000, 1000000]
# 이렇게 네 점의 좌표가 있을 때, 좌표는 네 개 이지만 좌표값이 1부터 1,000,000 까지 있다.
#
# 하지만 이 좌표를 압축하여 순서대로 표현하면 [0, 1, 2, 3] 이 된다.
# 즉, 작은 값부터 시작해서 0부터 인덱스를 부여하는 방식이다.
# 1이 가장 작으므로 0이되고 10이 1, 10000이 2, 1000000이 3이 되는 것이다.

import sys

n = int(sys.stdin.readline())
n_list = list(map(int, sys.stdin.readline().split()))
set_list = sorted(set(n_list))  # 중복 제거하여 정렬

dic = {set_list[i]: i for i in range(len(set_list))}
# 딕셔너리 사용
# 중괄호{ }로 선언
# 키: 값 형태를 쉼표로 연결
# 대괄호([키] = 값)를 사용하여 원하는 값을 할당

for i in n_list:
    print(dic[i], end=" ")

num_of_test_cases = 0
count = 0
num_of_test_cases = int(input())

while count < num_of_test_cases:
    N, M = list(map(int, input().split()))
    C = list(map(int, input().split()))
    remainder = sum(C) % M
    count = count + 1
    print("Case #"+ str(count) + f": {remainder}")

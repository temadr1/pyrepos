numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

for i in range(len(numbers)):
    if numbers[i] == None:
        nums = numbers[0:i:] + numbers[i+1::]
        numbers[i] = sum(nums) / len(numbers)

print('Измененный список:', numbers)

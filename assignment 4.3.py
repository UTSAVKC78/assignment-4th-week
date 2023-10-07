def num_divide3(num):
    count = 0
    for i in range(1, num + 1):
        if i % 3 == 0:
            count += 1
    return count

while True:
    user_input = input("enter a positive integer (or 'done' to quit): ")
    
    if user_input.lower() == 'done':
        break
    
    try:
        num = int(user_input)
        if num <= 0:
            print("please enter a positive integer.")
        else:
            result = num_divide3(num)
            print(f"numbers divisible by 3 from 1 to {num}: {result}")
    except ValueError:
        print("invalid input. please enter a positive integer or 'done'.")

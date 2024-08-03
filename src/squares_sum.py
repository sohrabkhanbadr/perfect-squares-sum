def find_squares_sum(n, max_square):
    """
    پیدا کردن ترکیب‌های مربع‌های کامل که مجموع آنها برابر با n باشد.
    """
    def backtrack(target, start, path, results):
        if target == 0:
            results.append(path.copy())
            return
        for i in range(start, len(squares)):
            if squares[i] > target:
                break
            path.append(squares[i])
            backtrack(target - squares[i], i, path, results)
            path.pop()
    
    # تولید مربع‌های کامل تا max_square
    squares = []
    i = 1
    while i * i <= max_square:
        squares.append(i * i)
        i += 1
    
    # نتایج نهایی
    results = []
    backtrack(n, 0, [], results)
    return results

# استفاده از تابع
n = 20
max_square = 20
combinations = find_squares_sum(n, max_square)

print(f"ترکیب‌های مربع‌های کامل که مجموع آنها برابر با {n} باشد:")
for combo in combinations:
    print(combo)

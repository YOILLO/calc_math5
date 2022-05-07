import collections

def find_euler_next(func, x_pr, y_pr, h):
    return y_pr + h * func(x_pr, y_pr)


def adams_method(func, x_0, y_0, h, n):
    if n <= 4:
        print("Не имеет смысла считать для меньше чем для 4х")
        exit()
    answer = {x_0 + i * h: 0 for i in range(n)}
    answer[x_0] = y_0
    y_1 = find_euler_next(func, x_0, y_0, h)
    func_prev_1 = func(x_0 + h, y_1)
    answer[x_0 + h] = y_1
    y_2 = find_euler_next(func, x_0 + h, y_1, h)
    func_prev_2 = func(x_0 + 2 * h, y_2)
    answer[x_0 + 2*h] = y_2
    y_3 = find_euler_next(func, x_0 + 2 * h, y_2, h)
    func_prev_3 = func(x_0 + 3 * h, y_3)
    answer[x_0 + 3*h] = y_3
    y_prev = find_euler_next(func, x_0 + 3 * h, y_3, h)
    func_prev_4 = func(x_0 + 4 * h, y_prev)
    answer[x_0 + 4*h] = y_prev
    for i in range(4, n):
        del_f_i = func_prev_4 - func_prev_3
        del2_f_i = func_prev_4 - 2 * func_prev_3 + func_prev_2
        del3_f_i = func_prev_4 - 3 * func_prev_3 + 3 * func_prev_2 - func_prev_1
        x_next = x_0 + i * h
        x_prev = x_0 + (i - 1) * h
        y_next = y_prev + h * func(x_prev, y_prev) + ((h ** 2) / 2) * del_f_i + ((5 * (h ** 3)) / 12) * del2_f_i + \
                 ((3 * (h ** 4)) / 8) * del3_f_i
        answer[x_next] = y_next
        func_prev_1 = func_prev_2
        func_prev_2 = func_prev_3
        func_prev_3 = func_prev_4
        func_prev_4 = func(x_next, y_next)
        y_prev = y_next
    return answer

def get_answer(func, x_0, y_0, a, b):
    h = 0.001
    while True:
        try:
            ans = adams_method(func, x_0, y_0, h, round(abs(b - x_0)/h))
            ans = ans | adams_method(func, x_0, y_0, -h, round(abs(x_0 - a)/h))
            return collections.OrderedDict(sorted(ans.items()))
        except OverflowError:
            h *= 2
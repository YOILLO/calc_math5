from calculations import *
from io_module import *

func = ask_function()

x_0 = ask_float("Введте x0: ")
y_0 = ask_float("Введте y0: ")
a = ask_float("Введте правую границу (a): ")
b = ask_float("Введте левую границу (b): ")
if a <= x_0 <= b:
    ans = get_answer(func, x_0, y_0, a, b)
    #for i in ans:
        #print(i, ans[i])
    plot(ans, x_0, y_0)
else:
    print("Введите a < x0 < b")
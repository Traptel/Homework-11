hypotenuse_value = lambda x, y=2: (x ** 2 + y ** 2) ** 0.5

values_1 = [4, 5, 6]
result_1 = list(map(hypotenuse_value, values_1))
print("Гіпотенуза з одним параметром:", result_1)

values_x = [7, 3, 6]
values_y = [3, 5, 8]
result_2 = list(map(hypotenuse_value, values_x, values_y))
print("Гіпотенузи з двома параметроми:", result_2)

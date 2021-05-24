# Дан список интов, повторяющихся элементов в списке нет. Нужно преобразовать это множество в строку, сворачивая
# соседние по числовому ряду числа в диапазоны.
# Примеры:
# [1,4,5,2,3,9,8,11,0] => "0-5,8-9,11"
# [1,4,3,2] => "1-4"
# [1,4] => "1,4"

input_arr = [1, 4, 5, 2, 3, 9, 8, 11, 0]


def get_result(input_arr):
    sorted_arr = sorted(input_arr)
    results = list()
    i, j = 0, 0
    while i < len(sorted_arr):
        start_val = sorted_arr[i]
        j = i + 1

        if j < len(sorted_arr) - 1:
            if sorted_arr[i] + 1 == sorted_arr[j]:
                end_val = sorted_arr[j]
                while j < len(sorted_arr) - 1:
                    j += 1
                    if end_val + 1 == sorted_arr[j]:
                        end_val = sorted_arr[j]
                    else:
                        break

                results.append(f"{start_val}-{end_val}")
                i = j
        else:
            results.append(str(sorted_arr[i]))
            i += 1

    return ",".join(results)


print(get_result(input_arr))

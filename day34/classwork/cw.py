def remove_by_indexes(main_list, indexes_list):
    for index in sorted(indexes_list, reverse=True):
        if 0 <= index < len(main_list):
            del main_list[index]
    return main_list

main_list = [10, 20, 30, 40, 50]
indexes_list = [1, 3]

result = remove_by_indexes(main_list, indexes_list)
print(result)
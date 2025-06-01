class Sorter:
    def __init__(self):
        pass

    def bubblesort(self, arr, new=False):
        if new:
            # 复制原列表，避免修改原列表
            new_arr = arr[:]
            n = len(new_arr)
            # 外层循环控制排序的轮数
            for i in range(n):
                # 标记是否发生交换
                swapped = False
                # 内层循环进行相邻元素的比较和交换
                for j in range(0, n - i - 1):
                    if new_arr[j] > new_arr[j + 1]:
                        # 交换相邻元素
                        new_arr[j], new_arr[j + 1] = new_arr[j + 1], new_arr[j]
                        swapped = True
                # 如果没有发生交换，说明列表已经有序，可以提前退出
                if not swapped:
                    break
            return new_arr
        else:
            n = len(arr)
            # 外层循环控制排序的轮数
            for i in range(n):
                # 标记是否发生交换
                swapped = False
                # 内层循环进行相邻元素的比较和交换
                for j in range(0, n - i - 1):
                    if arr[j] > arr[j + 1]:
                        # 交换相邻元素
                        arr[j], arr[j + 1] = arr[j + 1], arr[j]
                        swapped = True
                # 如果没有发生交换，说明列表已经有序，可以提前退出
                if not swapped:
                    break

    def selectsort(self, arr, new=False):
        if new:
            # 复制原列表，避免修改原列表
            new_arr = arr[:]
            n = len(new_arr)
            # 外层循环控制排序的轮数
            for i in range(n):
                # 假设当前轮次的第一个元素为最小值
                min_index = i
                # 内层循环找到未排序部分的最小值
                for j in range(i + 1, n):
                    if new_arr[j] < new_arr[min_index]:
                        min_index = j
                # 将找到的最小值与当前轮次的第一个元素交换
                new_arr[i], new_arr[min_index] = new_arr[min_index], new_arr[i]
            return new_arr
        else:
            n = len(arr)
            # 外层循环控制排序的轮数
            for i in range(n):
                # 假设当前轮次的第一个元素为最小值
                min_index = i
                # 内层循环找到未排序部分的最小值
                for j in range(i + 1, n):
                    if arr[j] < arr[min_index]:
                        min_index = j
                # 将找到的最小值与当前轮次的第一个元素交换
                arr[i], arr[min_index] = arr[min_index], arr[i]
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

    def insertsort(self, arr, new=False):
        if new:
            # 复制原列表，避免修改原列表
            new_arr = arr[:]
            n = len(new_arr)
            # 外层循环控制排序的轮数
            for i in range(1, n):
                # 假设当前元素需要插入到已排序部分的合适位置
                key = new_arr[i]
                j = i - 1
                # 内层循环找到插入位置
                while j >= 0 and new_arr[j] > key:
                    new_arr[j + 1] = new_arr[j]
                    j -= 1
                # 将当前元素插入到合适位置
                new_arr[j + 1] = key
            return new_arr
        else:
            n = len(arr)
            # 外层循环控制排序的轮数
            for i in range(1, n):
                # 假设当前元素需要插入到已排序部分的合适位置
                key = arr[i]
                j = i - 1
                # 内层循环找到插入位置
                while j >= 0 and arr[j] > key:
                    arr[j + 1] = arr[j]
                    j -= 1
                # 将当前元素插入到合适位置
                arr[j + 1] = key

    def quicksort(self, arr, new=False):
        if new:
            # 复制原列表，避免修改原列表
            new_arr = arr[:]
            n = len(new_arr)
            # 递归终止条件：如果数组长度小于等于1，直接返回
            if n <= 1:
                return new_arr
            # 选择基准元素
            pivot = new_arr[n // 2]
            # 划分左子数组和右子数组
            left = [x for x in new_arr if x < pivot]
            middle = [x for x in new_arr if x == pivot]
            right = [x for x in new_arr if x > pivot]
            # 递归排序左子数组和右子数组，并将结果合并
            return self.quicksort(left, new=True) + middle + self.quicksort(right, new=True)
        else:
            n = len(arr)
            # 递归终止条件：如果数组长度小于等于1，直接返回
            if n <= 1:
                return arr
            # 选择基准元素
            pivot = arr[n // 2]
            # 划分左子数组和右子数组
            left = [x for x in arr if x < pivot]
            middle = [x for x in arr if x == pivot]
            right = [x for x in arr if x > pivot]
            # 递归排序左子数组和右子数组，并将结果合并
            return self.quicksort(left, new=False) + middle + self.quicksort(right, new=False)

    
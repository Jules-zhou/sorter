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
            def _quicksort_inplace(arr, low, high):
                if low < high:
                    pi = self._partition(arr, low, high)
                    _quicksort_inplace(arr, low, pi - 1)
                    _quicksort_inplace(arr, pi + 1, high)
            _quicksort_inplace(arr, 0, len(arr) - 1)

    def _partition(self, arr, low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] <= pivot:
                i = i + 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def mergesort(self, arr, new=False):
        if new:
            # 复制原列表，避免修改原列表
            new_arr = arr[:]
            n = len(new_arr)
            # 递归终止条件：如果数组长度小于等于1，直接返回
            if n <= 1:
                return new_arr
            # 划分左子数组和右子数组
            mid = n // 2
            left = new_arr[:mid]
            right = new_arr[mid:]
            # 递归排序左子数组和右子数组
            left_sorted = self.mergesort(left, new=True)
            right_sorted = self.mergesort(right, new=True)
            # 合并排序后的左子数组和右子数组
            return self._merge(left_sorted, right_sorted)
        else:
            def _mergesort_inplace(arr, low, high):
                if low < high:
                    mid = (low + high) // 2
                    _mergesort_inplace(arr, low, mid)
                    _mergesort_inplace(arr, mid + 1, high)
                    self._merge_inplace(arr, low, mid, high)
            _mergesort_inplace(arr, 0, len(arr) - 1)

    def _merge_inplace(self, arr, low, mid, high):
        # 创建临时数组存储左半部分
        left = arr[low:mid + 1]
        i = j = 0
        k = low
        while i < len(left) and j < high - mid:
            if left[i] <= arr[mid + 1 + j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = arr[mid + 1 + j]
                j += 1
            k += 1
        # 将左半部分剩余元素复制回原数组
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

    def _merge(self, left, right):
        # 合并两个已排序的子数组
        merged = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
        # 将剩余的元素添加到合并数组中
        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged
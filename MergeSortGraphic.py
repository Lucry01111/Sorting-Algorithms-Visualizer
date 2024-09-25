import matplotlib.pyplot as plt
import numpy as np
import time

def merge_sort_visualize(arr):
    n = len(arr)
    fig, ax = plt.subplots(figsize=(10, 6))

    def update_plot(arr, left, right, swaps):
        ax.clear()
        bars = ax.bar(range(len(arr)), arr, color=plt.get_cmap('viridis')(np.linspace(0, 1, len(arr))))
        ax.set_ylim(0, max(arr) + 1)
        ax.set_title(f"Merge Sort Swaps: {swaps[0]}")
        ax.set_xlabel('Index')
        ax.set_ylabel('Value')

        for i in range(left, right + 1):
            bars[i].set_color('red')
        plt.draw()
        plt.pause(0.5)

    def merge(arr, left, mid, right, swaps):
        L = arr[left:mid + 1]
        R = arr[mid + 1:right + 1]
        i = j = 0
        k = left
        
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
                swaps[0] += 1
            k += 1
            update_plot(arr, left, right, swaps)
        
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
            update_plot(arr, left, right, swaps)
        
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
            update_plot(arr, left, right, swaps)

    def merge_sort(arr, left, right, swaps):
        if left < right:
            mid = (left + right) // 2
            merge_sort(arr, left, mid, swaps)
            merge_sort(arr, mid + 1, right, swaps)
            merge(arr, left, mid, right, swaps)
            update_plot(arr, left, right, swaps)
            time.sleep(0.5)

    swaps = [0]
    update_plot(arr, 0, n - 1, swaps)
    merge_sort(arr, 0, n - 1, swaps)

    plt.show(block=False)
    plt.pause(1) 
    plt.close() 

def get_user_input():
    while True:
        try:
            print("Warning: Do not close the window during the animation. The window will automatically close a few seconds after the process is complete.")
            user_input = input("Enter a list of numbers separated by spaces (e.g., 64 34 25 12 22 11 90): ")
            arr = list(map(int, user_input.split()))
            if len(arr) < 2:
                print("The list must contain at least two numbers.")
                continue
            return arr
        except ValueError:
            print("Please enter only integers separated by spaces.")

arr = get_user_input()
merge_sort_visualize(arr)
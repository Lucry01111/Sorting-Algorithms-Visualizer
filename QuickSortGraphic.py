import matplotlib.pyplot as plt
import numpy as np
import time

def quick_sort_visualize(arr):
    n = len(arr)
    fig, ax = plt.subplots(figsize=(10, 6))
    
    def update_plot(arr, low, high, swaps):
        ax.clear()
        bars = ax.bar(range(len(arr)), arr, color=plt.get_cmap('viridis')(np.linspace(0, 1, len(arr))))
        ax.set_ylim(0, max(arr) + 1)
        ax.set_title(f"Quick Sort | Swaps: {swaps}")
        ax.set_xlabel('Index')
        ax.set_ylabel('Value')
        for i in range(low, high + 1):
            bars[i].set_color('red')
        plt.draw()
        plt.pause(0.5)
    
    def partition(arr, low, high, swaps):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            update_plot(arr, low, high, swaps)
            if arr[j] < pivot:
                i += 1
                if arr[i] != arr[j]: 
                    arr[i], arr[j] = arr[j], arr[i]
                    swaps += 1  
        if arr[i + 1] != arr[high]:  
            arr[i + 1], arr[high] = arr[high], arr[i + 1]
            swaps += 1  
        update_plot(arr, low, high, swaps)
        return i + 1, swaps

    def quick_sort(arr, low, high, swaps):
        if low < high:
            pi, swaps = partition(arr, low, high, swaps)
            swaps = quick_sort(arr, low, pi - 1, swaps)
            swaps = quick_sort(arr, pi + 1, high, swaps)
            update_plot(arr, low, high, swaps)
            time.sleep(0.5)
        return swaps

    swaps = 0
    update_plot(arr, 0, n - 1, swaps)
    swaps = quick_sort(arr, 0, n - 1, swaps)

    plt.show(block=False)
    plt.pause(1)
    plt.close()

def get_user_input():
    while True:
        try:
            print("Warning: Do not close the window during the animation. It will close automatically after the process finishes.")
            user_input = input("Enter a list of numbers separated by spaces (e.g., 64 34 25 12 22 11 90): ")
            arr = list(map(int, user_input.split()))
            if len(arr) < 2:
                print("The list must contain at least two numbers.")
                continue
            return arr
        except ValueError:
            print("Please enter only integers separated by spaces.")

arr = get_user_input()
quick_sort_visualize(arr)
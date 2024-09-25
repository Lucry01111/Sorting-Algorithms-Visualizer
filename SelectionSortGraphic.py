import matplotlib.pyplot as plt
import numpy as np
import time

def selection_sort_visualize(arr):
    n = len(arr)
    fig, ax = plt.subplots(figsize=(10, 6))

    def update_plot(arr, i, min_idx, swaps):
        ax.clear()
        bars = ax.bar(range(len(arr)), arr, color=plt.get_cmap('viridis')(np.linspace(0, 1, len(arr))))
        ax.set_ylim(0, max(arr) + 1)
        ax.set_title(f"Selection Sort | Swaps: {swaps}")
        ax.set_xlabel('Index')
        ax.set_ylabel('Value')
        bars[i].set_color('blue')
        bars[min_idx].set_color('red')
        plt.draw()
        plt.pause(0.5)

    swaps = 0
    update_plot(arr, 0, 0, swaps)
    time.sleep(1)

    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            update_plot(arr, i, min_idx, swaps)
            if arr[j] < arr[min_idx]:
                min_idx = j
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            swaps += 1
            update_plot(arr, i, min_idx, swaps)
            time.sleep(0.5)

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
selection_sort_visualize(arr)
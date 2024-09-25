import matplotlib.pyplot as plt
import numpy as np
import time

def bubble_sort_visualize(arr):
    n = len(arr)
    fig, ax = plt.subplots(figsize=(10, 6))
    
    def update_plot(arr, swaps):
        ax.clear()
        bars = ax.bar(range(len(arr)), arr, color=plt.get_cmap('viridis')(np.linspace(0, 1, len(arr))))
        ax.set_ylim(0, max(arr) + 1)
        ax.set_title(f"Bubble Sort | Swaps: {swaps}")
        ax.set_xlabel('Index')
        ax.set_ylabel('Value')
        plt.draw()
        plt.pause(0.5)
    swaps = 0
    
    update_plot(arr, swaps) 
    time.sleep(1) 

    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
                swaps += 1
                update_plot(arr, swaps)
        if not swapped:
            break

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
bubble_sort_visualize(arr)
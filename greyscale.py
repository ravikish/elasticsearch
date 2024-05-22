import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# Load the grayscale image
img = Image.open('gray_cat.png').convert('L')
img_arr = np.array(img)

# Calculate the total number of numbers needed to store or transmit the original image
total_numbers_original = img_arr.size
print("Number of numbers needed to store or transmit the original image:", total_numbers_original)

# Display the original image
plt.imshow(img_arr, cmap='gray')
plt.title(f'Original Image\nNumbers needed: {total_numbers_original}')
plt.show()

# Perform Singular Value Decomposition (SVD)
U, S, Vt = np.linalg.svd(img_arr)

# Function to compress the image to a given rank, display, and print the number of numbers needed
def compress_and_display(rank):
    compressed_img_arr = np.dot(U[:, :rank], np.dot(np.diag(S[:rank]), Vt[:rank, :]))
    plt.imshow(compressed_img_arr, cmap='gray')
    plt.title(f'Compressed Image (Rank {rank})')
    plt.text(10, 20, f'Numbers needed: {U[:, :rank].size + S[:rank].size + Vt[:rank, :].size}', color='red')
    plt.show()

# Reduce the image to rank 300 and display
compress_and_display(300)

# Reduce the image to rank 100 and display
compress_and_display(100)

# Reduce the image to rank 50 and display
compress_and_display(50)

# Reduce the image to rank 10 and display
compress_and_display(10)

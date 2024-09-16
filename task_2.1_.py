from PIL import Image
import time

# Load the uploaded image

image = Image.open('chapter1.jpg')

# Generate the number (n) based on the current time
current_time = int(time.time())
generated_number = (current_time % 100) + 50

# Ensure the number is even
if generated_number % 2 == 0:
    generated_number += 10

print("Generated number n = ", generated_number)

# Convert the image to RGB if it's not in that mode
image = image.convert("RGB")
pixels = image.load()
width, height = image.size

# Initialize a variable to hold the sum of all red (r) pixel values
red_pixel_sum = 0

# Process the pixels
for x in range(width):
    for y in range(height):
        r, g, b = pixels[x, y]  # Get pixel value (R, G, B)
        
        # Modify the pixel values by adding the generated number (n)
        new_r = min(r + generated_number, 255)  # Ensure the value stays within [0, 255]
        new_g = min(g + generated_number, 255)
        new_b = min(b + generated_number, 255)
        
        # Update the pixel with new values
        pixels[x, y] = (new_r, new_g, new_b)
        
        # Add the new red value to the sum
        red_pixel_sum += new_r

# Save the modified image as 'chapter1out.png'

image.save('chapter1out.png')

# Output the sum of all red pixels and the path to the new image
print(red_pixel_sum)

# Github link https://github.com/Shantanu-Barua/HIT137_asgn2.git 
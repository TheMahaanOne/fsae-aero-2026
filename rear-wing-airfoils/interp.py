import sys
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import splprep, splev
from pathlib import Path

# CHANGE THE THRESHOLD ANGLE BY CHANGING THE "MAX_ANGLE_DEG" VARIABLE BELOW

# Function to calculate angles between three consecutive points
def calculate_angle(p1, p2, p3):
    v1 = p2 - p1
    v2 = p3 - p2
    cos_theta = np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))
    cos_theta = np.clip(cos_theta, -1.0, 1.0)  # Handle floating-point precision issues
    angle = np.arccos(cos_theta)
    return np.degrees(angle)

# Function to refine points based on maximum allowable angle
def refine_points(x, y, max_angle_deg):
    points = np.column_stack((x, y))
    refined_points = [points[0]]  # Start with the first point

    for i in range(1, len(points) - 1):
        p1 = refined_points[-1]
        p2 = points[i]
        p3 = points[i + 1]
        angle = calculate_angle(p1, p2, p3)
        if angle > max_angle_deg:
            refined_points.append(p2)

    refined_points.append(points[-1])  # Add the last point
    refined_points = np.array(refined_points)
    return refined_points[:, 0], refined_points[:, 1]

# Set the maximum allowable angle in degrees (modifiable directly in the script)
MAX_ANGLE_DEG = 0.35  # Change this value to set the maximum angle

# Check if a filename was provided via command-line argument
if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    filename = input("Enter the name of the file (with extension, e.g., 'Be122-125.txt'): ")

# Load coordinates. Accepts plain two-column files (.txt/.dat: x y) and
# CAD-style .asc files written as 'X <x> Y <y> Z <z>', where the profile
# lies in the X-Z plane (Y = 0).
def load_coordinates(path):
    pts = []
    with open(path) as f:
        for line in f:
            nums = []
            for tok in line.replace(',', ' ').split():
                try:
                    nums.append(float(tok))
                except ValueError:
                    pass  # skips labels such as X, Y, Z and header text
            if len(nums) == 2:
                pts.append(nums)
            elif len(nums) == 3:
                pts.append([nums[0], nums[2]])  # X and Z
    return np.array(pts)

data = load_coordinates(filename)
x, y = data[:, 0], data[:, 1]

# Fit a cubic spline and generate initial fine points
tck, _ = splprep([x, y], s=0, k=3)
spline_points = np.linspace(0, 1, 5000)  # Generate fine points for initial sampling
spline_x, spline_y = splev(spline_points, tck)

# Refine the points based on the maximum angle
refined_x, refined_y = refine_points(spline_x, spline_y, MAX_ANGLE_DEG)

# Set output filename based on input filename
output_filename = f"{Path(filename).stem}_interpolated.txt"
np.savetxt(output_filename, np.c_[refined_x, refined_y])

# Plot the original data points and the refined spline
plt.figure(figsize=(10, 5))
plt.plot(x, y, 'o', label='Original Data Points')
plt.plot(refined_x, refined_y, 'r', label='Refined Spline')
plt.xlim([-0.1, 1.1])
plt.axis('equal')
plt.legend()
plt.xlabel("X")
plt.ylabel("Y")
plt.title(f"Cubic Spline with Angle Constraint ({MAX_ANGLE_DEG}°)")
plt.savefig(f"{Path(filename).stem}_interpolated.png", dpi=150)
plt.show()
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("students.csv")

print("First 5 Records")
print(data.head())

average_marks = data["Marks"].mean()
print("\nAverage Marks:", average_marks)

plt.bar(data["Name"], data["Marks"])
plt.title("Student Marks")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show(block=True)

plt.scatter(data["Age"], data["Marks"])
plt.title("Age vs Marks")
plt.xlabel("Age")
plt.ylabel("Marks")
plt.show(block=True)

correlation = data.corr(numeric_only=True)

plt.imshow(correlation)
plt.colorbar()
plt.title("Heatmap")
plt.show(block=True)
import numpy as np

# First experiment
rng1 = np.random.default_rng(42)
a = rng1.normal(50, 10, 1000)

mean1 = np.mean(a)
median1 = np.median(a)
std1 = np.std(a)
minimum1 = np.min(a)
maximum1 = np.max(a)

lower1 = mean1 - std1
upper1 = mean1 + std1

inside1 = np.sum((a >= lower1) & (a <= upper1))
percentage1 = (inside1 / 1000) * 100

print("First Experiment")
print("Mean:", mean1)
print("Median:", median1)
print("Standard Deviation:", std1)
print("Minimum:", minimum1)
print("Maximum:", maximum1)
print("Percentage inside one standard deviation:", percentage1)

# Second experiment with a different seed
rng2 = np.random.default_rng(123)
b = rng2.normal(50, 10, 1000)

mean2 = np.mean(b)
median2 = np.median(b)
std2 = np.std(b)
minimum2 = np.min(b)
maximum2 = np.max(b)

lower2 = mean2 - std2
upper2 = mean2 + std2

inside2 = np.sum((b >= lower2) & (b <= upper2))
percentage2 = (inside2 / 1000) * 100

print("\nSecond Experiment")
print("Mean:", mean2)
print("Median:", median2)
print("Standard Deviation:", std2)
print("Minimum:", minimum2)
print("Maximum:", maximum2)
print("Percentage inside one standard deviation:", percentage2)

# Compare the results
print("\nComparison")
print("Difference between means:", abs(mean1 - mean2))
print("Difference between standard deviations:", abs(std1 - std2))
print("Difference between percentages:", abs(percentage1 - percentage2))
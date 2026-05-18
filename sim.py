import numpy as np
import matplotlib.pyplot as plt
import os

# ============================================================
# USER CONFIGURATION
# ============================================================
n_samples = 1000
mean      = 0
std       = 1
seed      = 42
# ============================================================

os.makedirs("figures", exist_ok=True)

np.random.seed(seed)
data = np.random.normal(loc=mean, scale=std, size=n_samples)

plt.figure(figsize=(8, 5))
plt.hist(data, bins=30, color="steelblue", edgecolor="white")
plt.title(f"Normal Distribution  (n={n_samples}, mean={mean}, std={std})")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("figures/normal_histogram.png", dpi=150)
plt.close()

print("Plot saved to figures/normal_histogram.png")

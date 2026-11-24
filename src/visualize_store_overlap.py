
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

INPUT_FILE = "reports/store_pair_overlap.csv"
OUTPUT_DIR = "reports/figures"

os.makedirs(OUTPUT_DIR, exist_ok=True)

df = pd.read_csv(INPUT_FILE)

stores = sorted(set(df["StoreA"]) | set(df["StoreB"]))

matrix = pd.DataFrame(
    np.zeros((len(stores), len(stores))),
    index=stores,
    columns=stores
)

for _, row in df.iterrows():
    a = row["StoreA"]
    b = row["StoreB"]
    value = row["OverlapPercentage"]

    matrix.loc[a, b] = value
    matrix.loc[b, a] = value

for store in stores:
    matrix.loc[store, store] = 100

fig, ax = plt.subplots(figsize=(9, 7))

image = ax.imshow(matrix.values, cmap="YlOrRd", vmin=0, vmax=100)

ax.set_xticks(range(len(stores)))
ax.set_yticks(range(len(stores)))
ax.set_xticklabels(stores)
ax.set_yticklabels(stores)

ax.set_title(
    "Store-to-Store Device Overlap Heatmap",
    fontsize=15,
    fontweight="bold"
)

ax.set_xlabel("Store")
ax.set_ylabel("Store")

for i in range(len(stores)):
    for j in range(len(stores)):
        ax.text(
            j, i,
            f"{matrix.iloc[i, j]:.1f}%",
            ha="center",
            va="center",
            color="black",
            fontweight="bold"
        )

colorbar = fig.colorbar(image, ax=ax)
colorbar.set_label("Jaccard Similarity (%)")

plt.tight_layout()

output_file = os.path.join(
    OUTPUT_DIR,
    "store_overlap_heatmap.png"
)

plt.savefig(output_file, dpi=300, bbox_inches="tight")
plt.close()

print("Store overlap heatmap generated successfully!")
print(f"Saved to: {output_file}")

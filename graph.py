import matplotlib.pyplot as plt

# -------------------------------------------------------
# DATA (from Table III - Drift Reduction Analysis)
# -------------------------------------------------------
cluster_nodes = [3, 5, 7, 9, 11]

drift_before = [0.42, 0.57, 0.69, 0.81, 0.93]
drift_after = [0.18, 0.24, 0.31, 0.36, 0.41]

# -------------------------------------------------------
# VALIDATION
# -------------------------------------------------------
def validate_data():
    if not (len(cluster_nodes) == len(drift_before) == len(drift_after)):
        raise ValueError("Mismatch in dataset lengths")
    print("Validation successful")

validate_data()

# -------------------------------------------------------
# CALCULATE DRIFT REDUCTION (%)
# -------------------------------------------------------
def calculate_reduction(before, after):
    reduction = []
    for b, a in zip(before, after):
        percent = ((b - a) / b) * 100
        reduction.append(round(percent, 2))
    return reduction

reduction_percent = calculate_reduction(drift_before, drift_after)

# Print reduction values
print("\nDrift Reduction (%):")
for n, r in zip(cluster_nodes, reduction_percent):
    print(f"Nodes {n}: {r}%")

# -------------------------------------------------------
# PLOTTING FUNCTION
# -------------------------------------------------------
def plot_drift_comparison():
    plt.figure(figsize=(10, 6))

    # Before Sync line
    plt.plot(cluster_nodes, drift_before,
             marker='o', linewidth=2,
             label='Drift Before Synchronization')

    # After Sync line
    plt.plot(cluster_nodes, drift_after,
             marker='o', linewidth=2,
             label='Drift After Synchronization')

    # Labels
    plt.xlabel("Cluster Nodes", fontsize=12)
    plt.ylabel("Drift Value", fontsize=12)
    plt.title("Drift Reduction Comparison", fontsize=14)

    # Grid
    plt.grid(True)

    # Legend
    plt.legend()

    # Annotate points
    for i in range(len(cluster_nodes)):
        plt.text(cluster_nodes[i], drift_before[i],
                 str(drift_before[i]), ha='right', fontsize=9)
        plt.text(cluster_nodes[i], drift_after[i],
                 str(drift_after[i]), ha='left', fontsize=9)

    plt.tight_layout()

# -------------------------------------------------------
# SAVE GRAPH
# -------------------------------------------------------
def save_graph():
    plt.savefig("drift_comparison.png", dpi=300)
    print("\nGraph saved as drift_comparison.png")

# -------------------------------------------------------
# EXECUTION
# -------------------------------------------------------
plot_drift_comparison()
save_graph()

plt.show()

# -------------------------------------------------------
# SUMMARY OUTPUT
# -------------------------------------------------------
def summary():
    avg_reduction = round(sum(reduction_percent) / len(reduction_percent), 2)

    print("\nSUMMARY")
    print("--------")
    print("Drift increases with cluster size before synchronization.")
    print("Adaptive synchronization significantly reduces drift.")
    print(f"Average Drift Reduction: {avg_reduction}%")

summary()

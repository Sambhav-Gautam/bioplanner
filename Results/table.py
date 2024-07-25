import matplotlib.pyplot as plt
import pandas as pd

# Data
data = {
    "function_precision": {
        "mean": 0.99,
        "standard_deviation": 0.03,
        "average": 0.99
    },
    "recall_funcs": {
        "mean": 0.98,
        "standard_deviation": 0.04,
        "average": 0.98
    },
    "precision_args": {
        "mean": 0.8,
        "standard_deviation": 0.28,
        "average": 0.8
    },
    "recall_args": {
        "mean": 0.97,
        "standard_deviation": 0.08,
        "average": 0.97
    },
    "args_similarity": {
        "mean": 0.86,
        "standard_deviation": 0.11,
        "average": 0.86
    },
    "args_bleu": {
        "mean": 0.2,
        "standard_deviation": 0.14,
        "average": 0.2
    },
    "levenshtein_distance": {
        "mean": 0.74,
        "standard_deviation": 0.42,
        "average": 0.74
    },
    "scaled_levenshtein_distance": {
        "mean": 0.18,
        "standard_deviation": 0.12,
        "average": 0.18
    }
}
# Convert data to DataFrame
df = pd.DataFrame.from_dict(data, orient='index')

# Round values for better readability
df = df.round(2)

# Plotting
plt.figure(figsize=(10, 6))
plt.bar(df.index, df['mean'], yerr=df['standard_deviation'], capsize=5, color='skyblue', alpha=0.7)
plt.xlabel('Metrics')
plt.ylabel('Mean Values')
plt.title('Evaluation Metrics')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

# Save plot as PNG
plt.savefig('evaluation_metrics_plot_FeedbackAndShuffled.png')

# Display and save table as PNG
fig, ax = plt.subplots(figsize=(10, 6))
ax.axis('off')
ax.table(cellText=df.values, colLabels=df.columns, rowLabels=df.index, loc='center', cellLoc='center')
fig.tight_layout()
plt.savefig('evaluation_metrics_table_FeedbackAndShuffled.png')

# Show plot
plt.show()

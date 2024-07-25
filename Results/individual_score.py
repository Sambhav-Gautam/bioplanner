import json
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Read the JSON file
file_path = 'C:\\Users\\sambh\\bioplanner\\Results\\functionEvaluation.json'  # replace with your file path
with open(file_path, 'r') as file:
    data = json.load(file)

# Step 2: Extract precision and recall values
precision_values = [entry['function_precision'] for entry in data]
recall_values = [entry['recall_funcs'] for entry in data]

# Step 3: Calculate mean, average, and standard deviation
precision_mean = np.mean(precision_values)
recall_mean = np.mean(recall_values)

precision_std = np.std(precision_values)
recall_std = np.std(recall_values)

# Step 4: Create the graph
fig, ax = plt.subplots()

metrics = ['Precision', 'Recall']
means = [precision_mean, recall_mean]
stds = [precision_std, recall_std]

# Plotting the bar chart
bar_width = 0.4
ax.bar(metrics, means, yerr=stds, capsize=10, color=['blue', 'orange'], alpha=0.7, width=bar_width)

# Adding the values on top of the bars
for i, v in enumerate(means):
    ax.text(i, v + 0.01, f'{v:.2f}', ha='center', va='bottom')

# Plotting individual precision and recall scores
ax.scatter(['Precision']*len(precision_values), precision_values, color='blue', label='Individual Precision Scores', alpha=0.6)
ax.scatter(['Recall']*len(recall_values), recall_values, color='orange', label='Individual Recall Scores', alpha=0.6)

ax.set_ylabel('Values')
ax.set_title('Mean and Standard Deviation of Precision and Recall with Individual Scores')

# Adding legend
ax.legend()

# Save the plot as a PNG image
plt.savefig('metrics_with_individual_scores.png')

# Display the plot
plt.show()

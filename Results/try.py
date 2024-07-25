import json
import statistics
import pandas as pd
import matplotlib.pyplot as plt

# Load data from JSON file
with open('Results/protocolFeedbackAndShuffled.json', 'r') as f:
    data = json.load(f)

# Initialize lists to store values for calculation
function_precision = []
recall_funcs = []
precision_args = []
recall_args = []
args_similarity = []
args_bleu = []
levenshtein_distance = []
scaled_levenshtein_distance = []

# Extract values from each entry in data
for entry in data:
    function_precision.append(entry['function_precision'])
    recall_funcs.append(entry['recall_funcs'])
    precision_args.append(entry['precision_args'])
    recall_args.append(entry['recall_args'])
    args_similarity.append(entry['args_similarity'])
    args_bleu.append(entry['args_bleu'])
    levenshtein_distance.append(entry['levenshtein_distance'])
    scaled_levenshtein_distance.append(entry['scaled_levenshtein_distance'])

# Calculate mean, standard deviation, and average for each metric
metrics = {
    'function_precision': function_precision,
    'recall_funcs': recall_funcs,
    'precision_args': precision_args,
    'recall_args': recall_args,
    'args_similarity': args_similarity,
    'args_bleu': args_bleu,
    'levenshtein_distance': levenshtein_distance,
    'scaled_levenshtein_distance': scaled_levenshtein_distance
}

results = {}

for metric, values in metrics.items():
    mean = statistics.mean(values)
    sd = statistics.stdev(values)
    average = sum(values) / len(values)
    
    # Round the values to 2 decimal places
    mean = round(mean, 2)
    sd = round(sd, 2)
    average = round(average, 2)
    
    results[metric] = {
        'mean': mean,
        'standard_deviation': sd,
        'average': average
    }

# Save results to a JSON file
with open('metrics_summary_FeedbackAndShuffled.json', 'w') as outfile:
    json.dump(results, outfile, indent=4)

# Create a table using pandas DataFrame
df = pd.DataFrame(results)

# Plotting the table as a PNG file
plt.figure(figsize=(12, 6))  # Adjust figsize as needed
plt.axis('off')
table = plt.table(cellText=df.values,
                  colLabels=df.columns,
                  cellLoc='center',
                  loc='center',
                  cellColours=[['#f2f2f2']*len(df.columns) for _ in range(len(df))],
                  colColours=['#f2f2f2']*len(df.columns),
                  bbox=[0, 0, 2, 2])  # Adjust bbox to fit the table properly
table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(2, 2)  # Adjust table size if needed

plt.savefig('metrics_summary_for_FeedbackAndShuffled_table.png', bbox_inches='tight')
plt.close()

print("Metrics Summary:")
print(df)
print("\nResults saved as 'metrics_summary.json' and 'metrics_summary_table.png'.")

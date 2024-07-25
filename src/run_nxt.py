import json
import glob
import os
from evaluate_metrics import (
    get_PR_funcs,
    get_PR_args,
    get_args_similarity,
    get_args_bleu,
    get_levenshtein_distance,
)

def compute_accuracy(ground_truth, prediction):
    # Compute accuracy of function assignments
    ground_truth_funcs = ground_truth.split("\n")
    prediction_funcs = prediction.split("\n")

    correct_count = 0
    total_functions = len(ground_truth_funcs)

    for gt_func, pred_func in zip(ground_truth_funcs, prediction_funcs):
        if gt_func.strip() == pred_func.strip():
            correct_count += 1

    accuracy = (correct_count / total_functions) * 100
    return accuracy

if __name__ == "__main__":
    evaluation_folder = "./src/to_evaluate/*.json"
    results = []

    for f in glob.glob(evaluation_folder):
        with open(f, "r") as file:
            data = json.load(file)
            id = data["id"]
            model_name = data["model_name"]
            ground_truth = data["ground_truth"]
            prediction_code = data["prediction_code"]
            prediction_functions = data["prediction_functions"]
            prediction = f"{prediction_functions}\n{prediction_code}"

            levenshtein_distance = get_levenshtein_distance(
                prediction_functions, ground_truth, prediction
            )
            scaled_levenshtein_distance = levenshtein_distance / len(
                ground_truth.split("\n")
            )

            precision_funcs, recall_funcs = get_PR_funcs(ground_truth, prediction)
            precision_args, recall_args = get_PR_args(ground_truth, prediction)

            args_similarity = get_args_similarity(ground_truth, prediction)

            args_bleu = get_args_bleu(ground_truth, prediction)

            # Compute accuracy
            accuracy = compute_accuracy(ground_truth, prediction)

            # Define model shuffle functions
            shuffle_functions = model_name.startswith("GPT-3.5")

            results.append(
                {
                    "id" : id,
                    "Model": model_name,
                    "Shuffle Functions": "✓",
                    "Accuracy": f"{accuracy:.1f}",
                    "Precision": f"{precision_args:.1f} ",
                    "Recall": f"{recall_args:.1f} ",
                    "SciBERTScore": f"{args_similarity:.1f}",
                    "BLEU": f"{args_bleu:.3f} ",
                }
            )

    # Prepare results for appending to JSON file
    results_dir = "./Results"
    os.makedirs(results_dir, exist_ok=True)
    results_file_path = os.path.join(results_dir, "nextstepprediction.json")

    if os.path.exists(results_file_path):
        with open(results_file_path, "r") as f:
            existing_results = json.load(f)
    else:
        existing_results = []

    existing_results.extend(results)

    with open(results_file_path, "w") as f:
        json.dump(existing_results, f, indent=4)

    print(f"Results appended to {results_file_path}")



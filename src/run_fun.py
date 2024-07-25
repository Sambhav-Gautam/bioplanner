import json
import glob
import os
from evaluate_metrics import (
    get_PR_funcs
)

if __name__ == "__main__":
    evaluation_folder = "./src/to_evaluate/*.json"
    results = []

    for f in glob.glob(evaluation_folder):
        with open(f, "r") as file:
            data = json.load(file)
            id = data["id"]
            model_name = data["model_name"] 
            ground_truth = data["prediction_functions"]
            prediction_functions = data["prediction_code"]

            precision_funcs, recall_funcs = get_PR_funcs(ground_truth, prediction_functions)

            

            results.append(
                {
                    "model": model_name,
                    "id": id,
                    "function_precision": precision_funcs,
                    "recall_funcs": recall_funcs
                }
            )

    results_dir = "./Results"
    os.makedirs(results_dir, exist_ok=True)
    results_file_path = os.path.join(results_dir, "functionEvaluation.json")

    if os.path.exists(results_file_path):
        with open(results_file_path, "r") as f:
            existing_results = json.load(f)
    else:
        existing_results = []

    existing_results.extend(results)

    with open(results_file_path, "w") as f:
        json.dump(existing_results, f, indent=4)

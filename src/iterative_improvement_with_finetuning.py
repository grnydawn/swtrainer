# iterative_improvement_with_finetuning.py
from generate_code import generate_code
from evaluate_code import evaluate_code
from fine_tune_model import fine_tune_model
import json

def iterative_improvement(prompt, iterations=10, fine_tuning_threshold=5):
    best_code = ""
    best_score = 0
    fine_tuning_data = []

    for i in range(iterations):
        code = generate_code(prompt)
        score = evaluate_code(code)
        print(f"Iteration {i+1}: Score {score}")

        if score > best_score:
            best_score = score
            best_code = code

        # Collect data for fine-tuning if the score meets the threshold
        if score >= fine_tuning_threshold:
            fine_tuning_data.append({"prompt": prompt, "code": code})

        # Fine-tune the model after a certain number of iterations
        if (i+1) % fine_tuning_threshold == 0 and fine_tuning_data:
            # Save fine-tuning data to a file
            with open('fine_tuning_data.json', 'w') as f:
                json.dump(fine_tuning_data, f)
            # Fine-tune the model
            fine_tune_model("llama3", 'fine_tuning_data.json', "./fine_tuned_model", epochs=1)
            # Clear the fine-tuning data
            fine_tuning_data = []

    return best_code, best_score

if __name__ == "__main__":
    prompt = "Write a Python function to calculate the factorial of a number."
    best_code, best_score = iterative_improvement(prompt)
    print("Best Code:\n", best_code)
    print("Best Score:", best_score)


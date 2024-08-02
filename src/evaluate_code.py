# evaluate_code.py
import subprocess

def evaluate_code(code):
    try:
        # Save the generated code to a temporary file
        with open("temp_code.py", "w") as f:
            f.write(code)

        # Run the code and capture the output
        result = subprocess.run(["python", "temp_code.py"], capture_output=True, text=True)
        output = result.stdout
        # Define a scoring function (e.g., based on correctness, performance, etc.)
        score = len(output.split("\n")) # Example scoring based on the number of lines of output
        return score
    except Exception as e:
        return 0

if __name__ == "__main__":
    code = """
    def factorial(n):
        if n == 0:
            return 1
        else:
            return n * factorial(n-1)

    print(factorial(5))
    """
    score = evaluate_code(code)
    print(f"Score: {score}")


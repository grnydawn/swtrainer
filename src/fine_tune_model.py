# fine_tune_model.py
from transformers import LlamaForCausalLM, LlamaTokenizer, Trainer, TrainingArguments
import torch

def fine_tune_model(model_name, dataset, output_dir, epochs=1):
    model = LlamaForCausalLM.from_pretrained(model_name)
    tokenizer = LlamaTokenizer.from_pretrained(model_name)

    def tokenize_function(examples):
        return tokenizer(examples['prompt'], padding="max_length", truncation=True)

    tokenized_dataset = dataset.map(tokenize_function, batched=True)
    training_args = TrainingArguments(
        output_dir=output_dir,
        num_train_epochs=epochs,
        per_device_train_batch_size=4,
        save_steps=10_000,
        save_total_limit=2,
        logging_dir='./logs',
    )

    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=tokenized_dataset,
    )

    trainer.train()
    model.save_pretrained(output_dir)

if __name__ == "__main__":
    # Example usage
    from datasets import load_dataset

    # Load your dataset here
    dataset = load_dataset('json', data_files={'train': 'path/to/your/dataset.json'})['train']
    fine_tune_model("llama3", dataset, "./fine_tuned_model")


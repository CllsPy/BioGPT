from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

MODEL_NAME = "microsoft/biogpt"

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(
    MODEL_NAME,
    device_map="auto",
    torch_dtype=torch.float16
)

def generate_answer(question: str, max_length: int = 128) -> str:
    inputs = tokenizer(question, return_tensors="pt").to(model.device)
    outputs = model.generate(**inputs, max_length=max_length)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

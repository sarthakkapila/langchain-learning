import os
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from transformers import AutoModelForCausalLM

# Load the Hugging Face tokenizer and model
tokenizer = AutoTokenizer.from_pretrained("gpt2")
model = AutoModelForCausalLM.from_pretrained("gpt2")

# Define the conversation context
context = "I am looking for a new mattress. Can you help me find one?"

# Define the user input
user_input = "What are the different types of mattresses you have?"

# Generate the agent's response using the Hugging Face model
input_ids = tokenizer(context + user_input, return_tensors="pt").input_ids
output_ids = model.generate(input_ids)
response = tokenizer.batch_decode(output_ids, skip_special_tokens=True)

# Print the agent's response
print(response)
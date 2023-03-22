import openai
from transformers import GPT2LMHeadModel, GPT2Tokenizer

openai.api_key = "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"
response = openai.Completion.create(
  engine="text-davinci-002",
  prompt="Hello, World!",
  max_tokens=512
)
print(response)
print(response.choices[0].text)

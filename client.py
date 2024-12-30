from openai import OpenAI
#This will only work if you have paid plan of openAi
client = OpenAI(
    api_key="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"
)

completion = client.chat.completions.create(
  model="gpt-4o-mini",
  store=True,
  messages=[
    {"role": "user", "content": "what is coding"}
  ]
)

print(completion.choices[0].message)
from mistralai import Mistral

#My API key from Mistral
api_key = "myApiKey"

model = "mistral-small-latest"

client = Mistral(api_key=api_key)

#input text (input text is hard-coded for simplicity)
input_text = """The way in which deep learning and machine learning differ is in how each algorithm learns. "Deep" 
machine learning can use labeled datasets, also known as supervised learning, to inform its algorithm, but it doesn’t 
necessarily require a labeled dataset. The deep learning process can ingest unstructured data in its raw form (e.g., 
text or images), and it can automatically determine the set of features which distinguish different categories of 
data from one another. This eliminates some of the human intervention required and enables the use of large amounts 
of data."""
prompt = f"Please summarize the following text:\n{input_text}"

chat_response = client.chat.complete(
    model=model,
    messages=[
        {
            "role": "user",
            "content": prompt,
        },
    ]
)

print("Summary:", chat_response.choices[0].message.content)

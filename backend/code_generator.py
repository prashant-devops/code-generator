import openai

openai.api_key = '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' 

def generate_code(prompt):
    response = openai.Completion.create(
        engine='text-davinci-003', 
        prompt=f'Generate Python code for: {prompt}',
        max_tokens=500,
        temperature=0.5
    )

    return response['choices'][0]['text'].strip()
import openai

openai.api_key = "YOUR_API_KEY"

def analyze_text(text):
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a compassionate AI helping to identify emotional and cultural themes."},
            {"role": "user", "content": f"Analyze the following text for emotional themes and cultural context:\\n\\n{text}"}
        ],
        max_tokens=300
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    sample_text = "I recently moved to a new country and felt both excited and lonely. The traditions here are different but beautiful."
    print(analyze_text(sample_text))

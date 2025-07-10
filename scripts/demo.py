import openai
import os

# Set your OpenAI API key from an environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

def analyze_text(text):
    response = openai.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a compassionate AI helping to identify emotional and cultural themes."},
            {"role": "user", "content": f"Analyze the following text for emotional themes and cultural context:\n\n{text}"}
        ],
        max_tokens=300
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    # You can edit this sample input text
    sample_text = "I recently moved to a new country and felt both excited and lonely. The traditions here are different but beautiful."

    # Call the AI function
    result = analyze_text(sample_text)

    # Print the result to the console
    print("AI Response:\n")
    print(result)

    # Save the result to output.txt
    with open("output.txt", "w") as f:
        f.write(result)
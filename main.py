from flask import Flask, render_template, request

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Mock AI route (always safe, never calls OpenAI)
@app.route('/ask', methods=['POST'])
def ask_mock_ai():
    user_input = request.form.get('user_input', '')

    # Safe mock response
    mock_response = f"Mock AI response to your query: {user_input}"

    # Log input and response (optional)
    try:
        with open("data.txt", "a") as file:
            file.write(f"Input: {user_input}\nResponse: {mock_response}\n\n")
    except Exception as e:
        print("Could not write to file:", e)

    return render_template('index.html', response=mock_response)

# Other pages
@app.route('/noticeboard')
def noticeboard():
    return render_template('noticeboard.html')

@app.route('/stories')
def stories():
    return render_template('stories.html')

@app.route('/listening-circle')
def listening_circle():
    return render_template('listening-circle.html')

@app.route('/hate-crime')
def hate_crime():
    return render_template('hate-crime.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)

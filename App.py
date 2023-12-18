from openai import OpenAI
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def thala_homepage():
    return render_template('homepage.html')

@app.route('/thala', methods=['POST', 'GET'])
def thala_response():
    input_string = request.form['prompt']
    if input_string:
        prompt = f"""
            You are a creative meme writer from India
            I will give you a input
            You are supposed to find a creative way to derive the number 7 in using the input as reference.
            Become very creative in deriving the relation.
            Get the response in Hinglish (Hindi + English) (Hindi written in english character)
            Don't give any pretext or reference
            Word limit: 15

            Input: {input_string}
        """
        client = OpenAI(api_key="")
        response = client.chat.completions.create(
            model="gpt-4-vision-preview",
            messages=[
                {"role": "assistant", "content": prompt},
            ]
        )
        result = str(response.choices[0].message.content)
        return render_template('outpage.html', result=result)
    else:
        return jsonify({"error": "No input provided"}), 400

@app.route('/out', methods=['POST', 'GET'])
def thala_outpage():
    input_string = request.form['prompt']
    return render_template('outpage.html')

if __name__ == '__main__':
    app.run(debug=True)
#updated ->>
# from flask import Flask, request
# from twilio.twiml.messaging_response import MessagingResponse  # Import Twilio for SMS response
# import openai
# import os

# # Init the Flask App
# app = Flask(__name__)

# # Initialize the OpenAI API key
# openai.api_key = os.environ.get("OPENAI_API_KEY")

# # Define a function to generate answers using GPT-3
# def generate_answer(question):
#     model_engine = "text-davinci-002"
#     prompt = (f"Q: {question}\n"
#               "A:")

#     response = openai.Completion.create(
#         engine=model_engine,
#         prompt=prompt,
#         max_tokens=1024,
#         n=1,
#         stop=None,
#         temperature=0.7,
#     )

#     answer = response.choices[0].text.strip()
#     return answer

# # Define a route to handle incoming requests
# @app.route('/chatgpt', methods=['POST'])
# def chatgpt():
#     incoming_que = request.values.get('Body', '').lower()
#     print("Question: ", incoming_que)

#     # Generate the answer using GPT-3
#     answer = generate_answer(incoming_que)
#     print("BOT Answer: ", answer)

#     bot_resp = MessagingResponse()
#     msg = bot_resp.message()
#     msg.body(answer)

#     return str(bot_resp)

# # Run the Flask app
# if __name__ == '__main__':
#     app.run(host='0.0.0.0', debug=False, port=5000)

# from flask import Flask, request, render_template
# import openai
# import os

# app = Flask(__name__)

# # Initialize the OpenAI API key
# #openai.api_key = os.environ.get("OPENAI_API_KEY")
# os.environ['OPENAI_API_KEY'] = ''
# openai.api_key = os.environ.get("OPENAI_API_KEY")
# #export OPENAI_API_KEY = your-api-key-here



# # Route to render the academic assistance form
# @app.route('/academic_assistance')
# def academic_assistance_form():
#     return render_template('./academic_assistance_form.htm')


# # Define a function to generate answers using GPT-3
# def generate_answer(question):
#     model_engine = "text-davinci-002"
#     prompt = (f"Q: {question}\n"
#               "A:")

#     response = openai.Completion.create(
#         engine=model_engine,
#         prompt=prompt,
#         max_tokens=1024,
#         n=1,
#         stop=None,
#         temperature=0.7,
#     )

#     answer = response.choices[0].text.strip()
#     return answer


# # Define a route to handle incoming requests
# @app.route('/ask_question', methods=['POST'])
# def ask_question():
#     # Retrieve form data
# username = request.form.get('username')
# email = request.form.get('email')
# academic_level = request.form.get('academic_level')
# area_of_interest = request.form.get('area_of_interest')
# question_text = request.form.get('question_text')

#     # Process the form data as needed
#     # You can interact with the OpenAI GPT-3 API here and generate a response
#     # Example: You can call the generate_answer function with the question_text

# answer = generate_answer(question_text)

# return answer


# if __name__ == '__main__':
#     app.run(host='0.0.0.0', debug=False, port=3000)

from flask import Flask, request, render_template, jsonify
import openai
import os
from pymongo import MongoClient

app = Flask(__name__)

# Initialize the OpenAI API key
# You can set the API key using the following line, or use an environment variable as previously mentioned.
#openai.api_key = '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'
os.environ['OPENAI_API_KEY'] = 'key'
#openai.api_key = os.environ.get("OPENAI_API_KEY")



mongo_client = MongoClient('mongodb+srv://aashutosh:password@aashutosh.quykynt.mongodb.net/?retryWrites=true&w=majority')  # Change the MongoDB connection string as needed
db = mongo_client['academic_assistance']
question_collection = db['questions']

# Route to render the academic assistance form
@app.route('/academic_assistance')
def academic_assistance_form():
    return render_template('academic_assistance_form.htm')

# Define a function to generate answers using GPT-3
def generate_answer(question):
    model_engine = "text-davinci-002"
    prompt = (f"Q: {question}\n"
              "A:")

    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )

    answer = response.choices[0].text.strip()
     # Return the answer to the user
    return jsonify({"answer": answer})


# Define a route to handle incoming requests
@app.route('/ask_question', methods=['POST'])
def ask_question():
    # Retrieve form data
    username = request.form.get('username')
    email = request.form.get('email')
    academic_level = request.form.get('academic_level')
    area_of_interest = request.form.get('area_of_interest')
    question_text = request.form.get('question_text')

    # Process the form data as needed
    # You can interact with the OpenAI GPT-3 API here and generate a response
    # Example: You can call the generate_answer function with the question_text
    answer = generate_answer(question_text)

    return answer

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False, port=3001)



# from dotenv import load_dotenv
# load_dotenv() ## loading all the environment variables

# import streamlit as st
# import os
# import google.generativeai as genai
# print("google.generativeai module imported successfully")

# genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# ## function to load Gemini Pro model and get repsonses
# model=genai.GenerativeModel("gemini-pro") 
# chat = model.start_chat(history=[])
# def get_gemini_response(question):
    
#     response=chat.send_message(question,stream=True)
#     return response

# ##initialize our streamlit app

# st.set_page_config(page_title="Q&A Demo")

# st.header("Gemini LLM Application")

# # Initialize session state for chat history if it doesn't exist
# if 'chat_history' not in st.session_state:
#     st.session_state['chat_history'] = []

# input=st.text_input("Input: ",key="input")
# submit=st.button("Ask the question")

# if submit and input:
#     response=get_gemini_response(input)
#     # Add user query and response to session state chat history
#     st.session_state['chat_history'].append(("You", input))
#     st.subheader("The Response is")
#     for chunk in response:
#         st.write(chunk.text)
#         st.session_state['chat_history'].append(("Sehat Sahayak", chunk.text))
# st.subheader("The Chat History is")
    
# for role, text in st.session_state['chat_history']:
#     st.write(f"{role}: {text}")
    

# from dotenv import load_dotenv
# import streamlit as st
# import os
# import google.generativeai as genai

# # Load environment variables
# load_dotenv()

# # Configure Google Generative AI
# genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
# model = genai.GenerativeModel("gemini-pro")
# chat = model.start_chat(history=[])

# # Function to get responses from the Gemini model
# def get_gemini_response(question):
#     response = chat.send_message(question, stream=True)
#     return response

# # Initialize Streamlit app
# st.set_page_config(page_title="Q&A Demo")

# st.header("Healthcare Assistant")

# # Initialize session state for chat history if it doesn't exist
# if 'chat_history' not in st.session_state:
#     st.session_state['chat_history'] = []

# # Input box for user queries
# input = st.text_input("Ask your question:", key="input")
# submit = st.button("Submit")

# if submit and input:
#     response=get_gemini_response(input)
#     # Add user query and response to session state chat history
#     st.session_state['chat_history'].append(("You", input))
#     st.subheader("The Response is")
#     for chunk in response:
#         st.write(chunk.text)
#         st.session_state['chat_history'].append(("Sehat Sahayak", chunk.text))
# # Display the chat history in a sidebar
# with st.sidebar:
#     st.subheader("Chat History")
#     for role, text in st.session_state['chat_history']:
#         st.write(f"{role}: {text}")

# # Styling for a better chatbox experience
# st.markdown("""
# <style>
#     .chat-container {
#         max-height: 400px;
#         overflow-y: auto;
#         border: 1px solid #ccc;
#         padding: 10px;
#         margin-bottom: 10px;
#     }
#     .chat-message {
#         margin-bottom: 5px;
#         padding: 10px;
#         border-radius: 5px;
#     }
#     .chat-message.user {
#         background-color: #e0f7fa;
#         text-align: left;
#     }
#     .chat-message.bot {
#         background-color: #fff9c4;
#         text-align: left;
#     }
# </style>
# """, unsafe_allow_html=True)

%%writefile app.py
import streamlit as st
import random
import time
import string

# Define intent labels
intent_labels = {
    0: "greetings",
    1: "product_search",
    2: "order_status",
    3: "return_policy",
    4: "complaint",
    5: "farewell"
}

# Preprocess Input Function
def preprocess_input(user_input):
    return user_input.lower().strip()  # Convert to lowercase and remove extra spaces

# Get Intent Prediction (This part should already be working with the model)
def get_intent(user_input):
    # Placeholder for the actual model prediction (replace with your model)
    input_vector = vectorizer.transform([user_input])  # Convert the input into a vector
    dense_input = input_vector.toarray()  # Convert sparse matrix to dense
    prediction = hb_model.predict(dense_input)  # Predict the intent
    predicted_intent = prediction[0]  # Get the predicted class (numeric)
    return intent_labels.get(predicted_intent, "unknown")  # Map to intent

# Helper function to simulate order tracking
def track_order(order_number):
    status_messages = [
        f"Order {order_number} has been dispatched and is on its way to you.",
        f"Order {order_number} is out for delivery. You can expect it soon.",
        f"Order {order_number} has been delayed. We apologize for the inconvenience.",
        f"Order {order_number} has been successfully delivered. Enjoy your product!",
        f"Order {order_number} is in transit. Please check back later for updates."
    ]
    return random.choice(status_messages)

# Function to generate a random meeting link
def generate_meeting_link():
    random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=10))  # Generate a random 10-character string
    return f"https://meet.google.com/{random_string}"

# Function to simulate complaint handling
def handle_complaint(product_name, issue):
    resolution_messages = [
        f"Thank you for reporting the issue with {product_name}. Our team will investigate and get back to you.",
        f"We are sorry for the inconvenience caused by {product_name}. You can contact the seller for further assistance.",
        f"Your complaint regarding {product_name} has been received. A video call with the seller is available to resolve this. Here is your meeting link: {generate_meeting_link()}",
        f"The issue with {product_name} has been noted. A support ticket has been created for immediate resolution. You can also schedule a video call with the seller here: {generate_meeting_link()}"
    ]
    return random.choice(resolution_messages)

# Streamlit app layout
st.title("Amazon Chatbot")

# Text input for the user to ask a question
user_input = st.text_input("Ask me anything about your order or Amazon services:")

if user_input:
    # Preprocess the input
    user_input = preprocess_input(user_input)

    # Get the intent prediction (this needs to be connected to your actual model)
    intent = get_intent(user_input)

    # Main chatbot flow based on intent
    if intent == "greetings":
        st.write("Amazon Chatbot: Hello! How can I assist you today?")

    elif intent == "order_status":
        order_number = st.text_input("Please provide your order number:")
        if order_number:
            order_status = track_order(order_number)  # Simulate order status
            st.write(f"Amazon Chatbot: {order_status}")

    elif intent == "complaint":
        order_number = st.text_input("Please provide your order number:")
        if order_number:
            st.write(f"Amazon Chatbot: Checking details for order {order_number}.")

            # Ask for product name and issue description
            product_name = st.text_input("Please tell me the product name:")
            issue = st.text_input("Please describe the issue you're facing:")

            if product_name and issue:
                # Handle the complaint
                resolution_message = handle_complaint(product_name, issue)
                st.write(f"Amazon Chatbot: {resolution_message}")

                # Ask for rating after resolution
                rating = st.selectbox("Would you like to rate our service?", options=["1", "2", "3", "4", "5"])
                st.write(f"Amazon Chatbot: Thank you for your rating of {rating} stars!")

    elif intent == "farewell":
        st.write("Amazon Chatbot: Thank you for visiting Amazon! Have a great day!")

    else:
        st.write("Amazon Chatbot: I'm sorry, I didn't understand that. Can you please rephrase?")

    # Simulate delay to make it more realistic
    time.sleep(1)

    # Example to show multiple random responses
    if intent == "order_status":
        st.write(f"Amazon Chatbot: Also, your order is now in 'Dispatched' status.")
    elif intent == "complaint":
        st.write("Amazon Chatbot: We are sorry for the inconvenience. A support representative will reach out to you soon.")
    elif intent == "return":
        st.write("Amazon Chatbot: Please ensure the item is in its original condition before returning.")

# Expose the app via localtunnel (for remote access)
!wget -q -O - ipv4.icanhazip.com
!streamlit run app.py & npx localtunnel --port 8501

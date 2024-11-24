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
    

from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai
import googlemaps
from geopy.exc import GeocoderTimedOut

# Load environment variables
load_dotenv()

# Configure Google Generative AI
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat(history=[])

# Initialize Google Maps client with your API key
gmaps = googlemaps.Client(key=os.getenv("GOOGLE_MAPS_API_KEY"))

# Function to get responses from the Gemini model
def get_gemini_response(question):
    response = chat.send_message(question, stream=True)
    return response

# Function to generate Google Meet link
def generate_meet_link():
    # Generate a unique Google Meet link
    meet_link = "https://meet.google.com/new"
    return meet_link

# Function to display a map for order tracking
def display_map(order_id):
    try:
        # Here, you would get the actual address or coordinates based on the order ID
        # For demo purposes, let's use a fixed address
        address = "1600 Amphitheatre Parkway, Mountain View, CA"  # Replace with actual order data
        
        # Geocode the address to get latitude and longitude
        geocode_result = gmaps.geocode(address)
        
        if geocode_result:
            location = geocode_result[0]['geometry']['location']
            lat, lng = location['lat'], location['lng']
            st.map([{'lat': lat, 'lon': lng}])  # Display the map with the order location
        else:
            st.write("Could not find location for this order ID.")
    except GeocoderTimedOut:
        st.write("Error: Geocoding request timed out. Please try again.")
    except Exception as e:
        st.write(f"An error occurred: {e}")

# Initialize Streamlit app
st.set_page_config(page_title="Q&A Demo")

st.header("Amazon Chatbot")

# Initialize session state for chat history if it doesn't exist
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

# Input box for user queries
input = st.text_input("Ask your question:", key="input")
submit = st.button("Submit")

if submit and input:
    # Handle specific queries
    if "hi" in input.lower():
        response_text = "Hi! How can I help you?"
    elif "track my product" in input.lower():
        order_id = st.text_input("Please enter your order ID:")
        if order_id:
            display_map(order_id)
            response_text = "Tracking your order... You can see the location on the map above."
        else:
            response_text = "Please provide your order ID to track the product."
    elif "issue with the product" in input.lower():
        order_id = st.text_input("Please enter your order ID for the product issue:")
        if order_id:
            meet_link = generate_meet_link()
            response_text = f"We've generated a Google Meet link for your video call: {meet_link}"
        else:
            response_text = "Please provide your order ID to address the product issue."
    else:
        # Get response from Gemini model
        response = get_gemini_response(input)
        response_text = ""
        for chunk in response:
            response_text += chunk.text
    
    # Add user query and response to session state chat history
    st.session_state['chat_history'].append(("You", input))
    st.subheader("The Response is")
    st.write(response_text)
    st.session_state['chat_history'].append(("Amazon", response_text))

# Display the chat history in a sidebar
with st.sidebar:
    st.subheader("Chat History")
    for role, text in st.session_state['chat_history']:
        st.write(f"{role}: {text}")

# Styling for a better chatbox experience
st.markdown("""
<style>
    .chat-container {
        max-height: 400px;
        overflow-y: auto;
        border: 1px solid #ccc;
        padding: 10px;
        margin-bottom: 10px;
    }
    .chat-message {
        margin-bottom: 5px;
        padding: 10px;
        border-radius: 5px;
    }
    .chat-message.user {
        background-color: #e0f7fa;
        text-align: left;
    }
    .chat-message.bot {
        background-color: #fff9c4;
        text-align: left;
    }
</style>
""", unsafe_allow_html=True)

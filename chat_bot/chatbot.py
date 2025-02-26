import os
import google.generativeai as genai  # type: ignore
import pytesseract
from PIL import Image

# Configure API key
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Text generation settings
generation_config = {
    "temperature": 0,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

# Initialize the model
model = genai.GenerativeModel(
    model_name="gemini-2.0-flash",
    generation_config=generation_config
)

# Conversation history
history = []

# Function to extract text from images
def extract_text_from_image(image_path):
    try:
        image = Image.open(image_path)
        text = pytesseract.image_to_string(image)
        return text.strip() if text.strip() else "I couldn't extract text from the image."
    except Exception as e:
        return f"Error processing the image: {str(e)}"

print("Bot: Hi! I'm BlingBot, the AI assistant for the Bling app. How can I help you today?\n")
print("Guidelines: You can type your message or provide an image path. If you want to extract text from an image, make sure the image file is accessible and provide its full path. Supported formats: .png, .jpg, .jpeg\n")

while True:
    user_input = input("You: ")

    if user_input.lower() in ["exit", "quit", "bye"]:  
        print("Bot: Goodbye!")
        break

    # Check if the input is an image path
    if os.path.exists(user_input) and user_input.lower().endswith((".png", ".jpg", ".jpeg")):
        extracted_text = extract_text_from_image(user_input)
        print(f"Extracted Text: {extracted_text}\n")
        user_input = extracted_text  # Send extracted text to the bot instead of the image

    # Start chat session
    chat_session = model.start_chat(history=history)
    response = chat_session.send_message(user_input)
    model_response = response.text

    print(f'Bot: {model_response}\n')

    # Save conversation history
    history.append({"role": "user", "parts": [user_input]})
    history.append({"role": "model", "parts": [model_response]})

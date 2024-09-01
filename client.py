import base64
import requests
import os 

# OpenAI API Key
api_key = "api-key"

# Path to your image
image_path = "CNote.jpg"  # No leading slash

# Function to encode the image
def encode_image(image_path):
  with open(image_path, 'rb') as image_file:
      return base64.b64encode(image_file.read()).decode('utf-8')
    
def create_output(api_key, image_path):

  # If you want to make sure the path is relative to the current script directory
  current_dir = os.path.dirname(__file__)
  image_path = os.path.join(current_dir, "CNote.jpg")

  # Getting the base64 string
  base64_image = encode_image(image_path)

  headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
  }

  payload = {
    "model": "gpt-4o",
    "messages": [
      {
        "role": "user",
        "content": [
          {
            "type": "text",
            "text": "What is the note name in this image? This note is specificially for a b-flat instrument."
          },
          {
            "type": "image_url",
            "image_url": {
              "url": f"data:image/jpeg;base64,{base64_image}"
            }
          }
        ]
      }
    ],
    "max_tokens": 300
  }

  response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
  
  # Check if the response is successful
  if response.status_code == 200:
      response_data = response.json()
      # print(response_data)  # Print the entire response JSON for debugging
      print(response_data["choices"][0]["message"]["content"])  # Print only the generated output
      return response_data["choices"][0]["message"]["content"]
  else:
      print(f"Request failed with status code {response.status_code}")
      print(response.text)
  

# Corrected entry point check
if __name__ == '__main__':
    create_output(api_key, image_path)

Here's an updated `README.md` file with Docker integration instructions:

```markdown
# AI-Powered English Conversation Learning Web Application

This project is an AI-powered web application designed to help users improve their English speaking skills through real-time, interactive voice conversations. The application leverages the **Gemma 2:2b** AI model and is built with Django, offering dynamic progress tracking, lessons, weekly tasks, and more.

## Features

- **Real-time Conversational AI**: Engage in natural English conversations powered by the Gemma 2:2b model.
- **Progress Tracking**: Monitor your progress across various language skills.
- **Weekly Tasks**: Complete weekly challenges to improve your conversational abilities.
- **Supplementary Resources**: Access videos and other resources to enhance learning.
- **Responsive Design**: Learn anytime, anywhere with a fully responsive interface.

## Requirements

### Software
- Python 3.x
- Django
- Docker (for AI model)
- JavaScript, HTML, CSS
- TensorFlow/PyTorch (for AI model)
- SpeechRecognition and PyAudio

### Hardware
- Quad-core processor (Intel i5 or equivalent)
- 8GB RAM (16GB recommended)
- 500GB SSD
- High-quality microphone
- (Optional) NVIDIA GPU with CUDA support

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/RO45Y/AI-Powered-English-Conversation-Learning-Web-Application.git
   cd AI-Powered-English-Conversation-Learning-Web-Application
   ```

2. **Create a Virtual Environment and Install Dependencies**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   pip install -r requirements.txt
   ```

3. **Apply Migrations**

   ```bash
   python manage.py migrate
   ```

4. **Run the Development Server**

   ```bash
   python manage.py runserver
   ```

5. **Start the Docker Container for the AI Model**

   To run the AI model, ensure Docker is installed. Use the following commands to pull and run the Docker image.

   ```bash
   docker pull sha256:98eb9f76550d603d005a70d408ac3137a0b288c24e1ed9e2261bd8c4675f867c
   docker run -d -p 8000:8000 sha256:98eb9f76550d603d005a70d408ac3137a0b288c24e1ed9e2261bd8c4675f867c
   ```

6. **Access the AI Model**

   - The AI model is hosted in a Docker container.
   - A **Link** button is available on the dashboard of the web application. 
   - **Before** clicking the link, make sure the Docker container is running.

## Usage

- **Create an Account**: Sign up and log in to start your language learning journey.
- **Practice Conversations**: Engage with the AI model for real-time speaking practice.
- **Track Your Progress**: Use the dashboard to monitor lesson completion, points earned, and weekly task status.
- **Complete Weekly Challenges**: Test your skills with new challenges every week.
  
## Docker and AI Model Integration

- The AI model for real-time conversations is hosted inside a Docker container.
- Before accessing the AI-powered conversation, make sure to **run the Docker container** using the commands mentioned above.
- After running the container, click the link button on the web application dashboard to connect with the AI model.

## Contribution

If you wish to contribute, feel free to submit pull requests or open issues on GitHub.

## License

This project is licensed under the MIT License.
```
https://youtu.be/kze_xJpBvqA?si=53pzYigkWw5rwBT4


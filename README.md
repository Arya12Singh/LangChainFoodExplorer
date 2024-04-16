# # World Foods Explorer

Welcome to "World Foods Explorer," an innovative web application that serves as your culinary guide to the world's diverse gastronomy. Crafted with care, this platform combines the sophisticated artificial intelligence of OpenAI with the seamless user experience provided by Streamlit, all orchestrated through the intelligent workflows of LangChain.

Embark on a journey of taste and knowledge as you discover the origins, nutritional facts, and recipes of international dishes right from your browser.

For a deeper dive into the inspirations and technology behind "World Foods Explorer," read the accompanying blog post:
[World Food Wisdom: A LangChain and OpenAI-Powered Culinary Odyssey] (https://aryasingh.hashnode.dev/world-food-wisdom-a-langchain-and-openai-powered-culinary-odyssey)

## Features

- **Cultural Insights**: Explore the rich history and cultural background of your favorite dishes from around the globe.
- **Health Conscious**: Access detailed nutritional information to make informed dietary choices.
- **Cooking Companion**: Find comprehensive recipes to recreate authentic flavors in your kitchen.

## Getting Started

Before enjoying the features of "World Foods Explorer," ensure you meet the following prerequisites:

- Python 3.9
- An active OpenAI API key

### Installation

Clone the repository and navigate to the project directory:

```bash
git clone https://github.com/Arya12Singh/world-foods-explorer.git
cd world-foods-explorer
Install the required dependencies with pip:

bash
Copy code
pip install -r requirements.txt
Configuration
Configure your OpenAI API key in constants.py. Remember to replace the placeholder with your actual key and to keep this information secure:

python
Copy code
# constants.py
openai_key = "INSERT-YOUR-OPENAI-API-KEY-HERE"
Running the Application
Start the application using Streamlit:

bash
Copy code
streamlit run main.py
Navigate to http://localhost:8501 in your web browser to interact with "World Foods Explorer."


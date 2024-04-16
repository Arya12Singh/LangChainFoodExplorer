# # World Foods Explorer

# LangChain Food Explorer

## Overview
The LangChain Food Explorer is a web application designed to leverage natural language processing to provide insights into various food-related queries. This tool uses the LangChain library to enable conversational AI capabilities, making it easier to navigate and extract culinary data, dietary trends, and nutrition information interactively.

## Features
- **Interactive Food Queries**: Utilize natural language processing to answer questions about food.
- **Data Visualization**: Graphical representations of food data analysis.
- **Trend Analysis**: Insights into current food trends and preferences.

## Technologies Used
- **LangChain**: For integrating conversational AI.
- **Streamlit**: For creating the web application.
- **OpenAI**: For advanced AI models and capabilities.

## Setting Up the OpenAI API Key
To use the OpenAI functionalities within the LangChain Food Explorer, you need to set up your OpenAI API key:

1. **Get an API Key**:
   - If you do not already have an API key, you can obtain one by signing up at [OpenAI](https://openai.com/).

2. **Configure the API Key**:
   - Once you have your API key, configure it in your environment variables:
     ```bash
     export OPENAI_API_KEY='your_api_key_here'
     ```
   - Alternatively, you can directly insert your key into the script where the API is initialized, but using environment variables is recommended for security reasons.

Adding this key enables the application to interact with OpenAI's models, enhancing its natural language processing capabilities.

## Installation
To set up the project locally, follow these steps:
1. **Clone the Repository**:
   git clone https://github.com/Arya12Singh/LangChainFoodExplorer.git
2. Navigate to the Project Directory:
   cd LangChainFoodExplorer
3. Install Required Libraries:
   pip install -r requirements.txt
4. Running the Application
  Execute the following command to start the application:
  streamlit run main.py
Navigate to http://localhost:8501 in your web browser to interact with "World Foods Explorer."

##Contributing
Contributions are welcome! Feel free to fork the repository and submit pull requests with your enhancements.

##License
This project is released under the MIT License.

## Contact
For any queries or feedback, please open an issue in the GitHub repository.


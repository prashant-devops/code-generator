# Automated Code Generator

Automated Code Generator is a web application powered by Streamlit and OpenAI's GPT-3 API. It effortlessly translates natural language descriptions into Python code.

## Features

- **Natural Language Input**: Users can describe the code they want in plain English.
- **Instant Code Generation**: Leverages the power of GPT-3 API to generate relevant Python code.
- **Clean Display**: The generated code is displayed in a well-formatted manner within the app.

## Usage

### Prerequisites

Ensure you have an OpenAI API key to use the GPT-3 service.

### Steps

1. Enter your OpenAI API key in the designated section of the code.
2. Execute the command `streamlit run app.py`.
3. On the app interface, provide a description of the code you wish to generate in natural language.
4. The app will communicate with the GPT-3 API and promptly display the generated Python code.

## Implementation

The heart of the application lies in the `openai.Completion.create()` function. This function, utilizing the Text Davinci 003 engine, crafts Python code based on the user's prompt.

The user interface is elegantly designed using Streamlit, ensuring a seamless experience for the end-user.

## Credits

- **OpenAI's GPT-3 API**: The app uses the GPT-3 API for text completion capabilities.

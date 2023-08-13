# Automated Code Generator

This is a simple web app built with Streamlit and OpenAI's GPT-3 API that generates Python code from a natural language description.

## Features

- User can enter a description of what they want the code to do
- App uses GPT-3 API to generate relevant Python code
- Generated code is displayed nicely formatted in the app

 

## Usage

To use the app:

1. Enter an OpenAI API key in the code
1. Run `streamlit run app.py`
1. Enter a description of the code you want generated in natural language
1. App will call GPT-3 API and display generated Python code

 

## Implementation

The core logic is in the `openai.Completion.create()` call. This uses the Text Davinci 003 engine to generate Python code based on the prompt.

The app is built with Streamlit for the UI.

## Credits

Uses OpenAI's GPT-3 API for text completion

from transformers import pipeline 
import gradio as gr 

# Load a pretrained Hugging Face Summarization model
model = pipeline("summarization")

# Define the prediction function 
def predict(prompt):
    """
    Summarize the input text using the pretrained 
    Hugging Face summarization model 

    Args: 
        prompt (str) Text provided by the user

    Return: 
        str: Generated summary 
    """
    summary = model(prompt)[0]["summary_text"]
    return summary

# Build the Gradio user interface
with gr.Blocks as demo:
    # Input component: accepts text from user 
    textbox = gr.Textbox(placeholder="Enter text block to summarize", lines=4)
    
    # Output component: displays the generated summary 
    output = gr.Textbox(label="Summary")
    # Button triggers the prediction function 
    button = gr.Button("Summarization")

    # Connect inputs, function and outputs 
    button.click(fn=predict, inputs=textbox, outputs=output)

demo.launch()

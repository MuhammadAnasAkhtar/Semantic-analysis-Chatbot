import torch
import gradio as gr
from transformers import pipeline

# Initialize the sentiment-analysis pipeline
semantic_analysis = pipeline("sentiment-analysis", model="BAAI/bge-reranker-v2-m3")

# Define a function to analyze text semantics
def analyze_semantics(input_text):
    # Get the result from the pipeline
    result = semantic_analysis(input_text)
    # Extract label (e.g., Positive/Negative) and confidence score
    label = result[0]['label']
    confidence = round(result[0]['score'] * 100, 2)
    return f"Sentiment: {label} (Confidence: {confidence}%)"

# Set up the Gradio interface
gr.close_all()

Demo = gr.Interface(
    fn=analyze_semantics,
    inputs=[gr.Textbox(label="Enter Text for Semantic Analysis", lines=5)],
    outputs=[gr.Textbox(label="Semantic Analysis Result", lines=2)],
    title="Semantic Analysis App",
    description="This application performs semantic analysis to determine the sentiment of the given text."
)

# Launch the app with a public link
Demo.launch(share=True)

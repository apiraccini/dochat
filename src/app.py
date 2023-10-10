import gradio as gr
from utils.app_utils import ask


with gr.Blocks() as demo:

    with gr.Tab(label='Ask me anything'):

        question = gr.Textbox(label='Question', placeholder="Insert your question here.")
        submit_btn = gr.Button(value = 'Ask', size='sm')
        answer = gr.Markdown(label="Answer")
    
    submit_btn.click(fn=ask, inputs=question, outputs=answer, api_name="datachat_answer")

if __name__ == '__main__':
    demo.launch(server_name="0.0.0.0", server_port=7860)
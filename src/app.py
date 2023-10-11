import gradio as gr
from utils.app_utils import ask


with gr.Blocks(theme=gr.themes.Monochrome()) as demo:

    gr.Markdown('# DOChat')

    with gr.Tab(label='Ask me anything'):

        question = gr.Textbox(label='Question', placeholder="Insert your question here.")
        submit_btn = gr.Button(value = 'Ask', size='sm')
        response = gr.Markdown()

    with gr.Accordion(label='Details', open=False):
        
        log = gr.Markdown()
        prompt = gr.Markdown()

    submit_btn.click(fn=ask, inputs=question, outputs=[response, prompt, log], api_name="datachat_answer")


if __name__ == '__main__':
    demo.launch(server_name="0.0.0.0", server_port=7860)
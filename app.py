import gradio as gr

def nascet (X,Y):
    result = ((Y-X)/Y)*100
    return round (result,2)



with gr.Blocks() as demo:
    X = gr.Number(label="Stenosis")
    Y = gr.Number(label="Normal Diameter")
    output = gr.Number(label="Stenosis per NASCET criteria is __ percent")
    greet_btn = gr.Button("calculate")
    greet_btn.click(fn=nascet, inputs=[X,Y], outputs=output, api_name="nascet")
    

demo.launch()

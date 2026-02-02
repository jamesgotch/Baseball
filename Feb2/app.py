import gradio as gr
import numpy as np
import pandas as pd
import sqlite3

def f(x,y):
    return x+y

with gr.Blocks() as iface:
    with gr.Row():
        with gr.Column():
            x = gr.Number(label = "Type in a Number")
            y = gr.Number(label = "Type in another Number")
        with gr.Column():
            sum = gr.Number(label = "Sum")
x.change(fn = f, inputs = [x,y], outputs = [sum])
y.change(fn = f, inputs = [x,y], outputs = [sum])

iface.launch()
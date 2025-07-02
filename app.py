from flask import Flask, render_template, request
import plotly.graph_objs as go
import plotly
import json

app = Flask(__name__)

@app.route('/plotly', methods=['GET'])
def plotly_graph():
    graph_type = request.args.get("type", "scatter")

    traces_list = []
    if graph_type == "scatter":
        traces_list = [
            go.Scatter(x=[1, 2, 3], y=[10, 15, 13], mode='markers', name="Scatter 1"),
            go.Scatter(x=[1, 2, 3], y=[16, 5, 11], mode='markers', name="Scatter 2"),
            go.Scatter(x=[1, 2, 3], y=[12, 9, 15], mode='markers', name="Scatter 3")
        ]
    elif graph_type == "box":
        traces_list = [
            go.Box(y=[10, 15, 13, 17, 20, 22], name="Box 1"),
            go.Box(y=[7, 9, 5, 12, 14, 18], name="Box 2"),
            go.Box(y=[20, 22, 19, 24, 25, 23], name="Box 3")
        ]

    # 각각 fig 생성
    figures = []
    for i, trace in enumerate(traces_list, 1):
        layout = go.Layout(title=f"{graph_type.title()} Graph {i}")
        fig = go.Figure(data=[trace], layout=layout)
        figures.append(json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder))

    return render_template("plotly_3graphs.html",
                           figures=figures,
                           graph_type=graph_type)

@app.route('/')
def home():
    return '<a href="/plotly">Go to Dynamic Plotly Page</a>'

if __name__ == '__main__':
    app.run(debug=True)
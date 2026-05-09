from dash import Dash, html
app = Dash(__name__)

app.layout = html.Div([ 
                       html.H1("Quantium Dashboard Test") ,
                       html.P("If you can see this your environment is working!!")
                       ])

if __name__ == '__main__':
    app.run(debug=True)
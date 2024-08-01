
import dash                                     # pip install dash
from dash import dcc, html, Input, Output 
import pandas as pd
import plotly.express as px     # (version 4.6.0)
from prepare import PrepareData



app = dash.Dash(__name__)

# ------------------------------------------------------------------------
# Import and filter data into pandas data frame
#read raw data
prepare_data = PrepareData(download_new=True)
#will return these dataframe already cleaned and transformed
data = prepare_data.run()


df = data['all']

names = df.columns

df = df.groupby(['Type','Sex', 'Gender',  'GeneralHealth', 'income', 'education'])[['Diabetes_binary']].count()
df.reset_index(inplace=True)
# ------------------------------------------------------------------------
#'Income', 'GenHlth', 'MentHlth', 'PhysHlth', 'DiffWalk'
input_types = ['number', 'number', 'number', 'number', 'number']

app.layout = html.Div([
    html.Div([
        dcc.Input(
            id='my_{}'.format(x),
            type=x,
            placeholder="insert {}".format(x),  # A hint to the user of what can be entered in the control
            debounce=True,                      # Changes to input are sent to Dash server only on enter or losing focus
            min=0, max=8, step=1,         # Ranges of numeric value. Step refers to increments
            minLength=1, maxLength=1,          # Ranges for character length inside input box
            autoComplete='on',
            disabled=False,                     # Disable input box
            readOnly=False,                     # Make input box read only
            required=False,                     # Require user to insert something into input box
            size="20",                          # Number of characters that will be visible inside box
            # style={'':''}                     # Define styles for dropdown (Dropdown video: 13:05)
            # className='',                     # Define style from separate CSS document (Dropdown video: 13:05)
            # persistence='',                   # Stores user's dropdown changes in memory (Dropdown video: 16:20)
            # persistence_type='',              # Stores user's dropdown changes in memory (Dropdown video: 16:20)
        ) for x in input_types
    ]),

    html.Br(),

    dcc.Graph(id="mymap"),

])


# ------------------------------------------------------------------------
@app.callback(
    Output(component_id='mymap', component_property='figure'),
    [Input(component_id='my_{}'.format(x), component_property='value')
     for x in input_types
     ],
)
def update_graph(num_year, pwd_state, txt_state, tel_state, email_, url_, search_disease, hidden_input):
    if tel_state:
        tel_state = tel_state
    elif tel_state is None or len(tel_state) == 0:
        tel_state = 10

    if search_disease:
        search_disease = search_disease
    elif search_disease is None or len(search_disease) == 0:
        search_disease = "Disease"

    dff = df.copy()

    dff = dff[dff['Year'] == num_year]
    dff = dff[dff['State'] != pwd_state]
    dff = dff[dff['State'] != txt_state]
    dff = dff[dff['State ANSI'] != int(tel_state)]
    dff = dff[dff['Affected by'] == search_disease]

    print("number: " + str(num_year))
    print("password: " + str(pwd_state))
    print("text: " + str(txt_state))
    print("telephone: " + str(tel_state))
    print("hidden: " + str(hidden_input))
    print("email: " + str(email_))
    print("url: " + str(url_))
    print("search: " + str(search_disease))
    print("---------------")

    beemap = px.choropleth(
        data_frame=dff,
        locationmode='USA-states',
        locations='state_code',
        scope="usa",
        color='Percent of Colonies Impacted',
        hover_data=['State', 'Percent of Colonies Impacted'],
        color_continuous_scale=px.colors.sequential.YlOrRd,
        title='Bees affected by {}'.format(search_disease),
        template='plotly_dark',
        labels={'Percent of Colonies Impacted': '% of Bee Colonies'}
    )

    beemap.update_layout(title={'x': 0.5, 'xanchor': 'center', 'font': {'size': 20}})

    beemap.update_traces(hovertemplate=
                         "<b>%{customdata[0]}</b><br><br>" +
                         "Percent of Colonies Impacted: %{customdata[1]:.3s}" +
                         "<extra></extra>",
                         )
    return (beemap)

# ------------------------------------------------------------------------
if __name__ == '__main__':
    app.run_server(debug=True)

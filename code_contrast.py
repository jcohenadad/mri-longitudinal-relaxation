%use sos
%get params --from Octave
%get TR_range --from Octave
%get signal_WM --from Octave
%get signal_GM --from Octave
%get signal_CSF --from Octave

import matplotlib.pyplot as plt
import plotly.plotly as py
import plotly.graph_objs as go
import numpy as np
from plotly import __version__
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
config={'showLink': False, 'displayModeBar': False}

init_notebook_mode(connected=True)

from IPython.core.display import display, HTML

data1 = [dict(
        visible = False,
        mode = 'lines',
        x = params["EXC_FA"],
        y = abs(np.squeeze(np.asarray((signal_WM[ii] - signal_GM[ii]) / signal_WM[ii]))),
        name = 'Contrast WM/GM',
        text = 'Contrast WM/GM',
        hoverinfo = 'x+y+text') for ii in range(len(TR_range))]

data1[4]['visible'] = True

data = data1

steps = []
for i in range(len(TR_range)):
    step = dict(
        method = 'restyle',  
        args = ['visible', [False] * len(data1)],
        label = str(TR_range[i])
        )
    step['args'][1][i] = True # Toggle i'th trace to "visible"
    steps.append(step)

sliders = [dict(
    x = 0,
    y = -0.02,
    active = 2,
    currentvalue = {"prefix": "TR value (ms): <b>"},
    pad = {"t": 50, "b": 10},
    steps = steps
)]

layout = go.Layout(
    width=580,
    height=450,
    margin=go.layout.Margin(
        l=80,
        r=40,
        b=60,
        t=10,
    ),
    annotations=[
        dict(
            x=0.5004254919715793,
            y=-0.18,
            showarrow=False,
            text='Excitation Flip Angle (Â°)',
            font=dict(
                family='Times New Roman',
                size=22
            ),
            xref='paper',
            yref='paper'
        ),
        dict(
            x=-0.15,
            y=0.5,
            showarrow=False,
            text='Contrast WM/GM',
            font=dict(
                family='Times New Roman',
                size=22
            ),
            textangle=-90,
            xref='paper',
            yref='paper'
        ),
    ],
    xaxis=dict(
        autorange=False,
        range=[0, params['EXC_FA'][-1]],
        showgrid=False,
        linecolor='black',
        linewidth=2
    ),
    yaxis=dict(
        autorange=True,
        showgrid=False,
        linecolor='black',
        linewidth=2
    ),
    legend=dict(
        x=0.5,
        y=0.9,
        traceorder='normal',
        font=dict(
            family='Times New Roman',
            size=12,
            color='#000'
        ),
        bordercolor='#000000',
        borderwidth=2
    ), 
    sliders=sliders
)

fig = dict(data=data, layout=layout)

plot(fig, filename = 'vfa_fig_2.html', config = config)
display(HTML('vfa_fig_2.html'))


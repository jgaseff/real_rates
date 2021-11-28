import numpy as np
import pandas as pd
import plotly.express as px

x0 = np.random.randn(250)
# Add 1 to shift the mean of the Gaussian distribution
x1 = np.random.randn(500) + 1

df =pd.DataFrame(dict(
    series=np.concatenate((["a"]*len(x0), ["b"]*len(x1))), 
    data  =np.concatenate((x0,x1))
))

px.histogram(df, x="data", color="series", barmode="overlay")

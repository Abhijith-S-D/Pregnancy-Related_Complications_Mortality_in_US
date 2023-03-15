# use plotly's historgram function
# first argument is the datafram, then put your x and y axis
# colors the column name referencing the different bars in each group, if you want to group the bars by the x-axis, use group bar mode
# category_orders helps order the bars, I wanted ascending order

import pandas as pd
import plotly.express as px
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

gestationalDiabetes_vs_BMI =  {
"<18.5" : 3.247,
"18.5-24.9" : 4.147,
"25.0-29.9" : 6.904,
"30.0-34.9" : 9.941,
"35.0-39.9" : 12.53,
">39.9" : 5.248,
}

cSection_vs_BMI =  {
 "<18.5" : 21.262,
 "18.5-24.9" : 25.606,
 "25.0-29.9" : 32.080,
 "30.0-34.9" : 37.693,
 "35.0-39.9" : 43.392,
 ">39.9" : 52.289,
}

preTermBirth_vs_BMI =  {
"<18.5" : 11.875,
"18.5-24.9" : 8.9903,
"25.0-29.9" : 9.8061,
"30.0-34.9" : 11.386,
"35.0-39.9" : 12.845,
">39.9" : 15.095,
}

inductionOfLabor_vs_BMI =  {
"<18.5" : 12.176,
"18.5-24.9" : 12.912,
"25.0-29.9" : 15.594,
"30.0-34.9" : 17.499,
"35.0-39.9" : 18.739,
">39.9" : 19.045,
}

anesthesia_vs_BMI =  {
"<18.5" : 61.770,
"18.5-24.9" : 61.842,
"25.0-29.9" : 63.731,
"30.0-34.9" : 65.133,
"35.0-39.9" : 66.407,
">39.9" : 67.853,
}

chotio_vs_BMI =  {
"<18.5" : 0.140,
"18.5-24.9" : 0.145,
"25.0-29.9" : 0.165,
"30.0-34.9" : 0.179,
"35.0-39.9" : 0.168,
">39.9" : 0.157,
}

anti_vs_BMI =  {
"<18.5" : 11.630,
"18.5-24.9" : 11.241,
"25.0-29.9" : 11.684,
"30.0-34.9" : 12.090,
"35.0-39.9" : 12.393,
">39.9" : 12.543,
}

combined_dict = {
                #  'bmi' : list(gestationalDiabetes_vs_BMI.keys()),
                 'Gest' : gestationalDiabetes_vs_BMI,
                 'csec' : cSection_vs_BMI,
                 'preterm' : preTermBirth_vs_BMI,
                 'induction' : inductionOfLabor_vs_BMI,
                 'anes' : anesthesia_vs_BMI,
                 'cho' : chotio_vs_BMI,
                 'anti' : anti_vs_BMI,
                 }

# print(combined_dict)

# issue
# bmi
# value

new_dict = {'issue': [], 'bmi': [], 'value': []}
for key, value in combined_dict.items():
    for key_d, value_d in gestationalDiabetes_vs_BMI.items():
        new_dict['issue'].append(key)
        new_dict['bmi'].append(key_d)
        new_dict['value'].append(value[key_d])

# print(new_dict)

# Convert dictionary to Pandas DataFrame
df = pd.DataFrame(new_dict)

print(df)

fig = px.histogram(df, 
                   x='bmi', 
                   y='value',
                   color='issue', 
                   barmode='group',
                   category_orders={'bmi':list(gestationalDiabetes_vs_BMI.keys())},
                   color_discrete_sequence=["rgb(255, 152, 90)", "rgb(119, 158, 204)", "rgb(255, 179, 71)", "rgb(255, 152, 90)", "rgb(119, 158, 204)", "rgb(255, 179, 71)", "rgb(48, 153, 217)"],
                   labels={"Single Race 6": "Single Race"})

# fig.update_layout(title={
#                   'text':'Maternal Mortality Ratio per 100,000 Live Births by Year and Race',
#                   'xanchor': 'center',
#                   'yanchor': 'top',
#                   'x': 0.5},
#                   yaxis_title={'text': 'MMR per 100,000 Live Births'},
#                   xaxis_title={'text': 'Years'})
# fig.update_layout(
#     font_family="Verdana",
#     font_color="black",
#     font_size = 24,
#     title_font_family="Verdana",
#     title_font_color="black",
#     title_font_size=28,
#     legend_title_font_color="black"
# )
# fig.show(renderer='png', height=900, width=1800)
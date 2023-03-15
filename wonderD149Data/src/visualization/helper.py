# use plotly's historgram function
# first argument is the datafram, then put your x and y axis
# colors the column name referencing the different bars in each group, if you want to group the bars by the x-axis, use group bar mode
# category_orders helps order the bars, I wanted ascending order

import pandas as pd
import plotly.express as px
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

def create_panda_and_plot_4_combined (input_dict, bmi_keys):
# Convert dictionary to Pandas DataFrame
    df = pd.DataFrame(input_dict)

    print(df)

    fig = px.histogram(df, 
                    x='bmi', 
                    y='value',
                    color='issue', 
                    barmode='group',
                    category_orders={'bmi':bmi_keys},
                    color_discrete_sequence=["rgb(255, 152, 90)", "rgb(119, 158, 204)", "rgb(255, 179, 71)", "rgb(48, 153, 217)"],
                    labels={"Single Race 6": "Single Race"})

    # fig.update_layout(title={
    #                 'text':'Percentage of Patiants experiencing complications during Pregnency v/a their BMI',
    #                 'xanchor': 'center',
    #                 'yanchor': 'top',
    #                 'x': 0.5},
    #                 yaxis_title={'text': 'Percentage of Patiants experienced issues'},
    #                 xaxis_title={'text': 'BMI'})
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

def create_panda_and_plot_3_combined (input_dict, bmi_keys):
# Convert dictionary to Pandas DataFrame
    df = pd.DataFrame(input_dict)

    print(df)

    fig = px.histogram(df, 
                    x='bmi', 
                    y='value',
                    color='issue', 
                    barmode='group',
                    category_orders={'bmi':bmi_keys},
                    color_discrete_sequence=["rgb(255, 152, 90)", "rgb(119, 158, 204)", "rgb(255, 179, 71)"],
                    labels={"Single Race 6": "Single Race"})

    # fig.update_layout(title={
    #                 'text':'Percentage of Patiants experiencing complications during Pregnency v/a their BMI',
    #                 'xanchor': 'center',
    #                 'yanchor': 'top',
    #                 'x': 0.5},
    #                 yaxis_title={'text': 'Percentage of Patiants experienced issues'},
    #                 xaxis_title={'text': 'BMI'})
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

def main():

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
    "<18.5" : 14.0,
    "18.5-24.9" : 14.5,
    "25.0-29.9" : 16.5,
    "30.0-34.9" : 17.9,
    "35.0-39.9" : 16.8,
    ">39.9" : 15.7,
    }

    anti_vs_BMI =  {
    "<18.5" : 11.630,
    "18.5-24.9" : 11.241,
    "25.0-29.9" : 11.684,
    "30.0-34.9" : 12.090,
    "35.0-39.9" : 12.393,
    ">39.9" : 12.543,
    }

    ste_vs_bmi = {
    "<18.5" : 20.58,
    "18.5-24.9" : 17.46,
    "25.0-29.9" : 20.82,
    "30.0-34.9" : 26.19,
    "35.0-39.9" : 31.86,
    ">39.9" : 41.73,
    }

    incresing_combined_dict = {
                    # 'bmi' : list(gestationalDiabetes_vs_BMI.keys()),
                    'Gestational Diabetes' : gestationalDiabetes_vs_BMI,
                    'Cesareans Mode of Delivery' : cSection_vs_BMI,
                    # 'Preterm Birth' : preTermBirth_vs_BMI,
                    'Induction of Labor' : inductionOfLabor_vs_BMI,
                    'Anesthesia' : anesthesia_vs_BMI,
                    # 'Chorioamnionitis (in 10^-2)' : chotio_vs_BMI,
                    # 'Antibiotics for Mother' : anti_vs_BMI,
                    }

    ushaped_combined_dict = {
                    # 'bmi' : list(gestationalDiabetes_vs_BMI.keys()),
                    # 'Gestational Diabetes' : gestationalDiabetes_vs_BMI,
                    # 'Cesareans Mode of Delivery' : cSection_vs_BMI,
                    'Preterm Birth' : preTermBirth_vs_BMI,
                    'Steroids (in 10^-1)' : ste_vs_bmi,
                    # 'Induction of Labor' : inductionOfLabor_vs_BMI,
                    # 'Anesthesia' : anesthesia_vs_BMI,
                    # 'Chorioamnionitis (in 10^-2)' : chotio_vs_BMI,
                    'Antibiotics for Mother' : anti_vs_BMI,
                    }

    # increasing: induction of labor, anesthe, gest, ceas
    # u shaped:  pre term birth, steroids (missing), anti
    # issue:
    # bmi
    # value

    incresing_new_dict = {'issue': [], 'bmi': [], 'value': []}
    for key, value in incresing_combined_dict.items():
        for key_d, value_d in gestationalDiabetes_vs_BMI.items():
            incresing_new_dict['issue'].append(key)
            incresing_new_dict['bmi'].append(key_d)
            incresing_new_dict['value'].append(value[key_d])

    ushaped_new_dict = {'issue': [], 'bmi': [], 'value': []}
    for key, value in ushaped_combined_dict.items():
        for key_d, value_d in gestationalDiabetes_vs_BMI.items():
            ushaped_new_dict['issue'].append(key)
            ushaped_new_dict['bmi'].append(key_d)
            ushaped_new_dict['value'].append(value[key_d])

    bmi_keys = list(gestationalDiabetes_vs_BMI.keys())
    # print(incresing_new_dict)
    create_panda_and_plot_4_combined(incresing_new_dict, bmi_keys)
    create_panda_and_plot_3_combined(ushaped_new_dict, bmi_keys)

main()
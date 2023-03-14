import matplotlib.pyplot as plt
import numpy

# f = open('./file.csv', 'r')

# plot_categories = []
# plot_sub_categories = dict()

# file_content = f.readlines()

# for i in file_content:
#     j = i.split(',')
#     if (j[1] not in plot_sub_categories) and (j[1] != ''):
#         plot_sub_categories[j[1]] = []
#     if (j[0]) not in plot_categories and  (j[0] != ''):
#         plot_categories.append(j[0]) 

# for i in file_content:
#     j = i.split(',')
#     if (j[1] != ''):
#         plot_sub_categories[j[1]].append(j[2])


# print(plot_sub_categories)
# print(plot_categories)

x_axis = []
y_axis = []

fig = plt.rcParams['figure.figsize'] = (8, 5)
fig, ax = plt.subplots()

gest_diab_vs_bmi =  {
"Underweight <18.5          ":      3.247,
"Normal 18.5-24.9           ":      4.147,
"Overweight 25.0-29.9       ":      6.904,
"Obesity I 30.0-34.9        ":      9.941,
"Obesity II 35.0-39.9       ":      12.53,
"Extreme Obesity III > 39.9 ":      5.248,
}


ax.bar(
    x = list[gest_diab_vs_bmi.keys()],
    height = list[gest_diab_vs_bmi.values()],
    tick_label = 'gest_diab_vs_bmi'
)

fig.tight_layout()

# plt.show()

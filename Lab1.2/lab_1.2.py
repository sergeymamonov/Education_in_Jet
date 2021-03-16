from matplotlib import pyplot
from openpyxl import load_workbook

wb = load_workbook('data_analysis_lab.xlsx')
sheet = wb['Data']


def getvalue(x):
    return x.value


years = list(map(getvalue, sheet['A'][1:]))
temperature = list(map(getvalue, sheet['C'][1:]))
activity = list(map(getvalue, sheet['D'][1:]))

pyplot.plot(years, temperature, label="Относительная темперетура")
pyplot.plot(years, activity, label="Активность солнца")
pyplot.show()

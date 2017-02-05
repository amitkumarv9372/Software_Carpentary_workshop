
# coding: utf-8

# In[2]:

from IPython.display import SVG
# to display SVG images


# In[5]:

import pandas as pd


# In[6]:

import pygal


# In[7]:

# reading dataset
health_data = pd.read_csv('Dem_Health_Full.txt', sep = '\t')


# In[10]:

health_data.head(7)
health_data.tail()


# In[12]:

help(health_data)
dir(health_data)


# In[19]:

health_data['State']
health_data[['State','Poverty']]
health_data.loc[0,:]
health_data.loc[0,['Population_Density','Poverty']]
health_data.iloc[0,2:4]
health_data[(health_data['State'] == 'AL') | (health_data['State'] == 'TX')]


# In[20]:

# cleaning data
health_data.iloc[3126] # works with integers


# In[24]:

health_data.fillna(0, inplace=True)
health_data.iloc[3126]


# In[33]:

#cleaning suicide values
health_data.head(6)
health_data['Suicide'].replace(-1111.1,0,inplace=True)
health_data.head(6)


# In[38]:

a_tuple = (1,2)
a_tuple
a_list = [1,2]
type(a_list)
nested_list = [(1,2),(3,4)]
nested_list


# In[39]:

data_for_al = health_data.loc[health_data['State'] == 'AL',                             ['Population_Density','Poverty']]
data_for_al.head()


# In[43]:

lst = [tuple(x) for x in data_for_al.values]
lst


# In[45]:

# creating scatter plot
scatter_plot = pygal.XY(stroke=True)
scatter_plot.add('AL',lst)
SVG(scatter_plot.render())


# In[46]:

# creating scatter plot
# Adding title to the graph
scatter_plot = pygal.XY(stroke=True)
scatter_plot.title = 'Population Density vs Poverty Correlation'
scatter_plot.add('AL',lst)
SVG(scatter_plot.render())


# In[48]:

# Adding label to x-axis and y-axis
scatter_plot = pygal.XY(stroke=True, x_title = 'Population Density', y_title = 'Poverty')
scatter_plot.title = 'Population Density vs Poverty Correlation'
scatter_plot.add('AL',lst)
SVG(scatter_plot.render())


# In[51]:

data_for_TX = health_data.loc[health_data['State'] == 'TX',                             ['Population_Density','Poverty']]
data_for_TX.head()


# In[52]:

lst1 = [tuple(x) for x in data_for_TX.values]
lst1


# In[53]:

scatter_plot1 = pygal.XY(stroke=True, x_title = 'Population Density', y_title = 'Poverty')
scatter_plot1.title = 'Population Density vs Poverty Correlation'
scatter_plot1.add('TX',lst1)
SVG(scatter_plot1.render())


# In[56]:

# adding values of Texas for same graph
scatter_plot = pygal.XY(stroke=False, x_title = 'Population Density', y_title = 'Poverty')
scatter_plot.title = 'Population Density vs Poverty Correlation'
scatter_plot.add('AL',lst)
scatter_plot.add('TX',lst1)
SVG(scatter_plot.render())


# In[58]:

# how for loops work
for i in range(0,6,2): # 0 - inclusive, 6 - exclusive
    print(i)


# In[60]:

# changing the x-axis 
scatter_plot = pygal.XY(stroke=False, x_title = 'Population Density', y_title = 'Poverty')
scatter_plot.title = 'Population Density vs Poverty Correlation'
scatter_plot.x_labels = (i for i in range(0,2000,100))
scatter_plot.add('AL',lst)
scatter_plot.add('TX',lst1)
SVG(scatter_plot.render())


# In[61]:

# adjust the x axis range 
scatter_plot = pygal.XY(stroke=False, x_title = 'Population Density', y_title = 'Poverty', xrange=(0,100))
scatter_plot.title = 'Population Density vs Poverty Correlation'
#scatter_plot.x_labels = (i for i in range(0,2000,100))
scatter_plot.add('AL',lst)
scatter_plot.add('TX',lst1)
SVG(scatter_plot.render())


# In[67]:

# adjust the dot size

scatter_plot = pygal.XY(stroke=False, x_title = 'Population Density', y_title = 'Poverty', xrange=(0,100), dots_size = 2)
scatter_plot.title = 'Population Density vs Poverty Correlation'
#scatter_plot.x_labels = (i for i in range(0,2000,100))
scatter_plot.add('AL',lst)
scatter_plot.add('TX',lst1)
SVG(scatter_plot.render())


# In[66]:

# one last cool stuff
from pygal.style import NeonStyle
scatter_plot = pygal.XY(stroke=False, x_title='Population Density', y_title='Poverty', xrange=(0,10), dots_size=2,                        style=NeonStyle, fill=True)
scatter_plot.title = 'Population Density vs Poverty Corelation'
scatter_plot.add('AL', lst)
scatter_plot.add('TX', lst1)
SVG(scatter_plot.render())


# In[71]:

from pygal.style import LightSolarizedStyle
chart = pygal.StackedLine(fill=True, interpolate='cubic', style=LightSolarizedStyle)
chart.add('A', [1, 3,  5, 16, 13, 3,  7])
chart.add('B', [5, 2,  3,  2,  5, 7, 17])
chart.add('C', [6, 10, 9,  7,  3, 1,  0])
chart.add('D', [2,  3, 5,  9, 12, 9,  5])
chart.add('E', [7,  4, 2,  1,  2, 10, 0])
SVG(chart.render())


# In[72]:

al = health_data.loc[health_data['State'] == 'AL',['Poverty']]
Poverty_mean_al = al['Poverty'].mean()
Poverty_mean_al


# In[74]:

def mean_of_column(state_name, column_name):
    state_df = health_data.loc[health_data['State'] == state_name,[column_name]]
    return state_df[column_name].mean()
mean_of_column('TX','Poverty')


# In[75]:

def mean_of_column(state_name, column_name):
    state_df = health_data.loc[health_data['State'] == state_name,[column_name]]
    return state_df[column_name].mean()
mean_of_column('TX','Suicide')


# In[78]:

health_data['State'].unique()
type(health_data['State'].unique())
list(health_data['State'].unique())


# In[82]:

# vertical bars
bar_chart = pygal.Bar()
bar_chart.title = 'Mean of Poverty across all states'
for state in list(health_data['State'].unique()):
    bar_chart.add(state,mean_of_column(state,'Poverty'))
SVG(bar_chart.render())


# In[83]:

bar_chart = pygal.HorizontalBar()
bar_chart.title = 'Mean of Poverty across all states'
for state in list(health_data['State'].unique()):
    bar_chart.add(state,mean_of_column(state,'Poverty'))
SVG(bar_chart.render())


# In[85]:

bar_chart = pygal.Bar(legend_at_bottom=True, legend_at_bottom_columns=11)
bar_chart.title = 'Mean of Poverty across all states'
for state in list(health_data['State'].unique()):
    bar_chart.add(state,mean_of_column(state,'Poverty'))
SVG(bar_chart.render())


# In[ ]:




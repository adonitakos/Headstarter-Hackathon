!pip install matplotlib

import streamlit as st
import pandas as pd
import numpy as np
from numpy import median
from PIL import Image
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sb
import matplotlib.pyplot as plt2

header = st.container()
dictionary = st.container()
charts = st.container()
charts2 = st.container()
charts3 = st.container()
charts4 = st.container()
barchart = st.container()
customer_raw = st.container()

image = Image.open('logo.jpg')
image2 = Image.open('Image2.jpg')

with header:
  st.image(image)
  st.markdown("<h1 style='text-align: center; color: rgb(61, 86, 240); font-family: 'Poppins',sans-serif; font-weight:bold'>Customer Analysis</h1>", unsafe_allow_html=True)
  st.markdown("<h4 style='text-align: center; color: #404040; font-family: 'Poppins',sans-serif';'>Customer Analysis and Data Visualization Used To Determine Eligibility For Discounts And Merch </h4>", unsafe_allow_html=True)




#load data set
import matplotlib.pyplot as plt
import pandas as pd



# Data Dictionary
with dictionary:
    st.markdown("""<h3 style="color:rgb(61, 86, 240); font-weight:bold";>Data Dictionary</h3><p style=color: #404040; font-family: 'Poppins',sans-serif';'">

Customer_ID : Unique ID assigned to each student

Date_Enrolled: The date of when the student first enrolled in Headstarter 

Days_Since_Last_Cohort: The number of days since the end of the last Headstarter cohort the student participated in 

Amount_Spent_On_Courses: Amount of $ the student spent on courses over the past year

Amount_Spent_on_Books: Amount of $ the student spent on books over the past year

Minutes_Spent_on_Headstarter: Total amount of minutes the student has spent on the Headstarter platform 

Questions_Completed: Total amount of questions the student has completed on the Headstarter platform 

Videos_Watched: Total amount of videos the student has watched on the Headstarter platform 

Minutes_Spent_Coding: Total amount of minutes the student has spent coding on the Headstarter platform 

Email_Opens: Total amount of emails the student has opened from Headstarter 

Num_Courses_Purchased: The number of courses the student has purchased over the past year 

Number_of_Students_Referred: The total number of students the student has referred to a Headstarter program. 

Site_Visits_Per_Month: Average number of times the student visits the Headstarter website a month

Average_Teammate_Rating: The average rating (1-10) the student gets from their teammates, based on their presentation skills and technical projects made during the cohort 

Cohorts_Participated_In: The number of Headstarter cohorts the student has participated in 

Highest_Leaderboard_Rank: The highest the student has ranked on the leaderboard during a Headstarter cohort. The lower the number the better, being ranked 2nd is better than being ranked 20th

Complain: Value of 1 If the student complained about the Headstarter program before, 0 otherwise

Headstarter_Rating: What the student rated Headstarter out of 10


Probability_Of_Getting_Offer: The probability of the student getting a job offer within 6 months of completing the Headstarter program. Expressed out of 100 and should be treated as a percentage
</p>""",  unsafe_allow_html=True)



st.markdown("<h3 style='color:rgb(61, 86, 240); font-weight:bold';>Charts</h3>", unsafe_allow_html=True)

# =========== Dropdown  =========== #
#Education, Major,    #Year Birth, 

xvalue = st.selectbox(
"Please select a x column",
("Education",	"Major","Complain","Cohorts_Participated_In","Headstarter_Rating"))

yvalue = st.selectbox(
"Please select a y column",
("Income","Amount_Spent_On_Courses","Amount_Spent_on_Books", "Minutes_Spent_on_Headstarter", "Questions_Completed",	"Videos_Watched","	Minutes_Spent_Coding", "Email_Opens","	Num_Courses_Purchased",	"Number_of_Students_Referre","Site_Visits_Per_Month",	"Average_Teammate_Rating","Cohorts_Participated_In	Highest_Leaderboard_Rank","Probability_Of_Getting_Offer"))





######################################
        #  BarChart  #
######################################

# =========== Graphs  =========== #
df = pd.read_csv("HackathonDataset.csv")#
df2 = pd.read_csv("HackathonDataset.csv")#
df2 = df2.query("Major == 'Law' " )

#bar chart
plt.title("Bar Chart")
plt.xlabel(xvalue)
plt.ylabel(yvalue)

fig = sb.barplot(x=df[xvalue], y = df[yvalue], estimator = median).figure
st.pyplot(fig, clear_figure=True)

#plt.show()



######################################
        #  BoxPlot  #
######################################



# =========== Graphs  =========== #

#box chart
plt.title("Box Plot")
plt.xlabel(xvalue)

plt.ylabel(yvalue)
fig2 = sb.boxplot(x=df[xvalue], y = df[yvalue],  linewidth = .3).figure
st.pyplot(fig2,clear_figure=True)


st.write("#")
######################################
        #  Scatter  #
######################################
plt2.title("Scatter")




xvalue2 = st.radio(
"Please select a x column",
( "Minutes_Spent_on_Headstarter", "Questions_Completed","	Minutes_Spent_Coding", "Email_Opens",	"Average_Teammate_Rating"))

yvalue2 = st.radio(
"Please select a y column",
("Probability_Of_Getting_Offer","Videos_Watched"	,"Highest_Leaderboard_Rank","Number_of_Students_Referre"))




plt2.xlabel(xvalue2)
plt2.ylabel(yvalue2)
fig3 = sb.scatterplot(data=df, x=xvalue2,y=yvalue2).figure
st.pyplot(fig3, clear_figure=True)

st.write(""" The minutes spent coding correlates to:
    * The probability of getting an offer
    * The number of videos watched
* The number of questions completed, correlates to 
    * The probability of getting an offer
    * The number of videos watched
    * The Higest Leaderboard Rank""")







######################################
        #  RAW DATA CSV  #
######################################
st.markdown("<h3 style='color:rgb(61, 86, 240); font-weight:bold';>Raw Customer Data</h3>", unsafe_allow_html=True)
cust_data = pd.read_csv('HackathonDataset.csv')
st.write(cust_data)

st.markdown("<h3 style='color:rgb(61, 86, 240); font-weight:bold';>How we would distribute merch and discounts</h3>", unsafe_allow_html=True)
st.image(image2)



  
######################################
        # Footer  #
######################################
st.write("Headstarter Hackathon")
st.write("Members")
st.write("")
st.write("Antonios F. Takos")
st.write("Lukasz Paul")
st.write("Aayana Evanson")
st.write("Amritpal Singh")

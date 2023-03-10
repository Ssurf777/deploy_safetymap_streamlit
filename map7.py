import streamlit as st
import pandas as pd
import numpy as np
import folium
from streamlit_folium import folium_static
import pandas as pd
import matplotlib.pyplot as plt
#from bokeh.plotting import figure


sales_office = pd.DataFrame(
    data=[[35.05743382079721, 137.1549853462676],
          [35.22378324365575, 138.89725244402015]],
    index=["_","_"],
    columns=["x","y"]
)
#sales_office
def AreaMarker_home(df,m):
    for index, r in df.iterrows(): 

        folium.Marker(
            location=[r.x, r.y],
            popup=index,
            icon=folium.Icon(icon="home",color="pink")
        ).add_to(m)

def AreaMarker(df,a,b,c,m):
    for index, r in df.iterrows(): 

        folium.Marker(
            location=[r.x, r.y],
            popup=str(a)+str(r.x)+","+str(r.y)+str(b)+str(r.p)+str(c),
            icon=folium.Icon(color="red")
        ).add_to(m)

#m = folium.Map(location=[35.05743382079721, 137.1549853462676], zoom_start=12)
#AreaMarker_home(sales_office,m)
#folium_static(m)



#--------------------------------------------------------------
#datasets
#1:pref
#2:year
#3:month
#4:daynight
#5:weather
#6:cont
#7:weekday
#8:x
#9:y
#10:p for popup
df=pd.read_csv("honhyo_192021_pop.csv",encoding="shift-jis",skiprows=0)
#df
#--------------------------------------------------------------
with st.sidebar:
    st.header("Setting")
#-------------------------------------------------------------
    pref=st.selectbox(
        'select Prefecture',
        ('Aichi','Mie','Gifu','Shizuoka'))
    #st.write(pref)
    if pref=='Aichi': 
       df2=df[df["pref"]==int(54)]
       m = folium.Map(location=[35.05743382079721, 137.1549853462676], zoom_start=12)
       AreaMarker_home(sales_office,m)
    if pref=='Gifu': 
       df2=df[df["pref"]==int(53)]
       m = folium.Map(location=[35.39115917534303, 136.72351981260852], zoom_start=10)
       AreaMarker_home(sales_office,m)
    if pref=='Mie': 
       df2=df[df["pref"]==int(55)]
       m = folium.Map(location=[34.71859388942724, 136.50748850848515], zoom_start=10)
       AreaMarker_home(sales_office,m)
    if pref=='Shizuoka': 
       df2=df[df["pref"]==int(49)]
       m = folium.Map(location=[35.22378324365575, 138.89725244402015], zoom_start=10)
       AreaMarker_home(sales_office,m)
    #df2
#-------------------------------------------------------------
    month = st.selectbox(
          'select Month',
          ('1','2','3','4','5','6','7','8','9','10','11','12'))
    #st.write(int(month))
    df3=df2[df2["month"]==int(month)]
    #df3
#-------------------------------------------------------------
    workday=st.selectbox(
	'select workday or weekend',
	('weekend','workday'))

    if workday=='workday':
        df4=df3[(df3["weekday"] >=2) & (df3["weekday"] <=6)]
        cdf=df2[(df2["weekday"] >=2) & (df2["weekday"] <=6)]
    else:
        df4=df3[(df3["weekday"] ==1) | (df3["weekday"] ==7)]
        cdf=df2[(df2["weekday"] ==1) | (df2["weekday"] ==7)]
    #cdf
#-------------------------------------------------------------
    daynight=st.selectbox(
	'select day or night',
	('day','night'))

    if daynight=='day':
        df5=df4[(df4["daynight"] <20)]
        cdf=cdf[(cdf["daynight"] <20)]
    else:
        df5=df4[(df4["daynight"] >=20)]
        cdf=cdf[(cdf["daynight"] >=20)]
    #df5
#-------------------------------------------------------------
    weather=st.selectbox(
	'select weather',
	('sunny&cloudy','rain','snow'))

    if weather=='sunny&cloudy':
        df6=df5[(df5["weather"] ==1) | (df5["weather"] ==2)]
        cdf=cdf[(cdf["weather"] ==1) | (cdf["weather"] ==2)]
    if weather=='rain':
        df6=df5[(df5["weather"] ==3)]
        cdf=cdf[(cdf["weather"] ==3)]
    if weather=='snow':
        df6=df5[(df5["weather"] ==5)]
        cdf=cdf[(cdf["weather"] ==5)]
    #df6
#-------------------------------------------------------------
    type=st.selectbox(
	'select type',
	('vehicle<>vehicle','person<>vehicle','vehicle_only'))
    if type=='vehicle<>vehicle':
        df7=df6[(df6["cont"] ==21)]
        cdf=cdf[(cdf["cont"] ==21)]
    if type=='vehicle_only':
        df7=df6[(df6["cont"] ==41)]
        cdf=cdf[(cdf["cont"] ==41)]        
    if type=='person<>vehicle':
        df7=df6[(df6["cont"] ==1)]
        cdf=cdf[(cdf["cont"] ==1)]
    #df7

#-------------------------------------------------------------

    df8=df7.loc[:,['x','y','p']]
    st.write("Counter",df8["x"].count())

#st.write("Count 1",cdf[cdf["month"]==1].count().min())
#st.write("Count 2",cdf[cdf["month"]==2].count().min())
#st.write("Count 3",cdf[cdf["month"]==3].count().min())
#st.write("Count 4",cdf[cdf["month"]==4].count().min())
#st.write("Count 5",cdf[cdf["month"]==5].count().min())
#st.write("Count 6",cdf[cdf["month"]==6].count().min())
#st.write("Count 7",cdf[cdf["month"]==7].count().min())
#st.write("Count 8",cdf[cdf["month"]==8].count().min())
#st.write("Count 9",cdf[cdf["month"]==9].count().min())
#st.write("Count 10",cdf[cdf["month"]==10].count().min())
#st.write("Count 11",cdf[cdf["month"]==11].count().min())
#st.write("Count 12",cdf[cdf["month"]==12].count().min())
#st.write(cdf.describe())

ndarray = np.array([[0, 0],
                    [1, cdf[cdf["month"]==1].count().min()],
                    [2, cdf[cdf["month"]==2].count().min()],
                    [3, cdf[cdf["month"]==3].count().min()],
                    [4, cdf[cdf["month"]==4].count().min()],
                    [5, cdf[cdf["month"]==5].count().min()],
                    [6, cdf[cdf["month"]==6].count().min()],
                    [7, cdf[cdf["month"]==7].count().min()],
                    [8, cdf[cdf["month"]==8].count().min()],
                    [9, cdf[cdf["month"]==9].count().min()],
                    [10, cdf[cdf["month"]==10].count().min()],
                    [11, cdf[cdf["month"]==11].count().min()],
                    [12, cdf[cdf["month"]==12].count().min()],
                   ])
summary=pd.DataFrame(ndarray, columns=["month", "count"])
#summary.loc[:,["month"]]
#st.line_chart(summary)

st.header("Trend analysis")
#st.write("settings",daynight)
#st.write("settings",weather)
#st.write("settings",type)
#st.bar_chart(summary.loc[:,["count"]])


#--------------------------------------------------------------
y = [1, 2, 3, 4, 5,6,7,8,9,10,11,12]
n = [cdf[cdf["month"]==1].count().min(),
     cdf[cdf["month"]==2].count().min(),
     cdf[cdf["month"]==3].count().min(),
     cdf[cdf["month"]==4].count().min(),
     cdf[cdf["month"]==5].count().min(),
     cdf[cdf["month"]==6].count().min(),
     cdf[cdf["month"]==7].count().min(),
     cdf[cdf["month"]==8].count().min(),
     cdf[cdf["month"]==9].count().min(),
     cdf[cdf["month"]==10].count().min(),
     cdf[cdf["month"]==11].count().min(),
     cdf[cdf["month"]==12].count().min()]
plt.style.use("ggplot")
def set_exoplanets(ax):
    ax.set_title("Trend", fontsize=5)
    ax.set_xlabel("Month", fontsize=5)
    ax.set_ylabel("Number of accidents", fontsize=5)
    ax.tick_params(axis='x', labelsize=5)
    ax.tick_params(axis='y', labelsize=5)

fig = plt.figure(figsize=(4,2))
ax=fig.add_subplot(111)
set_exoplanets(ax)
ax.bar(y, n)

st.pyplot(fig)
#--------------------------------------------------
#google map street view
urlt="<a href =""https://www.google.com/maps/@?api=1&map_action=pano&parameters&viewpoint="
urlb=" target=""_blank"" rel=""noopener noreferrer"">"
urlb2="<br>LINK </a>"

st.header("Map")
AreaMarker(df8,urlt,urlb,urlb2,m)
folium_static(m)
st.write("Data by https://www.npa.go.jp/publications/statistics/koutsuu/opendata/index_opendata.html")
st.write("settings---->",workday,"---->",daynight,"---->",weather,"---->",type)

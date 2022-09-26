import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title="Global Traffic Deaths Evolution", 
                   page_icon=":collision:", 
                   layout="wide"
)

df=pd.read_csv("C:/Users/hayda/OneDrive/Desktop/Traffic_Data.csv")

st.title("Global Traffic Deaths")


from PIL import Image
image = Image.open("C:/Users/hayda/OneDrive/Desktop/istockphoto-1268441700-612x612.jpg")

st.image(image)
st.header("Overview")
container = st.container()
container.write("This project explores a dataset that was published by the Global Burden of Disease Collaborative Network which measures the number of deaths from traffic crashes globally. The aim is to visualize the evolution of annual deaths and the observe the differences between countries from different economic statuses")

st.sidebar.header("Filters")

country = st.sidebar.selectbox(
    "Select Country:",
    options=df["Entity"].unique()
 
)

year = st.sidebar.selectbox(
    "Select Year:",
    options=df["Year"].unique()
)

driving_side = st.sidebar.selectbox(
    "Select Driving Side:",
    options=df["Sidedness"].unique()
)

death_rate_by_country = (
    df.groupby('Entity').agg({'Deaths': 'sum', 'Historical_Population': 'sum'})
    )


df_selection = df.query(
    "Entity == @country & Year == @year & Sidedness == @driving_side")

st.dataframe(df_selection)




st.title(":traffic_light: Traffic Accidents in the World")
st.markdown("##")



country_name = df_selection["Entity"].unique()
year_1 = df_selection["Year"].unique()
total_deaths = int(df_selection["Deaths"].sum())

left_column, middle_column, right_column = st.columns(3)
with left_column:
    st.subheader("Country :globe_with_meridians:")
    st.subheader(country_name)
with middle_column:
    st.subheader("Year :date:")
    st.subheader(year_1)
with right_column:
    st.subheader("Total Fatalities :warning:")
    st.subheader(total_deaths)
    
st.markdown("""---""")

# Creating charts
col1, col2 = st.columns(2)
with col1:
    deaths_by_year = df[df['Entity']==country].groupby(by=["Year"]).mean()[["Deaths"]]
    fig_yearly_deaths= px.line(
        deaths_by_year,
        x=deaths_by_year.index,
        y="Deaths",
        title="<b>Deaths by Year</b>",
        color_discrete_sequence=["red"] * len(deaths_by_year),
        template="plotly_white",
        )

    fig_yearly_deaths.update_layout(
        xaxis=dict(tickmode="linear"),
        plot_bgcolor="rgba(0,0,0,0)",
        yaxis=(dict(showgrid=False))
        )

    st.plotly_chart(fig_yearly_deaths)

with col2:
    population_growth= df[df['Entity']==country].groupby(by=["Year"]).mean()[["Historical_Population"]]
    fig_population_growth= px.line(
        population_growth,
        x=population_growth.index,
        y="Historical_Population",
        title="<b>Population Growth </b>",
        color_discrete_sequence=["lightsteelblue"] * len(population_growth),
        template="plotly_white",
        )

    fig_population_growth.update_layout(
        xaxis=dict(tickmode="linear"),
        plot_bgcolor="rgba(0,0,0,0)",
        yaxis=(dict(showgrid=False))
        )

    st.plotly_chart(fig_population_growth)


st.header("Summary")
container2 = st.container()
container2.write("From these visualizations, we can see that with constant advancements in the safety measures and technologies used by car manufacturers, the deaths from traffic accidents are decreasing over time in some countries (mostly first-world countries) but are increasing in poorer countries. This could be due to multiple factors such as hospital/medical support available in the country, quality of infrastructure, etc. Investments in road infrastructure, medical assistance proximity, and applying proper traffic laws would aid poorer countries and decrease the number of avoidable deaths from traffic accidents")


                 
            

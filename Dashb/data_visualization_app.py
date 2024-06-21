git push <remote_name> <branch_name>import streamlit as st
import plotly_express as px
import pandas as pd

#title of the app
st.title("Data Visualization app")

#add a sidebars
st.sidebar.subheader("Visualizatiom settings")

#To be able to upload file
uploaded_file = st.sidebar.file_uploader(label="Upload yor csv or Excel file",
                         type=["csv", "xlsx"])

global df
if uploaded_file is not None:

    print(uploaded_file)
    print("Hello")
    try:
        df = pd.read_csv(uploaded_file)
    except Exception as e:
        df = pd.read_excel(uploaded_file)

global numeric_columns
try:
    st.write(df)
    numeric_columns = list(df.select_dtypes(['float', 'int']).columns)
except:
    st.write("Please upload file to the application")


#add a select widget to the sidebar
chart_select = st.sidebar.selectbox(label= "Select the chart type",
                                    options= ("Scatterplot", "Boxplot", "Histogram", "Lineplot"))


if chart_select == "Scatterplot":
    st.sidebar.subheader("Scatterplot settings")
    try:
        x_values = st.sidebar.selectbox("X axis", options=numeric_columns)
        y_values = st.sidebar.selectbox("Y axis", options=numeric_columns)
        plot = px.scatter(data_frame=df, x=x_values, y=y_values)
        #display the chart
        st.plotly_chart(plot)
    except Exception as e:
        print("e")

import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

#configuration
st.set_page_config(page_title="Data Visualizer",layout="centered",page_icon="📊")

st.title("📊 Data Visualizer")
working_dir=os.path.dirname(os.path.abspath(__file__))
folder_path=f"{working_dir}/Data"

file_list=[f for f in os.listdir(folder_path) if f.endswith(".csv")]

selected_file=st.selectbox("Select a Title",file_list,index=None)



if selected_file:
    file_path=os.path.join(folder_path,selected_file)
    df=pd.read_csv(file_path)

    col1,col2=st.columns(2)
    columns=df.columns.tolist()

    with col1:
        st.write("")
        st.write(df.head())

    with col2:
        x_axis=st.selectbox("Select the x-axis",options=columns)
        y_axis=st.selectbox("Select the y-axis",options=columns)

        plot_list=['Line plot',"Bar plot"]

        selected_plot=st.selectbox("select a plot",options=plot_list)


    

    if st.button('Generate Plot'):
        fig,ax =plt.subplots(figsize=(6,4))


        if selected_plot=="Bar plot":
            sns.barplot(x=df[x_axis],y=df[y_axis],ax=ax)
        elif selected_plot=="Line plot":
            sns.lineplot(x=df[x_axis],y=df[y_axis],ax=ax)


        ax.tick_params(axis='x',labelsize=10)
        ax.tick_params(axis='y',labelsize=10)

        plt.title(f'{selected_plot} of {y_axis} vs {x_axis}',fontsize=12)
        plt.xlabel(x_axis,fontsize=10)                              
        plt.ylabel(y_axis,fontsize=10)   

        st.pyplot(fig)                           


#Created By Juan Minango

import os
import streamlit as st

#EDA pkgs
import pandas as pd
#Viz Pkgs
import matplotlib.pyplot as plt
import matplotlib 
matplotlib.use('Agg')
import seaborn as sns

def main():
    #Common ML Dataset#
    st.title("App para Explorar una Base de Datos o Dataset")
    st.subheader("Simple Explorador Base de Datos")

    html_temp = """
    <div style="background-color:tomato;"><p style="color:white;font-size:50px">JD-Techn</p></div>    
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    def file_selector(folder_path='./datasets'):  #ubicacion actual
        filenames = os.listdir(folder_path)
        selected_filename = st.selectbox("Selecciona el archivo", filenames)
        return os.path.join(folder_path,selected_filename)
    
    filename = file_selector()
    st.info("Has seleccionado {}".format(filename))

    #Leer Datos
    df = pd.read_csv(filename)
    #Mostrar Datos
    if st.checkbox("Mostrar Datos"):
        number = st.number_input("Numero de Filas",1)
        st.dataframe(df.head(number))
    
    #Mostrar Columnas
    st.text("Pulsas para Conocer el Nombre de las Columnas: ")
    if st.button("Nombre de las Columnas"):
        st.write(df.columns)
    
    #Mostrar Dimensiones
    if st.checkbox("Dimensiones Base de Datos"):
        data_dim = st.radio("Mostrar Dimensiones de la Base de Datos por: ", ("Filas","Columnas"))
        if data_dim == "Filas":
            st.text("Numero de Filas: ")
            st.write(df.shape[0])
        elif data_dim == "Columnas":
            st.text("Numero de Columnas: ")
            st.write(df.shape[1])
        else:
            st.write(df.shape)
    
    #Seleccionar Columna
    if st.checkbox("Seleccionar Columna para Mostrar"):
        all_columns = df.columns.tolist()
        select_columns = st.multiselect("Seleccionar", all_columns)
        new_df = df[select_columns]
        st.dataframe(new_df)
    
    #Mostrar Valores Target/Clase
    if st.button("Conteo de Valores"):
        st.text("Conteo de Valores por Target/Clase")
        st.write(df.iloc[:,-1].value_counts())
    
    #Mostrar Tipo de Datos
    if st.button("Tipo de Datos"):
        st.write(df.dtypes)
    
    #Mostrar Resumen
    if st.checkbox("Resumen"):
        st.write(df.describe().T)

    #Grafico y Visualizacion
    st.subheader("Visualizacion Datos")
    #Correlation
    #Seaborn
    if st.checkbox("Grafico Correlacion[Seaborn]"):
        st.write(sns.heatmap(df.corr(),annot=True))
        st.pyplot()

    #Pie Chart
    if st.checkbox("Grafico Pizza"):
        all_columns_name = df.columns.tolist()
        if st.button("Generamos Grafico Pizza"):
            st.success("Generando un Grafico Pizza")
            st.write(df.iloc[:,-1].value_counts().plot.pie(autopct="%1.1f%%"))
            st.pyplot()

    #Count Plot
    if st.checkbox("Grafico de Conteo de Valores"):
        st.text("Conteo de Valores por Target/Clase")
        all_columns_names = df.columns.tolist()
        primary_col = st.selectbox("Columna Primaria Agrupada por",all_columns_names)
        selected_columns_names = st.multiselect("Columnas Seleccionadas",all_columns_names)
        if st.button("Plot"):
            st.text("Generar Plot")
            if selected_columns_names:
                vc_plot = df.groupby(primary_col)[selected_columns_names].count()
            else:
                vc_plot = df.iloc[:,-1].value_counts()
            st.write(vc_plot.plot(kind="bar"))
            st.pyplot()



    #Grafico Personalizado
    st.subheader("Grafico Personalizado")
    all_columns_name = df.columns.tolist()
    type_of_plot = st.selectbox("Selecciona Tipo de Grafico",["area","bar","linea","hist","box","kde"])
    select_columns_names = st.multiselect("Columnas Seleccionadas para Graficar",all_columns_name)

    if st.button("Generar Grafico"):
        st.success("Generar Grafico Personalizado de {} para {}".format(type_of_plot,select_columns_names))

        #Graficando
        if type_of_plot == "area":
            cust_data = df[select_columns_names]
            st.area_chart(cust_data)
        
        elif type_of_plot == "bar":
            cust_data = df[select_columns_names]
            st.bar_chart(cust_data)

        elif type_of_plot == "linea":
            cust_data = df[select_columns_names]
            st.line_chart(cust_data)

        #Grafico Personalizado
        elif type_of_plot:
            cust_plot = df[select_columns_names].plot(kind=type_of_plot)
            st.write(cust_plot)
            st.pyplot()
    
    if st.button("Gracias"):
        st.balloons()

if __name__ == "__main__":
    main()
    


import streamlit as st
import pandas as pd
import plotly.express as px




def show_country_view(dfcopy):
    
    st.header('Fome Zero - Marketplace - Visão Países')
    st.markdown("""---""")


    st.markdown('#### Seções')
    tab1, tab2 = st.tabs(['Tipos de culinárias por países', 'Média de ranking de preço por país'])
    with tab1:
        colunas = ['Country Name', 'Cuisines']
        df_aux = dfcopy[colunas].drop_duplicates()
        df_aux = df_aux.sort_values('Country Name', ascending=True)
        st.dataframe(df_aux, use_container_width=True, hide_index=True)

    with tab2:
        colunas = ['Country Name', 'Price range']
        df_aux = dfcopy.loc[:, colunas].groupby('Country Name').mean().sort_values('Price range', ascending=False).round(2)
        st.dataframe(df_aux, use_container_width=True)

    st.markdown('### Gráficos')
   
    with st.container():
        st.markdown('##### Médias de notas agregadas por países')
        colunas = ['Country Name', 'Aggregate rating']
        df_aux = dfcopy.loc[:, colunas].groupby('Country Name').mean().sort_values('Aggregate rating', ascending=True)
        df_aux = df_aux.reset_index()
        fig = px.bar(df_aux.round(2), x='Country Name', y='Aggregate rating', text='Aggregate rating')        
       
        fig.update_layout( 
            xaxis_title = 'Países',
            yaxis_title = 'Notas médias agregadas'
            # template = 'plotly_dark'
        )

        fig.update_traces(texttemplate='%{text:.2f}', textposition='inside')
        st.plotly_chart(fig)

    with st.container():
        col1, col2 = st.columns(2, gap='large')
        with col1:
            st.markdown('##### Quantidades de cidades registradas por países')
            colunas = ['Country Name', 'City']
            df_aux = dfcopy.loc[:, colunas].groupby('Country Name').nunique()
            df_aux = df_aux.reset_index()
            fig = px.bar(df_aux, x = 'Country Name', y = 'City', text = 'City')
    
            fig.update_layout( 
                xaxis_tickangle=-45,
                xaxis_title = 'Países',
                yaxis_title = 'Quantidades de cidades'
            )
    
            fig.update_traces(textposition='inside')
            st.plotly_chart(fig)


        with col2:
            st.markdown('##### Quantidades de restaurantes por países')
            colunas = ['Country Name', 'Restaurant ID']
            df_aux = dfcopy.loc[:, colunas].groupby('Country Name').count()
            df_aux = df_aux.reset_index()
            fig = px.bar(df_aux, x='Country Name', y='Restaurant ID', text = 'Restaurant ID')
            
            fig.update_layout( 
                xaxis_tickangle=-45,
                xaxis_title = 'Países',
                yaxis_title = 'Quantidades de restaurantes'
            )
    
            fig.update_traces(textposition='inside')
            st.plotly_chart(fig)
    
        











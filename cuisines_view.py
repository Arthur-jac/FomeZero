import streamlit as st
import pandas as pd
import plotly.express as px




def show_cuisines_view(dfcopy):
    st.header('Fome Zero - Marketplace - Visão Tipos Culinários')
    st.markdown("""---""")

    st.markdown('#### Seções')
    tab = st.tabs(['Tipos culinários registrados'])
    with tab[0]:
        df_aux = pd.DataFrame(dfcopy['Cuisines'].unique(), columns=['Cuisines'])
        st.dataframe(df_aux, use_container_width=True, hide_index=True)

    st.markdown('### Gráficos')

    with st.container():
        st.markdown('#### Quantidades de tipos culinários por país')
        colunas = ['Country Name', 'Cuisines']
        qtd_culinaria_por_pais = dfcopy.loc[:, colunas].groupby('Country Name').nunique().reset_index()
        fig = px.bar(qtd_culinaria_por_pais, x='Cuisines', y='Country Name', text='Cuisines')
        
        fig.update_layout(
            xaxis_title = 'Tipos de Culinárias',
            yaxis_title = 'Países'
            # template = 'plotly_dark'
        )
        fig.update_traces(textposition='inside')
        
        st.plotly_chart(fig, use_container_width=True)

    with st.container():
        col1, col2 = st.columns(2, gap='large')
        with col1:
            st.markdown('#### Top 10 Culinárias bem avaliadas')
            colunas = ['Cuisines', 'Aggregate rating']
            df_aux = dfcopy.loc[:, colunas].groupby('Cuisines').mean()
            df_aux = df_aux.sort_values('Aggregate rating', ascending=False).reset_index()
            df_aux = df_aux.head(10)

            fig = px.bar(df_aux.round(2), x='Cuisines', y='Aggregate rating', text='Aggregate rating')
            fig.update_layout(
                xaxis_tickangle=-45,
                xaxis_title='Tipos de Culinárias',
                yaxis_title = 'Média de notas'
            )
            fig.update_traces(textposition='inside')

            st.plotly_chart(fig, use_container_width=True)
            
        with col2:
            st.markdown('#### Top 10 Culinárias mal avaliadas')
            colunas = ['Cuisines', 'Aggregate rating']
            df_aux = dfcopy.loc[:, colunas].groupby('Cuisines').mean()
            df_aux = df_aux.sort_values('Aggregate rating', ascending=True).reset_index()
            df_aux = df_aux.head(10)

            fig = px.bar(df_aux.round(2), x='Cuisines', y='Aggregate rating', text='Aggregate rating')
            fig.update_layout(
                xaxis_tickangle=-45,
                xaxis_title='Tipos de Culinárias',
                yaxis_title = 'Média de notas'
            )
            fig.update_traces(textposition='inside')

            st.plotly_chart(fig, use_container_width=True)
            
    with st.container():
        
        df_aux = dfcopy.groupby(['Cuisines', 'Country Name'], as_index=False)['Aggregate rating'].mean()
        df_aux = df_aux.sort_values('Aggregate rating', ascending=False).head(20)
        
        fig = px.scatter(
            df_aux,
            x='Cuisines',
            y='Aggregate rating',
            color='Country Name',  
            size='Aggregate rating', 
            hover_name='Country Name', 
            title='As 20 melhores culinárias com base nas avaliações médias destacadas por países',
            labels={'Cuisines': 'Tipos de culinárias', 'Aggregate rating': 'Notas agregadas em média'},
            size_max=30
        ) 
        
    
        fig.update_layout(
            legend_title='País',
            xaxis_title='Tipos de Culinárias',
            yaxis_title='Notas Agregadas em média',
            xaxis_tickangle=-45, 
            xaxis={'categoryorder': 'total ascending'}
        )
        
        st.plotly_chart(fig, use_container_width=True)

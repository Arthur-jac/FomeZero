import streamlit as st
import pandas as pd
import plotly.express as px




def show_city_view(dfcopy):
    
    st.header('Fome Zero - Marketplace - Visão Cidades')
    st.markdown("""---""")

    st.markdown('#### Seções')
    tab1, tab2 = st.tabs(['Métricas', 'Cidades registradas'])
    with tab1:
        col1, col2 = st.columns(2, gap='large')
        with col1:
            df_aux = dfcopy.groupby('City')['Aggregate rating'].mean()
            rating_city_idxmax = df_aux.idxmax()
            rating_city_max = df_aux.max()
            info_string = f"{rating_city_idxmax}/{rating_city_max:.2f}"
           
            st.metric(
                label="Cidade com maior classificação",
                value=info_string
            )

        with col2: 
            df_aux = dfcopy.groupby('City')['Aggregate rating'].mean()
            rating_city_idxmin = df_aux.idxmin()
            rating_city_min = df_aux.min()
            info_string = f"{rating_city_idxmin}/{rating_city_min:.2f}"
            
            st.metric(
                label="Cidade com pior classificação",
                value=info_string
            )
    with tab2:
        df_aux = dfcopy.loc[:, 'City'].unique()
        df_aux = pd.DataFrame(dfcopy['City'].unique(), columns=['City'])
        st.dataframe(df_aux, use_container_width=True, hide_index=True)
        
    
    with st.container():
        col1, col2 = st.columns(2, gap='large')
        with col1:
            st.markdown('#### As 10 Cidades mais caras em média')
            colunas = ['City', 'Price range']
            df_aux = dfcopy.loc[:, colunas].groupby('City').mean().sort_values('Price range', ascending=False)
            df_aux = df_aux.head(10)
            df_aux = df_aux.reset_index()
            fig = px.bar(df_aux.round(2), x='Price range', y='City', text='Price range')

            fig.update_layout(
                xaxis_title = 'Ranking de preços',
                yaxis_title = 'Cidades'  
            )
            st.plotly_chart(fig, use_container_width=True)
                        
        with col2:
            st.markdown('#### As 10 Cidades com mais Restaurantes')
            colunas = ['City', 'Restaurant ID']
            df_aux = dfcopy.loc[:, colunas].groupby('City').count().sort_values('Restaurant ID', ascending = False).head(10)
            df_aux = df_aux.reset_index()
            fig = px.bar(df_aux, x = 'City', y = 'Restaurant ID', text = 'Restaurant ID')
    
            fig.update_layout( 
                xaxis_tickangle=-45,
                xaxis_title = 'Cidades',
                yaxis_title = 'Quantidades de restaurantes'
            )
            
            fig.update_traces(textposition='inside')
            st.plotly_chart(fig, use_container_width=True)

    with st.container(): 
        st.markdown('#### As 5 Cidades com mais votos')
        colunas = ['City', 'Restaurant Name', 'Votes']
        df_aux = dfcopy.loc[:, colunas].groupby('City').count()
        df_aux = df_aux.sort_values('Votes', ascending=False).head(5)
        df_aux = df_aux.reset_index()
    
        fig = px.bar(df_aux, x='City', y='Votes', text='Votes')

        fig.update_layout( 
            xaxis_title = 'Cidades',
            yaxis_title = 'Quantidades de votos'
        )
            
        fig.update_traces(textposition='inside')

        st.plotly_chart(fig, use_container_width=True)
    
    

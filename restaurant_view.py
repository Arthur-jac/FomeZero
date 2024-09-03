import streamlit as st
import pandas as pd
import plotly.express as px



def show_restaurant_view(dfcopy):
    
    st.header('Fome Zero - Marketplace - Visão Restaurantes')
    st.markdown("""---""")

    st.markdown('#### Seções')

    tab1, tab2 = st.tabs(['Melhores restaurantes avaliados', 'Piores restaurantes avaliados'])
    with tab1:
        st.subheader('Top 10 melhores restaurantes bem avaliados em média')
        colunas = ['Restaurant Name', 'Rating text', 'Aggregate rating']
        df_aux = dfcopy.loc[:, colunas].groupby(['Restaurant Name', 'Rating text']).mean().sort_values('Aggregate rating', ascending=False).head(10)
        st.dataframe(df_aux.round(2), use_container_width=True)
        
    with tab2:
        st.subheader('Top 10 piores restaurantes mal avaliados em média')
        colunas = ['Restaurant Name', 'Rating text', 'Aggregate rating']
        condicao = dfcopy['Aggregate rating'] != 0
        df_aux = dfcopy.loc[condicao, colunas].groupby(['Restaurant Name', 'Rating text']).mean().sort_values('Aggregate rating', ascending=True).head(10)
        st.dataframe(df_aux.round(2), use_container_width=True)

    st.markdown('### Gráficos')
    
    with st.container():
        col1, col2 = st.columns(2, gap='large')

        with col1:
            
            df_aux = dfcopy['Has Table booking'].value_counts().reset_index()
            fig = px.pie(df_aux, names = 'Has Table booking', values = 'count', title = 'Percentual de restaurantes para reservas')
            
            fig.update_layout(
                legend_title='Reserva de Mesa',
                legend=dict(
                    title='Reserva de Mesa',
                    traceorder='normal',
                    orientation='v' 
                )
            )

            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            df_aux = dfcopy['Has Online delivery'].value_counts().reset_index()
            fig = px.pie(df_aux, names='Has Online delivery', values='count', title='Percentual de restaurantes para delivery')
                        
            fig.update_layout(
                legend_title='Faz delivery',
                legend=dict(
                    title='Faz delivery',
                    traceorder='normal', 
                    orientation='v'  
                )
            )
            
            st.plotly_chart(fig, use_container_width=True)

    with st.container():
        st.markdown('#### Quantidades de restaurantes por tipos de preço')
        colunas = ['Price type', 'Restaurant ID']
        df_aux = dfcopy.loc[:, colunas].groupby('Price type').count()
        df_aux = df_aux.reset_index()
    
        fig = px.bar(df_aux, x='Price type', y='Restaurant ID', text='Restaurant ID')
        fig.update_layout( 
            xaxis_title = 'Tipos de preço',
            yaxis_title = 'Quantidades de restaurantes'
        )
    
        fig.update_traces(textposition='inside')
        st.plotly_chart(fig, use_container_width=True)




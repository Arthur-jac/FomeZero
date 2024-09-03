import streamlit as st
import pandas as pd
import plotly.express as px
import folium
import streamlit.components.v1 as components
from folium.plugins import MarkerCluster



def show_general_view(dfcopy):
    
    st.header('Fome Zero - Marketplace - Visão Geral')
    st.markdown("""---""")
    
    st.markdown('#### Métricas Gerais')
    
    
    with st.container():
        col1, col2, col3, col4, col5 = st.columns(5, gap='large')
        
        with col1:
            qtd_restaurantes_unicos = dfcopy['Restaurant ID'].nunique()
            col1.metric('Qtd. Restaurantes', qtd_restaurantes_unicos)
        
        with col2:
            qtd_pais_unico = dfcopy['Country Code'].nunique()
            col2.metric('Qtd. Países', qtd_pais_unico)
        
        with col3:
            qtd_cidades_unicas = dfcopy['City'].nunique()
            col3.metric('Qtd. Cidades', qtd_cidades_unicas)
        
        with col4:
            qtd_avalicoes = dfcopy['Aggregate rating'].count()
            col4.metric('Qtd. Avaliações', qtd_avalicoes)
        
        with col5:
            qtd_tipo_cul_unico = dfcopy['Cuisines'].nunique()
            col5.metric('Qtd. Culinárias', qtd_tipo_cul_unico)

    st.markdown('#### Seções')
    tab1, tab2 = st.tabs(['Localização dos Restaurantes', 'Tabela Geral'])
    with tab1:
        
        st.markdown('#### Localização dos Restaurantes')
        
        colunas = ['Restaurant Name', 'Latitude', 'Longitude']
        df_aux = dfcopy.loc[:, colunas]
        df_aux = df_aux[df_aux['Restaurant Name'] != 'NaN']
        
        map_ = folium.Map(zoom_start=11)
        marker_cluster = MarkerCluster().add_to(map_)
        
        for index, location_info in df_aux.iterrows():
            folium.Marker(
                location=[location_info['Latitude'], location_info['Longitude']],
                popup=location_info['Restaurant Name']
            ).add_to(marker_cluster)
        
        map_html = map_._repr_html_()
        components.html(map_html, height=600)

    with tab2: 
        dados = dfcopy.loc[:, :]
        st.dataframe(dados, use_container_width=True, hide_index=True)
    
        


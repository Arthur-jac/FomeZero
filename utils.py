import streamlit as st
import pandas as pd


COUNTRIES = {
    1: "India",
    14: "Australia",
    30: "Brazil",
    37: "Canada",
    94: "Indonesia",
    148: "New Zeland",
    162: "Philippines",
    166: "Qatar",
    184: "Singapure",
    189: "South Africa",
    191: "Sri Lanka",
    208: "Turkey",
    214: "United Arab Emirates",
    215: "England",
    216: "United States of America",
}

mapping = {0: 'Não', 1: 'Sim'}

def color_name(color_code):
    return COLORS[color_code]


def country_name(country_id):
    return COUNTRIES.get(country_id, 'Unknown Country')

def get_first_cuisine(cuisines):
    if pd.isna(cuisines):
        return '' 
    cuisines_str = str(cuisines)
    return cuisines_str.split(',')[0]

def create_price_tye(price_range):
    if price_range == 1:
        return "cheap"
    elif price_range == 2:
        return "normal"
    elif price_range == 3:
        return "expensive"
    else:
        return "gourmet"

def clean_data(dfcopy):
    dfcopy = dfcopy.dropna()
    dfcopy = dfcopy.drop_duplicates()
    dfcopy = dfcopy.reset_index(drop=True)
    
    return dfcopy
    
    
def data_init():    
    df = pd.read_csv('zomato.csv')
    
    dfcopy = df.copy()
    
    dfcopy['Country Name'] = dfcopy['Country Code'].apply(country_name)
    dfcopy['Cuisines'] = dfcopy['Cuisines'].apply(get_first_cuisine)
    dfcopy['Price type'] = dfcopy['Price range'].apply(create_price_tye) 
    dfcopy['Has Online delivery'] = dfcopy['Has Online delivery'].map(mapping)
    dfcopy['Has Table booking'] = dfcopy['Has Table booking'].map(mapping)
    dfcopy = clean_data(dfcopy)
    
    return dfcopy


def home():
    st.header('Bem-vindo(a) ao Projeto de Análise de Dados - Fome Zero')

    st.markdown('#### Introdução')
    st.markdown(
        """
        Este projeto tem como objetivo fornecer uma análise detalhada dos dados relacionados ao programa Fome Zero.
        
        Utilize a navegação na barra lateral para ajustar filtros interativos e explorar diferentes páginas da aplicação. Abaixo, você encontrará uma breve descrição das abas disponíveis:
        """
    )

    st.markdown(
        """
        * **Geral**: exibe métricas gerais sobre os restaurantes, como a quantidade de restaurantes, países, cidades, avaliações e tipos de culinária. Em seguida, a visualização é dividida em duas seções: localização dos restaurantes em um mapa e uma tabela geral.
        * **Países**: apresenta uma visão detalhada sobre os países do marketplace. A interface é dividida em seções: Tipos de culinárias e média de ranking de preço por país. Médias de notas agregadas, quantidades de cidades registradas e quantidades de restaurantes por país.
        * **Cidades**: exibe informações detalhadas sobre cidades do marketplace, e é divida em seções: Métrica da cidade com a maior e a menor classificação média. Tabela com as cidades e suas culinárias únicas. Gráficos das, Top 10 cidades mais caras em média, Top 10 cidades com mais restaurantes e Top 5 cidades com mais votos.
        * **Restaurantes**: mostra informações sobre restaurantes em um marketplace, com os Top 10 melhores restaurantes e Top 10 piores restaurantes. Gráficos de percentual de restaurantes para reservas, percentual de restaurantes para delivery e quantidades de restaurantes por tipos de preço.
        * **Tipos Culinários**: fornece uma análise detalhada sobre os tipos culinários do marketplace, com os tipos culinários registrados. Gráficos com as quantidades de tipos culinários por país, Top 10 culinárias bem avaliadas, Top 10 culinárias mal avaliadas e Top 20 culinárias com base nas avaliações médias.
        """
    )

    st.markdown('#### Observações')
    st.markdown(
        """
        Cada página contém seções interativas que você pode explorar clicando nos itens.
        Explore as diferentes seções para obter uma compreensão completa dos dados.
        """
    )
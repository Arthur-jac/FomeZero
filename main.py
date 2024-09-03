import streamlit as st
from general_view import show_general_view
from country_view import show_country_view
from city_view import show_city_view
from cuisines_view import show_cuisines_view
from restaurant_view import show_restaurant_view
from utils import data_init, home


st.set_page_config(
    page_title="Análise de Dados - Fome Zero",
    page_icon="🍗",
    layout="wide"
)

def main():
    dfcopy = data_init()

    st.sidebar.markdown('### Filtros')
    country = st.sidebar.multiselect(
        'Filtro - País', 
        list(dfcopy.loc[:, 'Country Name'].unique()),
        default = list(dfcopy.loc[:, 'Country Name'].unique())
    ) 

    linhas_selecionadas = dfcopy['Country Name'].isin(country)
    dfcopy = dfcopy.loc[linhas_selecionadas, :]

    price_type = st.sidebar.multiselect(
        'Filtro - Tipo preço', 
        list(dfcopy.loc[:, 'Price type'].unique()),
        default = list(dfcopy.loc[:, 'Price type'].unique())
    ) 

    linhas_selecionadas = dfcopy['Price type'].isin(price_type)
    dfcopy = dfcopy.loc[linhas_selecionadas, :]

    st.sidebar.markdown( """---""" )
    
    st.sidebar.title('Navegação')
    
    selection = st.sidebar.radio('', ['🏠 Página Inicial', '📊 Geral', '🌍 Países', '🏙️ Cidades', '🍽️ Restaurantes', '🍲 Tipos Culinários'])

    if selection == '🏠 Página Inicial':
        home()
    elif selection == '📊 Geral':
        show_general_view(dfcopy)
    elif selection == '🌍 Países':
        show_country_view(dfcopy)
    elif selection == '🏙️ Cidades':
        show_city_view(dfcopy)
    elif selection == '🍽️ Restaurantes':
        show_restaurant_view(dfcopy)
    elif selection == '🍲 Tipos Culinários':
        show_cuisines_view(dfcopy)
    else:
        st.title('Página não encontrada')


if __name__ == '__main__':
    main()



import pandas as pd
import streamlit as st
from st_aggrid import AgGrid
from datetime import datetime
from actors.service import ActorService


def show_actors():
    actor_service = ActorService()
    actors = actor_service.get_actors()

    if actors:
        st.write('Lista de Atores/Atrizes')
        actors_df = pd.DataFrame(actors)
        AgGrid(
            data=actors_df,
            filter=True,
            key='actors_grid',
        )
    else:
        st.warning('Nenhum ator/atriz encontrado.')

    st.title('Adicionar Ator/Atriz')
    name = st.text_input('Nome do Ator/Atriz')
    birthday = st.date_input(
        label='Data de Nascimento',
        value=datetime.today(),
        min_value=datetime(1600, 1, 1).date(),
        max_value=datetime.today(),
        format='DD/MM/YYYY',
    )
    nationality = st.selectbox('Nacionalidade', ['Brasil', 'Estados Unidos', 'Canada'])

    if st.button('Adicionar'):
        new_actor = actor_service.create_actor(
            name=name,
            birthday=birthday,
            nationality=nationality,
        )
        if new_actor:
            st.rerun()
        else:
            st.error('Erro ao adicionar ator/atriz.')

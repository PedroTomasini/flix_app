import pandas as pd
import streamlit as st
from st_aggrid import AgGrid
from datetime import datetime
from actors.service import ActorService
from genres.service import GenreService
from movies.service import MovieService


def show_movies():
    movie_service = MovieService()
    movies = movie_service.get_movies()

    if movies:
        st.write('Lista de Filmes')
        movies_df = pd.json_normalize(movies)
        movies_df = movies_df.drop(columns=['actors', 'genre.id'])
        AgGrid(
            data=movies_df,
            filter=True,
            key='movies_grid',
        )
    else:
        st.warning('Nenhum filme encontrado.')

    st.title('Cadastrar Filme')

    title = st.text_input('Título')
    genre_service = GenreService()
    genres = genre_service.get_genres()
    genres_options = {genre['name']: genre['id'] for genre in genres}
    selected_genre = st.selectbox('Gênero', list(genres_options.keys()))
    release_date = st.date_input(
        label='Data de Nascimento',
        value=datetime.today(),
        min_value=datetime(1600, 1, 1).date(),
        max_value=datetime.today(),
        format='DD/MM/YYYY',
    )
    actor_service = ActorService()
    actors = actor_service.get_actors()
    actors_options = {actor['name']: actor['id'] for actor in actors}
    selected_actors = st.multiselect('Atores/Atrizes', list(actors_options.keys()))
    selected_actors_ids = [actors_options[name] for name in selected_actors]
    resume = st.text_area('Resumo')

    if st.button('Cadastrar'):
        new_movie = movie_service.create_movie(
            title=title,
            genre=genres_options[selected_genre],
            release_date=release_date,
            actors=selected_actors_ids,
            resume=resume,
        )
        if new_movie:
            st.rerun()
        else:
            st.error('Erro ao cadastrar filme.')

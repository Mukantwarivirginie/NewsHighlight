from flask import render_template
from app import app
from .request import get_sources

from .requests import get_movies,get_movie



@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    # Getting popular movie
    popular_general = get_sources('general')
    upcoming_category = get_sources('business')
    now_showing_category = get_sources('sports')
    title = 'Home - Welcome to The best Movie Review Website Online'
    return render_template('index.html', title = title, popular =popular_general, upcoming =upcoming_category, now_showing = now_showing_category )







    @app.route('/movie/<int:id>')
def movie(id):

    '''
    View movie page function that returns the movie details page and its data
    '''
    movie = get_movie(id)
    title = f'{movie.title}'

    return render_template('movie.html',title = title,movie = movie)
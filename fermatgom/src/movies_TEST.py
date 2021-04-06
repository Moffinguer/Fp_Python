#-*- coding:utf-8 -*-
'''
Created on 13 nov. 2020

@author: Fernando José Mateos Gómez
'''
from movies import *

def test_read_file(rute):
    return read_file(rute)

def test_filter_by_genre(movies,list_of_genres):
    return filter_by_genres(movies, list_of_genres)

def test_get_genres_by_year(movies,year=2000):
    return get_genres_by_year(movies,year)

def test_count_genres_by_year(movies,year):
    return count_genres_by_year(movies, year)

def test_average_users_by_rating(movies,rate):
    return average_users_by_rating(movies, rate)

def test_get_movies_ordered_by_title(movies,order,min_of_ocurrences):
    return get_movies_ordered_by_title(movies, order, min_of_ocurrences)

def test_get_movies_max_budget(movies):
    return get_movies_max_budget(movies)

def test_get_number_films_lang_color(movies,lang,color):
    return get_number_films_lang_color(movies,lang,color)

def test_list_of_countries_speaklang(movies,lang):
    return list_of_countries_speaklang(movies, lang)

def test_max_min_of_film_by_duration(data):
    temp= max_min_of_film_by_duration(data)
    print(f"Pelicula con la menor duracion {temp[1]}")
    print(f"Pelicula con la mayor duracion {temp[0]}")

def test_counter_films_of_color(data):
    return counter_films_of_color(data)

def test_get_longest_shorter_by_country(data):
    dumb=get_longest_shorter_by_country(data)
    for i in dumb:
        print(f"{i} --> {dumb[i]}")

def test_ar_med_num_critic_by_director(data):
    dumb=ar_med_num_critic_by_director(data)
    for i in dumb:
        print(f"{i} --> {dumb[i]}")

def test_get_films_by_content_rating(data):
    
    dumb=get_films_by_content_rating(data)
    for i in dumb:
        print(f"{i} --> {dumb[i]}")

def test_get_user_rate_films_by_lang(data,n,select):
    dumb=get_user_rate_films_by_lang(data,n,select)
    for i in dumb:
        print(f"{i} ==> \n Mejores: {dumb[i][0]} \n Peores {dumb[i][1]}")

if __name__ == '__main__':
    data=test_read_file("../data/movies.csv")
    #En caso de no poder ver el test de una linea, comente las funciones que no correspondan a esa función
    print(f"Datos extraidos: {data[:30]}")
    print(f"Películas con estos géneros: {test_filter_by_genre(data,['Sci-Fi'])[:30]}")
    print(f"Generos por año: {set(test_get_genres_by_year(data))}")
    print(f"Cuantos generos hay en ese año: {test_count_genres_by_year(data, 2009)}")
    print(f"Media de PG-13: {test_average_users_by_rating(data, 'PG-13')}")
    print(f"Orden alfabético: {test_get_movies_ordered_by_title(data, True, 5)[:10]}")
    print(f"Maximo presupuesto: {test_get_movies_max_budget(data)}")
    print(f"Numero de peliculas que: {test_get_number_films_lang_color(data, 'Spanish', ' Black and White')}")
    print(f"Paises con peliculas que hablan: {test_list_of_countries_speaklang(data, 'French')}")
    test_max_min_of_film_by_duration(data)
    print(f"Numero peliculas por color: {test_counter_films_of_color(data)}")
    print(f"Peliculas más cortas y largas por pais:")
    test_get_longest_shorter_by_country(data)
    print(f"Media aritmética de la critica por director: ")
    test_ar_med_num_critic_by_director(data)
    print(f"Peliculas por publico que tiene que puede verlo: ")
    test_get_films_by_content_rating(data)
    n,select=5,None
    print(f"Las {n} peliculas, peores y mejores valoradas por idioma")
    test_get_user_rate_films_by_lang(data, n, select)
#-*- coding:utf-8 -*-
'''
Created on 11 nov. 2020

@author: Fernando José Mateos Gómez
'''
import csv
from collections import namedtuple
def read_file(rute):
    '''
    Input: (Rute) Ruta relativa con el archivo csv deseado
    Ouput: Movies(str,str,int,int,list,str,str,,int,str,str,str,int,int,float,float)
    '''
    
    dumb=[]
    Movies=namedtuple("Movies",["color","director_name","num_critic_for_reviews",
                               "duration","genres",
                               "actor_1_name","movie_title","num_user_for_reviews",
                               "language","country","content_rating","budget","title_year",
                               "imdb_score","aspect_ratio"])
    with open(rute,"rt",encoding="utf-8") as f:
        file=csv.reader(f,delimiter=";")
        next(file)
        for i in file:
            color,dir_name,actor_1_name,movie_title=i[0],i[1],i[5],i[6].replace(u'\xa0', u' ')
            num_critic_reviews,duration,num_user_for_reviews=int(i[2]),int(i[3]),int(i[7])
            lang,country,content_rating=i[8],i[9],i[10]
            budget,title_year=int(i[11]),int(i[12])
            imdb_score,aspect_ratio=float(i[13]),float(i[14])              
            genres=i[4].split("|")
            dumb.append(Movies(color,dir_name,num_critic_reviews,duration,genres,actor_1_name,movie_title,
                                num_user_for_reviews,lang,country,content_rating,budget,title_year,
                                imdb_score,aspect_ratio))
                
    return dumb

def filter_by_genres(movies,genres):
    '''
    Input: (movies,genres) Dataset con las peliculas de tipo Movies, y una lista con generos
    Ouput: Listado con todas las peliculas que son de algún genero de la lista genres
    '''
    dumb=[]
    for i in movies:
        j=0
        not_Found=True
        while not_Found and j<len(genres):
            if genres[j] in i.genres:
                not_Found=not not_Found
                dumb.append(i)
            j+=1
    return dumb

def get_genres_by_year(movies,year=2009):
    '''
    Input: (movies,year) Dataset de tipo Movies, y un año de busqueda, por defecto vale 2009
    Output: Listado con todos los generos de todas las peliculas, se repiten, que se encuentran en el año seleccionado
    '''
    dumb=tuple()
    for i in movies:
        if i.title_year==year:
            dumb+=tuple(i.genres)
    print(dumb)
    return list(dumb)

def count_genres_by_year(movies,year):
    '''
    Input: (movies,year) Dataset de tipo Movies, y un año de búsqueda
    Output: Devuelve una lista de tuplas con todas las veces que se repite un género determinado en un año
    '''
    dumb=get_genres_by_year(movies, year)
    number_of_genres=dict()
    for i in dumb:
        if i not in number_of_genres:
            number_of_genres[i]=0
        number_of_genres[i]+=1
    dumb=[]
    for i in number_of_genres:
        dumb.append((i,number_of_genres[i]))
    return dumb

def average_users_by_rating(movies,rate="PG"):
    '''
    Input: (movies,rate) Dataset de tipo Movies, y marca de la película, con edad recomendada para ver la película, por defecto 'PG'
    Output: Devuelve una media correspondiente al número de críticas por los usuarios para las películas con edad recomendada
    '''
    dumb=[i.num_critic_for_reviews for i in movies if i.content_rating==rate]
    res=0
    length=len(dumb)
    if length>0:
        res=sum(dumb)/length
    return res

def get_movies_ordered_by_title(movies,order=False,min_of_ocurrences=10):
    '''
    Input: (movies,order,min_of_ocurrences) Dataset de tipo Movies, orden en que se ordena el dataset (Por defecto de forma ascendente), minimo de 
            elementos que se retornarán, por defecto 10
    Outut: Devuelve un listado de películas ordenadas a antojo del usuario, en función del titulo de la película. Solo se mostrarán tantas películas como
            películas haya o las enviadas por parámetro
    '''
    dumb=sorted(movies,reverse=order,key=lambda x:x.movie_title)
    if len(dumb)<min_of_ocurrences or min_of_ocurrences<0:
        min_of_ocurrences=len(dumb)
    return dumb[:min_of_ocurrences]

def get_movies_max_budget(movies):
    '''
    Input: (movies) Dataset de tipo Movies
    Outut: Devuelve un listado con las películas con máximo presupuesto
    '''
    maximum_budget=max(movies,key=lambda x:x.budget).budget
    return [i for i in movies if maximum_budget==i.budget]

def get_number_films_lang_color(movies,lang,color):
    '''
    Input: (movies,lang,color) Dataset de tipo Movies, lenguaje str, color de la película str
    Outut: Devuelve un número con la cantidad de películas que hablan en el idioma seleccionado y que coincidan con el campo color
    '''
    return len([i.color for i in movies if i.color.upper()==color.upper() and i.language==lang.upper()])

def list_of_countries_speaklang(movies,lang):
    '''
    Input: (movies,lang) Dataset de tipo Movies, y un lenguaje str
    Outut: Lista con los paises que hablan el idioma seleccionado
    '''
    return {i.country for i in movies if i.language.upper()==lang.upper()}

def max_min_of_film_by_duration(data):
    '''
    Input: (movies) Dataset de tipo Movies
    Outut: Una tupla con la duracion mayor y menor del dataset
    '''
    max_val,min_val=data[0],data[0]
    for i in data[1:]:
        if i.duration>max_val.duration:
            max_val=i
        elif i.duration<min_val.duration:
            min_val=i
    return max_val,min_val

def counter_films_of_color(movies):
    '''
    Input: (movies) Dataset de tipo Movies
    Outut: Un diccionario que devuelve el numero de peliculas en función del color en que esté
    '''
    dumb=dict()
    for i in movies:
        color=i.color
        if color not in dumb:
            dumb[color]=0
        dumb[color]+=1
    return dumb
  
def get_longest_shorter_by_country(data):
    '''
    Input: (movies) Dataset de tipo Movies
    Outut: Un diccionario con el que se devuelve la pelicula más larga y más corta en función del pais
    '''
    dumb=dict()
    for i in data:
        country= i.country
        if country not in dumb:
            dumb[country]=[]
        dumb[country].append(i)
    for i in dumb:
        dumb[i]=max_min_of_film_by_duration(dumb[i])
    return dumb

def ar_med_num_critic_by_director(data):
    '''
    Input: (movies) Dataset de tipo Movies
    Outut: Un diccionario de tuplas con la media por la critica en función del director y
             el valor total de la critica
    '''
    dumb=dict()
    for i in data:
        dir_name=i.director_name
        if dir_name not in dumb:
            dumb[dir_name]=[]
        dumb[dir_name]+=[i]
        
    for i in dumb:
        size=dumb[i]
        total_of_review=sum(x.num_critic_for_reviews for x in size)
        temp=(total_of_review/len(size),total_of_review)
        dumb[i]=temp
    return dumb
        
def get_films_by_content_rating(data):
    '''
    Input: (movies) Dataset de tipo Movies
    Outut: Un diccionario que devuelve las peliculas por rating del vidente
    '''
    dumb=dict()
    for i in data:
        rat=i.content_rating
        if rat not in dumb:
            dumb[rat]=[]
        dumb[rat]+=[i]
    return dumb

def get_user_rate_films_by_lang(data,n=1,select=None):
    '''
    Input: (movies,n,select) Dataset de tipo Movies, un numero entero que indica cuantas peliculas quiero ver, filtro que 
                                indica si quiero a las más vistas o las menos o ambas
    Outut: Un diccionario que devuelve las n peliculas mejores y peores valoradas
    Error: Devuelve none en caso de que n sea un numero menor o igual que 0
    '''
    dumb=dict()
    if n>0:
        for i in data:
            lang=i.language
            if lang not in dumb:
                dumb[lang]=[]
            dumb[lang]+=[i]
        for i in dumb:
            temp=sorted(dumb[i],key=lambda x:x.num_user_for_reviews,reverse=True)
            dumb[i]=[temp[:n],temp[-n:]]
            if select!=None:
                if select:
                    dumb[i]=dumb[i][0]
                else:
                    dumb[i]=dumb[i][1]
    return dumb
        
    
            
        


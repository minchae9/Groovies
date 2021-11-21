import json
from pprint import pprint
from tmdb import TMDBHelper
import requests

# movie_json = open('movies/data/popular_movies_1.json', encoding='UTF8')
# movie_json = open('movies/data/top_rated_movies.json', encoding='UTF8')
# movie_json = open('movies/data/now_playing_movies.json', encoding='UTF8')
# movie_json = open('movies/data/popular_movies_2.json', encoding='UTF8')
# movie_dict = json.load(movie_json)
# materials = movie_dict['results']

# 영화 세부 정보 (트레일러 영상 제외)
import json
from pprint import pprint

movie_id_list = [129, 238, 240, 278, 389, 424, 497, 680, 19404, 255709, 283566, 335983, 370172, 372058, 385128, 436969, 438631, 441130, 451048, 459151, 496243, 508943, 512195, 522402, 524434, 532067, 550988, 566525, 568620, 574060, 580489, 585245, 589754, 610253, 618162, 630004, 632632, 634649, 635302, 639721, 644479, 645788, 672582, 675319, 696374, 703771, 714968, 724089, 744275, 761053, 762469, 763164, 768449, 775943, 796499, 843241, 849938, 854442,871964, 885110]
API_KEY = '6756a6f5a02fa599f7f6c9c3afdc2e5d'
tmdb_helper = TMDBHelper(API_KEY)

keys_to_remove = ['backdrop_path', 'belongs_to_collection', 'budget', 'homepage', 'imdb_id', 'original_language',
'popularity', 'production_companies', 'production_countries', 'revenue', 'spoken_languages',
'status', 'video']


idx = 1
details = []
for movie_id in movie_id_list:
    # 세부정보
    request_url = tmdb_helper.get_request_url(method=f'/movie/{movie_id}', language='ko-KR')
    data = requests.get(request_url).json()
    # 트레일러 영상 정보
    trailer_request_url = tmdb_helper.get_request_url(method=f'/movie/{movie_id}/videos', language='ko-KR')
    trailer_data = requests.get(trailer_request_url).json()

    for key in keys_to_remove:
        del data[key]
    if trailer_data['results']:
        data['trailer_key'] = trailer_data['results'][0]['key']
    genres = []
    for genre in data['genres']:
        genres.append(genre['name'])
    data['genres'] = genres
    el = {}
    el['model'] = 'movies.movie'
    el['pk'] = data['id']
    del data['id']
    el['fields'] = data
    details.append(el)
    idx += 1




file_path = "movies/fixtures/movie_details.json"
with open(file_path, 'w') as outfile:
    json.dump(details, outfile, indent=4)
import json

movie_dict={
    "movies": [
        {
            "title":"inception",
            "director":"christor nolen",
            "year":2019
        },
        {
            "title":"premam",
            "director":"alphone puthran",
            "year":2016
        },
        {
            "title":"captain america",
            "director":"jhon",
            "year":2011
        }
    ]
}

json_movie_string=json.dumps(movie_dict)#oru data ye json data yayi covert cheyaan upayokikunu
print(json_movie_string)


with open("movies.json","w") as json_file:
    json.dump(movie_dict,json_file)#oru file lek njamak kittiya json data ye dump  cheyunath


converted_dict=json.loads(json_movie_string)#normal json datail ninum dictionary data ylek maari
print(type(converted_dict))
with open("movies.json","r") as json_files:
   json_from_file=json.load(json_files)
   print(json_from_file)
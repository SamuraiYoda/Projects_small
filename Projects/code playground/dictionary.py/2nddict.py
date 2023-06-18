travel_log = {
    "france" : {"cities_visited" : [" paris", "Lille", "Dijon"], "total_visitation" : 12},
    "germany": {"cities_visited" : ["berlin", "hamburg","stuttgart"], "total_tours" : 4}
}

# in above example the cities visited is a dictionary inside a dictionary
# [] suggests the list, and the "total visitation" represents string
# the above france describes following in dictionary - dict, list, string
# list can contain dictionary in it -
# [ list starts{ 

        #dictionary1
# },
# {
        #dictionary2
# 
# }
# 
# ] liist ends

# print(travel_log)

# nesting dictionary in a list
travel_log1 = [
    {
      "country": "France",
      "cities" : ["paris", "lille","Dijon"],
      "total_vistis": 2
     
    },
    {
        "country": "germany",
        "cities" : ["berlin", "hamburg"],
        "total visits": 12

    },
   
]
print(travel_log1)

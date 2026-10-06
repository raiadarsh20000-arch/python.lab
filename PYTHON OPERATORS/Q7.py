movie_collection = ["Avatar", "Titanic", "Interstellar"]
check_list = "Avatar" in (movie_collection)
print(check_list)

check_list2 = "Matrix" in (movie_collection)
print(check_list2)


movie_collection_1 = ("Avatar", "Titanic", "Interstellar:")
print(type(movie_collection_1))

movie_collection_2 = ["Avatar", "Titanic", "Interstellar:"]
print(type(movie_collection_2))

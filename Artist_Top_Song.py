def top_song():
    artist_name = input("Enter which artist songs you want to listen: ")

    query = """ match(a:tracks)-[x:sungBy]->(b:artists{a_name:\"""" + artist_name + """\"})
    where a.rating >= 3
    return a.t_name
    """
    result = graph.run(query).data()

    songs = []

    for x in result:
        songs.append(x['a.t_name'])
    songs = list(set(songs))
    print(songs)
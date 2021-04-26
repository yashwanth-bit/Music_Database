def for_you():
#list of tracks which user likes
    query = """ match (a:user{username:\"""" + login_User_Name + """\"})
    match(b:tracks)
    match (a)-[:likes]->(b)
    return b.genre
    """

    result = graph.run(query).data()

#variable to store the list of genre
    genre = []

    for x in result:
        genre.append(x["b.genre"])

    genre = list(set(genre))

#variable to store the list of songs
    songs =[]
#lsit of songs which user's friends like of the same genre
    for x in genre:
        gen = x.split(',')
        for g in gen:
            query = """ match (u:user{username:\"""" + login_User_Name + """\"})-[:follows]->(a:user)-[:likes]->(t:tracks)
            where \"""" + g.strip() + """\" in split(replace(t.genre,' ',''),',')
            return t.t_name
            """
            result = graph.run(query).data()
    
            for y in result :
                songs.append(y["t.t_name"])

    songs = list(set(songs))
    print(songs)

#Checking for the 'For You' playlist and creating a relation between playlist and song
    for z in songs:
        query = """match (u:user {username:\"""" + login_User_Name + """\"})-[:has]->(p:playlists{p_name:"For You"}), (s:tracks)
        where s.t_name = \"""" + z + """\"
        merge (s)-[:belongsTo]->(p)
        """
    
        result = graph.run(query).data()    
def create_playlist():
    print("please enter playlist name : ")
    playlist_name = input("")

    query = """match(u:user{username:\"""" + login_User_Name + """\"})
    merge(p:playlists{p_name:\"""" + playlist_name + """\"})
    merge(u)-[:has]->(p)
    """
    graph.run(query)
    print("Please type a song you want to add in your playlist : ")
    song_name = input("")

    query = """match(a:tracks{t_name:\""""+ song_name + """\"})
    return a.t_name
    """
    
    result = graph.run(query).data()

    for song_name in result:
        query = """match(q:playlists{p_name:\"""" + playlist_name + """\"}) 
        match(s:tracks{t_name:\"""" + song_name['a.t_name'] + """\"}) 
        merge(s)-[:belongsTo]->(q)
        """
        graph.run(query)
        print("song added successfully :)")

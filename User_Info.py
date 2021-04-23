def getuserdata():

#connection to neo4j database
    graph = Graph(host='localhost', port=7687, password="1234")

#Asking for recommendation
    print("Do you want to recommend a song to your friend?")
    user = input("")

#list of friends user follows
    if user == "yes":
        query = """
        match(u:user{username:\"""" + login_User_Name + """\"})-[x:follows]->(a:user)
        return a.username
        """
        result = graph.run(query).data()

#variable for storing user's friends data
        user_name = []

        for x in result:
            user_name.append(x["a.username"])
        user_name = list(set(user_name))
        print(user_name)
    
#selecting a friend from the list
        print("Choose a friend you want to recommend a song")
        friend = input("")
    
#list of songs user likes
        if friend in user_name:
            print("Choose a song that you want to recommend")
            query = """
            match(u:user{username:\"""" + login_User_Name + """\"})-[c:likes]->(t:tracks)
            return t.t_name
            """
            result = graph.run(query).data()

#variable to store list of songs
            songs = []
            for y in result:
                songs.append(y["t.t_name"])
            songs = list(set(songs))
            print(songs)

#selecting a song to recommend
            print("select a song")
            song = input("")

            if song in songs:
                query = """
                match(b:user{username: \"""" + friend + """\"}),(s:tracks)
                where s.t_name = \"""" + song + """\"
                merge (b) -[x:recommended {recommendedBy:\"""" + login_User_Name + """\"}]-> (s)
                """
                result = graph.run(query)
                print("Song recommended")
        
        else: 
            print("user not found")

#list of songs user has recommended
    elif user == "no":
        print("Do you want to see which songs you recommended?")
        recommend = input("")

#list of friends of user
        if recommend == "yes":
            print("Select a user")
            query = """
            match(u:user{username:\"""" + login_User_Name + """\"})-[x:follows]->(a:user)
            return a.username
            """
            result = graph.run(query).data()

#variable to store list of user's friends
            u_name = []

            for z in result:
                u_name.append(z["a.username"])
            u_name = list(set(u_name))
            print(u_name)

            user = input("")
#songs recommended by the user
            if user in u_name:
                query = """
                match (u:user{username:\"""" + user + """\"}) -[x:recommended]-> (s:tracks)
                where x.recommendedBy = \"""" + login_User_Name + """\"
                return s.t_name
                """
                result = graph.run(query).data()

#variable to store the songs
                tracks = []

                for x in result:
                    tracks.append(x["s.t_name"])
                tracks = list(set(tracks))
                print(tracks)

#song recommended to which users
        elif recommend == "no":
            print("Do you want to see a particular song recommended to which users")
            users = input("")

#list of tracks user likes
            if users == "yes":
                print("select a song")
                query = """
                match(u:user{username:\"""" + login_User_Name + """\"})-[c:likes]->(t:tracks)
                return t.t_name
                """
                result = graph.run(query).data()
#variable to store tracks
                track = []

                for x in result:
                    track.append(x["t.t_name"])
                track = list(set(track))
                print(track)

                tr = input("")

#track recommended to which users
                if tr in track:
                    query = """
                    match (u:user) -[x:recommended]-> (s:tracks{t_name:\"""" + tr + """\"})
                    where x.recommendedBy = \"""" + login_User_Name + """\"
                    return u.username
                    """
                    result = graph.run(query).data()

#variable to store the list of users
                    user_data = []

                    for y in result:
                        user_data.append(y["u.username"])
                    user_data = list(set(user_data))
                    print("This song is recommended to :", user_data)
        
            elif users == "no":
                print("enjoy the music")
def search_friend():
    print("Please enter the username of the friend :")
    username = input("")

    query = """match(u:user{username:\"""" + username + """\"})
    return u.username
    """
    result = graph.run(query)
    
    for username in result:
        print("user found")
        print("do you want to follow the user?")
        follow = input("")

        if follow == "yes":
            query = """ match(u:user{username:\"""" + username['u.username'] + """\"})
            match(a:user{username:\"""" + login_User_Name + """\"})
            merge (a)-[x:follows]->(u)
            """
            graph.run(query)
            print("user followed :)")
        elif follow == "no":
            print("enjoy the music")

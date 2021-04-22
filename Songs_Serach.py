def search():
    print("Please enter what you want to search")
    s = input("")

    query = """match(a:tracks{t_name:\""""+ s + """\"})
    return a
    """
    result = graph.run(query).data()
    print(result)

    query = """match(a:tracks{t_name:\""""+ s + """\"})-[x:sungBy]->(b:artists)
    return b.a_name
    """
    result2 = graph.run(query).data()
    print(result2)

    query = """match(a:tracks{t_name:\""""+ s + """\"})
    return a.t_name
    """
    result3 = graph.run(query).data()


    
    for s in result3:
        print("Do you want to like this song")
        like = input("")

        if like == "yes":
            query = """ match(u:user{username:\"""" + login_User_Name + """\"})
            match(s:tracks{t_name:\"""" + s['a.t_name'] + """\"})
            merge(u)-[h:likes]->(s)
            """
            graph.run(query)
            print("song liked")
        elif like == "no":
            print("enjoy the music")    
login_User_Name = ""
ur_id = ""
def login_opt():
    db = conn.Music 
    collection_old = db.new_login
    global login_User_Name
    global ur_id  

    login_User_Name = input("login_Enter Your User_Name: ")
    login_Password = input("login_Enter Your Password: ")

    data = collection_old.find_one({"new_UserName" : login_User_Name})
    ur_id = data["_id"]

    user = r.keys(pattern=login_User_Name)
    if not user:
        print("user does'nt exists")
    else:   
        Password = r.get(login_User_Name)
        if Password.decode("utf-8") == login_Password:
            print("login successful")
            print("1.Enter this option if you want to listen the top songs from different artists")
            print("2.Enter this option if you want to recommend a song")
            print("3.Refer to your friend and earn some cash points")
            print("4.Search")
            print("5.Create your own playlist")
            print("6.Search a friend")
            print("7.Check 'For You' Playlist")
            print("8.Total cash earned:")
            opt = input("Enter which option you want to choose:")
            if opt ==  "1":
                top_song()
            elif opt== "2":
                getuserdata()
            elif opt== "3":
                reward_code()
            elif opt== "4":
                search()
            elif opt== "5":
                create_playlist()
            elif opt== "6":
                search_friend()
            elif opt== "7":
                for_you()
            elif opt== "8":
                total_cash()      
            else:
                print("wrong entry")
        else:
            print("wrong credentials")
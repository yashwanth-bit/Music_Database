def total_cash():
    db = conn.Music 
    collection = db.rewards
    pipeline = [{"$match":{"user_name": login_User_Name}},{"$group":{"_id":None , "sum":{"$sum":"$cash_earned"}}},
                {"$project":{"_id":0 ,"sum":1}}
                ]
    docu = collection.aggregate(pipeline)
    for x in docu:
        print (x['sum'])
    print(login_User_Name)
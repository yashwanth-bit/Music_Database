def reward_code():
    random_code = secrets.token_hex(3)
    
    print(random_code)
    db = conn.Music     
    collection = db.rewards
    
    document1 = {
        "user_name":login_User_Name,
        "cash_earned":100,
        "referred_with_code": random_code
        }
    collection.insert_one(document1)
    print("referred sucessfully")
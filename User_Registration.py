from pymongo import MongoClient
from getpass import getpass
from py2neo import Graph
import pandas
import redis
import secrets

print("Enter which option you want to choose: ")
print("New Customer? Please type Yes ")
print("Do you want to login? Login ")

new_user = input("Enter your option here: ")


def new_regis():
    db = conn.Music 
    collection = db.new_login
    global new_User_Name
    global new_Password

    new_User_Name = input("Enter Your User_Name: ")
    new_Password = input("Enter Your Password: ")
    new_First_Name = input("Enter Your First_Name: ")
    new_Last_Name = input("Enter Your Last_Name: ")
    new_Email_id =input("Enter Your Email Address: ")
    new_Phone_Number =input("Enter Your Phone_Number: ")
    new_Date_of_Birth =input("Enter Your Date_of_Birth: ")
    new_Place_of_Birth =input("Enter Your Place_of_Birth: ")

    referral_code = input("Do you have referal code? If yes please type Yes:") 
    
    if  referral_code == "Yes":
        db = conn.Music 
        collection_new = db.new_login
        collection_rew = db.rewards
        refer_id = input("Enter refer code:")
        data = collection_rew.find_one({"referred_with_code" : refer_id})
        print(data)
        referred_by_usr = input("Enter the user name who referred you?")
        if data['user_name'] == referred_by_usr:
            print("VERIFIED!!! ")
            collection_new.insert_many(
    [
        {
            "new_UserName" : new_User_Name,
            "new_Password" : new_Password,
            "new_First_Name" : new_First_Name, 
            "new_Last_Name" : new_Last_Name,
            "new_Email_id" : new_Email_id,
            "new_Phone_Number" : new_Phone_Number,
            "new_Date_of_Birth" : new_Date_of_Birth,
            "new_Place_of_Birth" : new_Place_of_Birth,  
            },
            ]
            )
            db = conn.Music     
            collection = db.rewards
            document1 = {
            "user_name":new_User_Name,
            "cash_earned":50,
            "referred_by_code": refer_id
        }
            collection.insert_one(document1)
            print("VERIFIED!!! and also earned cashpoints ")
           
        
        else:
            print("wrong user name")
    
    else:

        db.new_login.insert_many(
        [
        {
            "new_UserName" : new_User_Name,
            "new_Password" : new_Password,
            "new_First_Name" : new_First_Name, 
            "new_Last_Name" : new_Last_Name,
            "new_Email_id" : new_Email_id,
            "new_Phone_Number" : new_Phone_Number,
            "new_Date_of_Birth" : new_Date_of_Birth,
            "new_Place_of_Birth" : new_Place_of_Birth
            },
            ]
            )
        print("You have not earned cash points but your account has been created")
    
    r.set(new_User_Name, new_Password)
    
    query = """ create(u:user{username:\"""" + new_User_Name + """\"})
    """
    graph.run(query)

    query = """ match(u:user{username:\"""" + new_User_Name + """\"})
    create(p:playlists{p_name:"For You"})
    merge(u)-[x:has]->(p)
    """
    graph.run(query)
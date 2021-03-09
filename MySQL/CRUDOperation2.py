import mysql.connector as connector


class DBHelper:
   def __init__(self):
      self.con = connector.connect(host="localhost",
                                   user="root",
                                   password="mundhe012@",
                                   database="dbpython")
      query = "create table if not exists user(userId int primary key,userName varchar(200),phone varchar(12))"
      cur = self.con.cursor()
      cur.execute(query)
      print("created suceessfully")

   #insert
   def insert_user(self,userid,username,phone):
       query = "insert into user(userId,userName,phone)values({},'{}','{}')".format(userid,username,phone)
       print(query)
       cur = self.con.cursor()
       cur.execute(query)
       self.con.commit()
       print("user saved to db")


   #Fetch all
   def fetch_all(self):
       query = "select * from user"
       cur = self.con.cursor()
       cur.execute(query)
       for row in cur:
        print("userId :",row[0])
        print("userName :", row[1])
        print("phone :", row[2])
        print()


   #Delete User
   def delete_user(self,userId):
       query= "delete from user where userId={}".format(userId)
       print(query)
       c = self.con.cursor()
       c.execute(query)
       self.con.commit()
       print("deleted successfully")


   #update
   def update_user(self,userId,newName,newPhone):
       query = "update user set userName='{}',phone ='{}'where userId={}".format(newName, newPhone, userId)
       print(query)
       cur = self.con.cursor()
       cur.execute(query)
       self.con.commit()
       print("updated Successfully")

def main():
    db = DBHelper()
    while True:
        print("**********WELCOME*******")
        print("Press 1 to insert new user")
        print("Press 2 to display all user")
        print("Press 3 to delete user")
        print("Press 4 to update user")
        print("Press 5 to exit")
        try:
            choice = int(input("Enter Choice"))
            if (choice == 1):
                #insert New user
              uid =int(input("Enter user Id"))
              username =input("Enter username")
              userphone =input("Enter userphone")
              db.insert_user(uid,username,userphone)
              pass
            elif choice == 2:
                #display user
                db.fetch_all()
                pass
            elif choice == 3:
                #delete user
               userid = int (input("enter user id ehich you want to delete"))
               db.delete_user(userid)
            elif choice == 4:
                #update User
                uid = int(input("enter id of user :"))
                username = input("enter user name :")
                userphone = input("enter user phone :")
                db.update_user(uid,username,userphone)
            elif choice == 5:
                break
            else:
                print("invalid input ! try again")
        except Exception as e:
            print(e)
            print("invalid deatails ! try again")

if __name__ == '__main__':
    main()



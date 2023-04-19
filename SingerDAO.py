from object.music import *
from connect import *
class SingerDao:
    connect = mydb.cursor()
    def __init__(self):
        pass
    def SelectList(self):
        self.connect.execute("select * from Singer")
        myresult = self.connect.fetchall()
        list = []
        for x in myresult:
            value =  Singer(x[0],x[1])
            list.append(value)
        mydb.commit()
        return list
    def Update(self,value):
        s = (value.name,value.id)
        self.connect.execute("update Singer name = %s where id = %s",s)
        mydb.commit()
    def Delete(self,id):
        self.connect.execute("delete from Singer where id = %s",id)
        mydb.commit()
    def searchId(self,id):
        s = [id]
        self.connect.execute("select * from Singer where id = %s",s)
        myresult = self.connect.fetchall()
        name  = myresult[0][1]
        mydb.commit()
        return name
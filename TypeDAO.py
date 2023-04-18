from object.music import *
from connect import *
class TypeDao:
    connect = mydb.cursor()
    def __init__(self):
        pass
    def SelectListType(self):
        self.connect.execute("select * from TypeSong")
        myresult = self.connect.fetchall()
        list = []
        for x in myresult:
            value =  Type(x[0],x[1])
            list.append(value)
        mydb.commit()
        return list
    def Update(self,type):
        s = (type.name,type.id)
        self.connect.execute("update TypeSong name = %s where id = %s",s)
        mydb.commit()
    def Delete(self,id):
        self.connect.execute("delete from TypeSong where id = %s",id)
        mydb.commit()
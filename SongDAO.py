from object.music import *
from connect import *
class SongDAO:
    connect = mydb.cursor()
    def __init__(self):
        pass
    def SelectList(self):
        self.connect.execute("select * from Song")
        myresult = self.connect.fetchall()
        list = []
        for x in myresult:
            value =  Music(x[0],x[1],x[2],x[3],x[4],x[5])
            list.append(value)
        mydb.commit()
        return list
    def Update(self,value):
        s = (value.name,value.link,value.image,value.idType,value.idSinger,value.id)
        self.connect.execute("update Song name = %s, link = %s, image = %s, idType = %s, idSinger = %s where id = %s",s)
        mydb.commit()
    def Delete(self,id):
        self.connect.execute("delete from Song where id = %s",id)
        mydb.commit()
    def Insert(self,value):
        sql = "INSERT INTO Song (id,name,link,image,idType,idSinger) VALUES (%s, %s,%s,%s,%s,%s)"
        s = (value.id,value.name,value.link,value.image,value.idType,value.idSinger)
        self.connect.execute(sql,s)
        mydb.commit()
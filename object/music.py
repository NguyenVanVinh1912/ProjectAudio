class Music:
    def __init__(self,id=-1, name="", link="", image="", idType=-1, idSinger=-1):
        self.id = id
        self.name = name
        self.link = link
        self.image = image
        self.idType = idType
        self.idSinger = idSinger

class Type:
    def __init__(self, id=-1, name=""):
  
        self.name = name
        self.id = id
class Singer:
    def __init__(self, id=-1, name=""):
  
        self.name = name
        self.id = id
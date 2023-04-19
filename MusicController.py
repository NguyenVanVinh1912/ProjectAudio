from object.music import *
from TypeDAO import *
from SingerDAO import *
from SongDAO import *
class MusicController:
    typeDao = TypeDao()
    singerDao = SingerDao()
    songDao = SongDao()
    def __init__(self) -> None:
        pass
    def searchTypeId(self,id):
        return self.typeDao.searchId(id)
    def searchSingerId(self,id):
        return self.singerDao.searchId(id)
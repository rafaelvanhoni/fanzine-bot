class Artist:
    
    def __init__(self, 
                 id: int, 
                 type: str, 
                 user_data: dict, 
                 master_id: str | None, 
                 master_url: str | None, 
                 uri: str, 
                 title: str, 
                 thumb: str, 
                 cover_image: str, 
                 resource_url: str ):
        self.__id = id
        self.__type = type
        self.__user_data = user_data
        self.__master_id = master_id
        self.__master_url = master_url
        self.__uri = uri
        self.__title = title
        self.__thumb = thumb
        self.__cover_image = cover_image
        self.__resource_url = resource_url

    def __str__(self):
        return f"{self.__title}, id: {self.__id}"
    
    def __repr__(self):
        return f"Artist(id='{self.__id}', title='{self.__title}')"

    @staticmethod
    def from_dict(data: dict) -> "Artist":
        return Artist(id=data["id"],
                      type=data["type"],
                      user_data=data["user_data"],
                      master_id=data["master_id"],
                      master_url=data["master_url"],
                      uri=data["uri"],
                      title=data["title"],
                      thumb=data["thumb"],
                      cover_image=data["cover_image"],
                      resource_url=data["resource_url"])
    


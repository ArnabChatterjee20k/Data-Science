import requests as req , json

class Extractor:
    @classmethod
    def __extract(cls,state,requirement):
        with open("config.json") as f:
            json_data = json.load(f)
        url = json_data.get("State-district-wise")
        res = req.get(url).json().get(state).get(requirement)
        keys = list(res.keys())
        return (keys , res)
    
    def __init__(self , state) :
        self.state = state
        self.requirement = "districtData"
        self.__getkey = "active"
        self.__keys , self.__data = (self.__extract(state = self.state  , requirement= self.requirement))
    
    def get_active_cases(self):
        data = dict()
        for place in self.__keys:
            data[place] = self.__data.get(place).get(self.__getkey)
        return data
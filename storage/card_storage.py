import json
class CardStorage:
    @staticmethod
    def save(cards, filename):
        data=[]
        for card in cards:
            data.append(card.__dict__)
        with open(filename,'w') as f:
            json.dump(data,f,indent=4,default=str)

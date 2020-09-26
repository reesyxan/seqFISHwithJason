from os import path
import requests
from enum import Enum

class Model(Enum):
    ORGANISM = 'Organism'
    GENE = 'Gene'
    Chromosome = 'Chromosome'
    STRUCTURE = 'Structure'

class BrainMapAPI(object):
    __url_base = 'http://api.brain-map.org/api/v2/data/'
    __url_prototype = path.join(__url_base, '{model}', '{model_id}.json')
    __status_url = 'http://api.brain-map.org/api/v2/status/query.json'

    @classmethod
    def status(cls):
        ''' Get Brain-Map status '''
        r = requests.get(cls.__status_url)
        return r.json()

    @classmethod 
    def gene(cls, id):
        url = cls.__url_prototype.format(model=Model.GENE.value, model_id=id)
        r = requests.get(url)
        print(url)
        return r.json()
    



print(BrainMapAPI.gene(2))

from os import path
import requests
from enum import Enum

class Model(Enum):
    
    ORGANISM = 'Organism'
    GENE = 'Gene'
    Chromosome = 'Chromosome'
    STRUCTURE = 'Structure'

class BrainMapAPI(object):
    '''
    http://help.brain-map.org/display/api/RMA+Path+Syntax
    '''
    __url_base = 'http://api.brain-map.org/api/v2/data/'
    __url_prototype = path.join(__url_base, '{model}', '{model_id}.json')
    __query_url = path.join(__url_base, 'query.json')
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

    @classmethod 
    def experiments_by_gene(cls, gene):
        rma_path = ''

        rma_path  = 'model::SectionDataSet,'
        rma_path += "rma::criteria,[failed$eq'false'],"
        rma_path += "products[abbreviation$eq'Mouse'],"
        rma_path += "plane_of_section[name$eq'sagittal'],"
        rma_path += "genes[acronym$eq'{}']".format(gene)

        url = cls.__query_url + '?criteria='
        url += rma_path
        r = requests.get(url)
        print(r.json())

        


print(BrainMapAPI.gene(2))
BrainMapAPI.experiments_by_gene('Star')

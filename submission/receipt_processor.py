import uuid
import math
from openapi_spec_validator import validate_spec
from openapi_spec_validator.readers import read_from_filename

spec_dict, base_uri = read_from_filename('../api.yml')

validate_spec(spec_dict)
database = {}

def process_receipt(prototype):
    receipt = prototype.json
    id = str(uuid.uuid4())

    receipt[id] = {'id': id, 'points': 0.0}
    receipt[id]['points'] = calcuate_total_points(receipt)
    

    database['entry'] = receipt
    return ({'id':id})

def get_points(id):
    return (database[id]['points'])

def calcuate_total_points(prototype):
    points = 0.0 
    points += character_points(prototype)
    points += round_dollar_amount_points(prototype)
    points += multiple_points(prototype)
    points += item_points(prototype)
    points += description_points(prototype)
    points += day_points(prototype)
    points += time_points(prototype)
    return points

def character_points(prototype):
    points = 0
    for c in prototype['retailer']:
        if c.isalpha():
            points += 1
    
    return points 
    

def round_dollar_amount_points(prototype):
    total = float(prototype['total'])
    if total.is_integer():
        return 50 
    else:
        return 0
    
def multiple_points(prototype):
    total = float(prototype['total'])
    if total % .25 == 0: 
        return 25 
    else:
        return 0
    
def item_points(prototype):
    num_items = math.floor(len(prototype['items'])/2)
    return (5 * num_items)
    
def description_points(prototype): 
    total = 0
    for item in prototype['items']:

        description = item['shortDescription'].lstrip().rstrip()
        price = float(item['price'])
        if len(description) % 3 == 0:
            total += math.ceil(price* .2)
    
    return total

def day_points(prototype):
    date = prototype['purchaseDate'].split('-')
    day = int(date[2])

    if day % 2 != 0:
        return 6 
    else : 
        return 0
    
def time_points(prototype): 

    date = prototype['purchaseTime'].split(':')
    hour = int(date[0])
    minute = int(date[1])


    if hour == 14 and minute < 1:
        return 0
    if hour >= 14 and hour < 16:
       return 10 
    
    return 0

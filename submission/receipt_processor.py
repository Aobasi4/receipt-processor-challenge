import uuid
import json
import math
import datetime
from openapi_spec_validator import validate_spec
from openapi_spec_validator.readers import read_from_filename

spec_dict, base_uri = read_from_filename('../api.yml') #/Users/amaraobasi/receipt-processor-challenge/api.yml

validate_spec(spec_dict)
database = {}

# Takes in a JSON receipt (see example in the example directory) and returns a JSON object with an ID generated by your code.
def process_receipt(prototype):
    receipt = prototype.json
    receipt['points'] = calcuate_total_points(receipt)
    phony = receipt['points']

    id = str(uuid.uuid4())

    database['X'] = receipt

    return {'id':id, 'points2': phony}

def get_points(id):
    return { "points": database[id]['points'] }

def calcuate_total_points(prototype):
    points = 0.0 
    points += character_points(prototype)
    points += round_dollar_amount_points(prototype)
    points += multiple_points(prototype)
    points += item_points(prototype)
    points += description_points(prototype)
    #points += day_points(prototype)
    #points += time_points(prototype)
    return points

def character_points(prototype):
    points = sum(c.isalpha() for c in prototype['retailer'])
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
    return (5 * math.floor(len(prototype['items'])))
    
def description_points(prototype): 
    total = 0
    for item in prototype['items']:

        description = item['shortDescription']
        price = float(item['price'])
        print(price)

        if len(description) % 3 == 0:
            total += math.ceil(price* .2)
    
    return total

def day_points(prototype):
    date = datetime(prototype['purchaseDate'])
    day = int(date.strftime("%d"))

    if day % 2 != 0:
        return 6 
    else : 
        return 0
    
def time_points(prototype): 
    #retrun 10 points if the time of purchase is after 2 and before 4

    date = datetime(prototype['purchaseDate'])
    hour = int(date.strftime("%H"))
    minute = int(date.strftime("%M"))

    if hour == 2 and minute < 1:
        return 0
    if hour > 2 and hour < 4:
       return 10 
    
    return 0

def validateJSON(jsonData):
    try:
        json.loads(jsonData)
    except ValueError as err:
        return False
    return True
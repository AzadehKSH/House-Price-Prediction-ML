
import json
import pickle
import numpy as np
__states = None
__data_columns = None
__model = None

def get_estimated_price(State,Living_space,Rooms,Bathrooms):
    try:
        loc_index = __data_columns.index(State.lower())
    except:
        loc_index = -1
    x = np.zeros(len(__data_columns))
    x[0] = Living_space
    x[1] = Rooms
    x[2] = Bathrooms
    if loc_index >= 0:
        x[loc_index] = 1
    return round(__model.predict([x])[0])


def get_state_names():
    return __states

def load_saved_artifacts():
    print("Loading saved artifacts...start")
    global __data_columns
    global __states
    with open("./artifacts/columns.json",'r') as f:
        __data_columns = json.load(f)['data_columns']
        __states = __data_columns[10:]
    global __model
    with open("./artifacts/Mecklenburg-Vorpommern_home_prices_model.pickle",'rb') as f:
        __model = pickle.load(f)
    print("Loading saved artifacts done")

if __name__ == '__main__':
    load_saved_artifacts()
    print(get_state_names())
    print(get_estimated_price('bayern',1000,2,3))
    print(get_estimated_price('mecklenburg-vorpommern', 1000, 2, 3))
    print(get_estimated_price('niedersachsen', 1000, 2, 3))
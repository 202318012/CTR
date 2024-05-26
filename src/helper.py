import pickle

def make_pickle(file, pkl):

    try:
        with open(file, 'wb') as f:
            pickle.dump(pkl, f)

    except Exception as e:
        print('\nError in pickle helper function \nExcetion: ', e)

def get_pickle(file):

    try:
        with open(file, 'rb') as f:
            return pickle.load(f)

    except Exception as e:
        print('\nError in pickle helper function \nExcetion: ', e)
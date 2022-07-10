import pickle

def load_model(path='lin_reg.bin'):
    with open(path, 'rb') as f_in:
        (dv, model) = pickle.load(f_in)
        return (dv, model)

def prepare_features(ride):
    features = {}
    features['PU_DO'] = '%s_%s' % (ride['PULocationID'], ride['DOLocationID'])
    features['trip_distance'] = ride['trip_distance']
    return features


def predict(features, dv, model):
    X = dv.transform(features)
    preds = model.predict(X)
    return float(preds[0])
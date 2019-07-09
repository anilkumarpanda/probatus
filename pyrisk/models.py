import pickle
import os

def lending_club_model(file_name = 'sample_credit_model.pkl'):
    """Sample Random Forest model trained on the lending club loan data.

    Model Hyper Parameberts:
        bootstrap=True, class_weight=None, criterion='gini',
        max_depth=6, max_features='auto', max_leaf_nodes=None,
        min_impurity_decrease=0.0, min_impurity_split=None,
        min_samples_leaf=1, min_samples_split=2,
        min_weight_fraction_leaf=0.0, n_estimators=100, n_jobs=None,
        oob_score=False, random_state=0, verbose=0, warm_start=False

    Args:
        file_name (str) : name of the file which will be loaded from the pretrained model

    Returns:
        credit_clf (sklearn.ensemple.RandomForestClassifier): Pretrained model

    """

    credit_clf = pickle.load(open(os.path.join('data',file_name), 'rb'))

    return credit_clf
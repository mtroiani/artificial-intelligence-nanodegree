import warnings
from asl_data import SinglesData


def recognize(models: dict, test_set: SinglesData):
    """ Recognize test word sequences from word models set

   :param models: dict of trained models
       {'SOMEWORD': GaussianHMM model object, 'SOMEOTHERWORD': GaussianHMM model object, ...}
   :param test_set: SinglesData object
   :return: (list, list)  as probabilities, guesses
       both lists are ordered by the test set word_id
       probabilities is a list of dictionaries where each key a word and value is Log Liklihood
           [{SOMEWORD': LogLvalue, 'SOMEOTHERWORD' LogLvalue, ... },
            {SOMEWORD': LogLvalue, 'SOMEOTHERWORD' LogLvalue, ... },
            ]
       guesses is a list of the best guess words ordered by the test set word_id
           ['WORDGUESS0', 'WORDGUESS1', 'WORDGUESS2',...]
   """
    warnings.filterwarnings("ignore", category=DeprecationWarning)
    probabilities = [] #list of dictionaries
    guesses = [] # list of the best guess words

    words = test_set.get_all_Xlengths()

    for word in words:
        probability = {}
        best_guess = None
        best_score = 0
        for key in models:
            try: #Some models may not have enough data to train a model
                score = models[key].score(words[word][0])
                probability[key] = score
            except: #if not enough data for model, assign 0 - as in https://discussions.udacity.com/t/failure-in-recognizer-unit-tests/240082
                score = 0
                probability[key] = score

            if not best_guess or score > best_score:
                best_guess = key
                best_score = score
        probabilities.append(probability)
        guesses.append(best_guess)
    return probabilities, guesses

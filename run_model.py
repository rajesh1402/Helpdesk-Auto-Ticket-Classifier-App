import pickle
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.multiclass import OneVsRestClassifier

#tfidf_vect = TfidfVectorizer(ngram_range=(1,2),max_df=0.5,min_df=2)
#oneVsRestSVC = OneVsRestClassifier(LinearSVC(class_weight='balanced'))

def clean_text(text):
    text = text.lower()
    text = re.sub('\W', ' ', text)
    text = re.sub('\s+', ' ', text)
    text = text.strip(' ')
    return text

def predict(input_text):
    input_text = [clean_text(input_text)]

    with open(f'model/finalized_model.sav', 'rb') as f:
        model = pickle.load(f)

    with open(f'model/tfidf_model.sav', 'rb') as f:
        vectorizer = pickle.load(f)

    mapping = {0: 'ACCESS',
    1: 'HARDWARE',
    2: 'SOFTWARE',
    3: 'WINDOWS',
    4: 'EMAIL',
    5: 'ANTIVIRUS'
  }



    text_feats = vectorizer.transform(input_text)
    prediction = model.predict(text_feats)[0]

    category = ""
    for key, value in mapping.items():
        if key == prediction:
            category = value
    return category
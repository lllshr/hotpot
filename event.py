import jieba
from sklearn.externals import joblib


class Event(object):
    def __init__(self):
        self.class_dic = {}
        with open('event_config.txt', 'r', encoding='utf-8-sig') as config:
            for line in config.readlines():
                if len(line.split(':')) == 2:
                    self.class_dic.setdefault(int(line.split(':')[0]), line.split(':')[1].strip())
        with open('swords.txt', 'r', encoding='utf-8-sig') as s:
            self.swords = [line.strip() for line in s.readlines() if len(line) > 0]

    def loadmodel(self, vec='model_save/vec.m', trans='model_save/tfidf.m', model='model_save/rf_gini50.0.m'):
        self.vectorizer = joblib.load(vec)
        self.transformer = joblib.load(trans)
        self.clf = joblib.load(model)

    def classify(self, content):
        tfidf = self.transformer.transform(self.vectorizer.transform([' '.join([word for word in jieba.cut(content) if word not in self.swords])]))
        weight = tfidf.toarray()
        result = self.clf.predict(weight)
        return self.class_dic.get(result[0])
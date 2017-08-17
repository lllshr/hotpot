import jieba


class SegWord(object):
    def __init__(self):
        with open(r'newwords.txt', 'r', encoding='utf-8-sig') as file:
            self.dic = [line.strip() for line in file.readlines()]
        jieba.load_userdict(r'newwords.txt')
        pass

    def get_words(self, corpus):
        """
        获取热词
        :param corpus: 语料
        :return:
        """
        return [word for word in list(jieba.cut(corpus)) if word in self.dic and word != '客户' and word != '坐席']

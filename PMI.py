# coding=utf-8
import math
class PMI:
    def __init__(self, document):
        self.document = document
        self.pmi = {}
        self.miniprobability = float(1.0) / document.__len__()
        self.minitogether = float(0)/ document.__len__()
        self.set_word = self.getset_word()

    def calcularprobability(self, document, wordlist):

        """
        :param document:
        :param wordlist:
        :function : 计算单词的document frequency
        :return: document frequency
        """

        total = document.__len__()
        number = 0
        for doc in document:
            if set(wordlist).issubset(doc):
                number += 1
        percent = float(number)/total
        return percent

    def togetherprobablity(self, document, wordlist1, wordlist2):

        """
        :param document:
        :param wordlist1:
        :param wordlist2:
        :function: 计算单词的共现概率
        :return:共现概率
        """

        joinwordlist = wordlist1 + wordlist2
        percent = self.calcularprobability(document, joinwordlist)
        return percent

    def getset_word(self):

        """
        :function: 得到document中的词语词典
        :return: 词语词典
        """
        list_word = []
        for doc in self.document:
            list_word = list_word + list(doc)
        set_word = []
        for w in list_word:
            if set_word.count(w) == 0:
                set_word.append(w)
        return set_word

    def get_dict_frq_word(self):

        """
        :function: 对词典进行剪枝,剪去出现频率较少的单词
        :return: 剪枝后的词典
        """
        dict_frq_word = {}
        for i in range(0, self.set_word.__len__(), 1):
            list_word=[]
            list_word.append(self.set_word[i])
            probability = self.calcularprobability(self.document, list_word)
            if probability > self.miniprobability:
                dict_frq_word[self.set_word[i]] = probability
        return dict_frq_word

    def calculate_nmi(self, joinpercent, wordpercent1, wordpercent2):
        """
        function: 计算词语共现的nmi值
        :param joinpercent:
        :param wordpercent1:
        :param wordpercent2:
        :return:nmi
        """
        per =  (joinpercent) / (wordpercent1 * wordpercent2)
        log_per = math.log(per, 2)
        return log_per

    def calculate_sopmi(self, p, n):
        return p - n

    def get_pmi(self):
        """
        function:返回符合阈值的pmi列表
        :return:pmi列表
        """
    #    pp = open('/home/mac/Downloads/posneg.txt').read()
        positive = ('好吃', '便宜', '喜欢', '很快', '肉多')
        negative = ('送得慢', '难吃', '糟糕', '太贵', '差劲','差评')
        dict_pmi = {}
        dict_frq_word = self.get_dict_frq_word()
        i = 1
      #  print (dict_frq_word)
        print('[STPE3] CALCULATE PMI OF EVERY WORD')
        for word1 in dict_frq_word:
            positive_pmi = 0
            negative_pmi = 0
            wordpercent1 = dict_frq_word[word1]
            for word2 in positive: 
                # dict_frq_word:
                if word1 == word2:
                    continue
                wordpercent2 = dict_frq_word[word2]
                list_together=[]
                list_together.append(word1)
                list_together.append(word2)
                together_probability_pos = self.calcularprobability(self.document, list_together)
                if together_probability_pos > self.minitogether:
                    positive_pmi = positive_pmi + self.calculate_nmi(together_probability_pos, wordpercent1, wordpercent2)
                
            for word3 in negative:
                if word1 == word3:
                    continue
                wordpercent3 = dict_frq_word[word3]
                list_together = []
                list_together.append(word1)
                list_together.append(word3)
                together_probability_neg = self.calcularprobability(self.document, list_together)
                if together_probability_neg > self.minitogether:
                    negative_pmi = negative_pmi + self.calculate_nmi(together_probability_neg, wordpercent1, wordpercent3)
          #  print('done')
          #  if flag_pos != 0 and flag_neg != 0:
              #  if together_probability_pos > self.minitogether and together_probability_neg > self.minitogether:
            string = word1 + ' , '+ ' PMI:'
            dict_pmi[string] = self.calculate_sopmi(positive_pmi, negative_pmi)
            print('store the SO-PMI: done! WORD', i)
            i = i + 1
            if i > 100:
                break
        print('all new words done, return the main')
        return dict_pmi
                #    dict_pmi[string] = self.calculate_nmi(together_probability, wordpercent1, wordpercent2)
        """
        for word1 in dict_frq_word :
            wordpercent1 = dict_frq_word[word1]
            for word2 in negative:
                if word1 == word2:
                    continue
                wordpercent2 = dict_frq_word[word2]
                list_together = []
                list_together.append(word1)
                list_together.append(word2)
                together_probability = self.calcularprobability(self.document, list_together)
                if together_probability > self.minitogether:
                    string = word1 + ' , ' + word2 + ', negative, PMI:'
                    dict_pmi[string] = self.calculate_nmi(together_probability, wordpercent1, wordpercent2)
        return dict_pmi
    
"""

from utils.load_data_utils import *
import re
#import neuspell
#from neuspell import available_checkers, CnnlstmChecker
from keybert import KeyBERT


class KeywordExtractor():
    def __init__(self, candi_keywords=None, idf_dict=None):
        self.candi_keywords = candi_keywords
        self.idf_dict = idf_dict
        self.kw_model = KeyBERT()
        
        # self.checker = CnnlstmChecker()
        # self.checker.from_pretrained()

    @staticmethod
    def is_keyword_tag(tag):
        return tag.startswith('VB') or tag.startswith('NN') or tag.startswith('JJ')

    @staticmethod
    def cal_tag_score(tag):
        if tag.startswith('VB'):
            return 1.
        if tag.startswith('NN'):
            return 2.
        if tag.startswith('JJ'):
            return 0.5
        return 0.

    def is_candi_keyword(self, keyword):
        if keyword in self.candi_keywords:
            return True
        return False

    #modified 
    def tokenize_weights(self,test_string):
        utterances = re.split('[?,.]',test_string)
        utterances= [utterance.strip() for utterance in utterances if len(utterance)>1]
        token_to_index_map={}
        for index, utterance in enumerate(utterances):
            tokens=utterance.split()
            for token in tokens:
                if len(token) > 1:
                    token_to_index_map[token] = (index +1)/len(utterances)
        return token_to_index_map

    def idf_extract(self, string, is_context,con_kw=None):
        # string = self.checker.correct(string)
        # string = string.lower()
        # token_to_weights_map = None
        # if is_context:
        #     token_to_weights_map = self.tokenize_weights(string)
        
        #Modified Code  (K BERT)
        keyword_probs = self.kw_model.extract_keywords(string)
        keywords = [keyword[0] for keyword in keyword_probs]
        return keywords
        
        #Modified Code (Word Decay)
        # tokens = simp_tokenize(string)
        # seq_len = len(tokens)
        # tokens = pos_tag(tokens)
        # source = kw_tokenize(string)
        # candi = []
        # result = []


        # for i, (word, tag) in enumerate(tokens):
        #     score = self.cal_tag_score(tag)
        #     if not self.is_candi_keyword(source[i]) or score == 0.:
        #         continue
        #     if con_kw is not None and source[i] in con_kw:
        #         continue
        #     score *= source.count(source[i])
        #     score *= 1 / seq_len
        #     score *= self.idf_dict[source[i]] if source[i] in self.idf_dict else 1
        #     #print(word, score)
        #     #print("TEST BEFORE ",i,word,tag,score)
        #     # if token_to_weights_map:
        #     #     if source[i] in token_to_weights_map:
        #     #         score *= token_to_weights_map[source[i]]
        #     #print("TEST AFTER",i,word,tag,score)
        #     candi.append((source[i], score))
        #     if score > 0.015:
        #         result.append(source[i])
        # return result
        # tokens = simp_tokenize(string)
        # seq_len = len(tokens)
        # tokens = pos_tag(tokens)
        # source = kw_tokenize(string)
        # candi = []
        # result = []
        # for i, (word, tag) in enumerate(tokens):
        #     score = self.cal_tag_score(tag)
        #     if not self.is_candi_keyword(source[i]) or score == 0.:
        #         continue
        #     if con_kw is not None and source[i] in con_kw:
        #         continue
        #     score *= source.count(source[i])
        #     score *= 1 / seq_len
        #     score *= self.idf_dict[source[i]]
        #     candi.append((source[i], score))
        #     if score > 0.15:
        #         result.append(source[i])
        # return result

    def perserve_non_lemmatized_tokens_idf_extract(self, string, con_kw=None):
        tokens = simp_tokenize(string)
        seq_len = len(tokens)
        tokens = pos_tag(tokens)
        source = kw_tokenize(string)
        candi = []
        lemmatized_keywords = []
        non_lemmatized_keywords = []
        for i, (word, tag) in enumerate(tokens):
            score = self.cal_tag_score(tag)
            if not self.is_candi_keyword(source[i]) or score == 0.:
                continue
            if con_kw is not None and source[i] in con_kw:
                continue
            score *= source.count(source[i])
            score *= 1 / seq_len
            score *= self.idf_dict[source[i]]
            candi.append((source[i], score))
            if score > 0.15:
                lemmatized_keywords.append(source[i])
                non_lemmatized_keywords.append(word)
        return lemmatized_keywords, non_lemmatized_keywords

    def extract(self, string):
        tokens = simp_tokenize(string)
        tokens = pos_tag(tokens)
        source = kw_tokenize(string)
        kwpos_alters = []
        for i, (word, tag) in enumerate(tokens):
            if source[i] and self.is_keyword_tag(tag):
                kwpos_alters.append(i)
        kwpos, keywords = [], []
        for id in kwpos_alters:
            if self.is_candi_keyword(source[id]):
                keywords.append(source[id])
        return list(set(keywords))

    def candi_extract(self, string):
        tokens = simp_tokenize(string)
        tokens = pos_tag(tokens)
        source = kw_tokenize(string)
        keywords = []
        for i, (_, tag) in enumerate(tokens):
            if source[i] and self.is_keyword_tag(tag):
                keywords.append(source[i])
        return list(set(keywords))

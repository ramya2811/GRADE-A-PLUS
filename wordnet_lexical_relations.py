from nltk.corpus import wordnet as wn

#for ss in wn.synsets('green'):
#     #print(dir(ss))
#     for hyper in ss.hypernyms():
#         print(ss,"hypernym", hyper)

hit = wn.synset('hit.v.01')
slap = wn.synset('slap.v.01')

print(wn.path_similarity(hit, slap))
#print(wn.synsets('color').lowest_common_hypernyms(wn.synsets('green')))
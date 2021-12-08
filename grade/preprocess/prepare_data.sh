# load raw dailydialog

python load_data.py

#export CLASSPATH=/Users/shubhamphal/Documents/'CMU coursework 1st sem'/'Advanced Natural Language Processing'/DialogEval/DialEvalMetrics/grade/preprocess/lucene-core-7.4.0.jar:/Users/shubhamphal/Documents/'CMU coursework 1st sem'/'Advanced Natural Language Processing'/DialogEval/DialEvalMetrics/grade/preprocess/lucene-queryparser-8.4.0

# lexical negative sampling
javac IndexCreate.java
java IndexCreate
javac IndexSearch.java
java IndexSearch

# generate standard training data
python prepare_data.py

# generate pkl
python prepare_pkl.py
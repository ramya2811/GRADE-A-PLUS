from pathlib import Path
import json
import numpy as np

def load_grade_data(base_dir, dataset, model_name, grade_score_path):
    base_dir = Path(f'{base_dir}/{dataset}/{model_name}')

    contexts = []
    with (base_dir / 'human_ctx.txt').open() as f:
        for line in f.readlines():
            context = line.strip().split('|||')
            contexts.append(context)

    responses = []
    with (base_dir / 'human_hyp.txt').open() as f:
        for line in f.readlines():
            response = line.strip()
            responses.append(response)

    references = []
    with (base_dir / 'human_ref.txt').open() as f:
        for line in f.readlines():
            reference = line.strip()
            references.append(reference)

    scores = []
    with (base_dir / 'human_score.txt').open() as f:
        for line in f.readlines():
            score = line.strip()
            scores.append(float(score))

    with open(grade_score_path) as f:
        grade_scores = json.load(f)['GRADE_K2_N10_N10_eval_best_71']


    print(grade_scores)
    scores = np.array(scores)
    grade_scores = np.array(grade_scores)

    scores = scores/5
    #scores = (scores - scores.min())/(scores.max() - scores.min())
    
    # if len(grade_scores) > 1:
    #     grade_scores = (grade_scores - grade_scores.min()) / (grade_scores.max() - grade_scores.min())


    #print("TEST",len(grade_scores))
    #print("TEST")

    for i in range(len(grade_scores)):
        # if abs(grade_scores[i] - scores[i]) < 0.5:
        #     continue
        print("i: ", i+1)
        print("Context: ", contexts[i])
        print("Response: ", responses[i])
        print("Reference: ", references[i])
        print("Human Score:", scores[i])
        print("Grade Score", grade_scores[i])
        print("")

if __name__ == '__main__':
    base_dir = '../data/grade_data'
    dataset = 'convai2'
    model_name = 'bert_ranker'
    grade_score_path = './evaluation/infer_result/eval_convai2_grade_bert_ranker/model/non_reduced_results.json'
    load_grade_data(base_dir, dataset, model_name, grade_score_path)
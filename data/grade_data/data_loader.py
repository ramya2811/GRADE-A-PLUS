from pathlib import Path
import neuspell
from neuspell import available_checkers, CnnlstmChecker




def load_grade_data(base_dir, dataset, model_name):
    checker = CnnlstmChecker()
    checker.from_pretrained()
    # preprocessed_dataset= []
    # for dialog in dataset:
    #     preprocessed_utterances = []
    #     for utterance in dialog:
    #         preprocessed_utterances.append(checker.correct(utterance).lower())
    #     preprocessed_dataset.append(preprocessed_utterances)
    # dataset = preprocessed_dataset
    base_dir = Path(f'{base_dir}/{dataset}/{model_name}')
    contexts = []
    with (base_dir / 'human_ctx.txt').open() as f:
        for line in f.readlines():
            context = line.strip().split('|||')
            #Spelling corrections
            preprocessed_utterances = []
            for utterance in context:
                preprocessed_utterances.append(checker.correct(utterance).lower())
            contexts.append(preprocessed_utterances)
    
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
            scores.append(score)

    models = [model_name] * len(scores)
    return {
        'contexts': contexts,
        'responses': responses,
        'references': references,
        'models': models,
        'scores': scores
    }


if __name__ == '__main__':
    
    data = load_grade_data('.','convai2', 'bert_ranker')
    
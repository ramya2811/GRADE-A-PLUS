import argparse
from neuspell.noising import CharacterReplacementNoiser
from neuspell.noising import ProbabilisticCharacterReplacementNoiser
from neuspell.noising import WordReplacementNoiser





if __name__ == '__main__':
    # parser = argparse.ArgumentParser()
    # parser.add_argument('--data_path', type=str, help='name of dataset')
    # args = parser.parse_args()
    data_path = "./data/grade_data/convai2/transformer_ranker/human_ctx.txt"
    adversarial_set = []
    example_texts = []

    with open(data_path, "r") as f:
        for line in f.readlines():
            example_texts.append(line)
    print(len(example_texts))

    noisers = [
    CharacterReplacementNoiser,
    # ProbabilisticCharacterReplacementNoiser,
    # WordReplacementNoiser,
    ]

    for noiser in noisers:
        my_noiser = noiser(language="english")
        my_noiser.load_resources()
        for example in example_texts:
            output = my_noiser.noise([example])
            print("OUTPUT",output)
            adversarial_set.append(output[0])
        
    
    print(len(adversarial_set))
    with open("convai2_adversarial.txt","w") as f:
        for line in  adversarial_set:
            print(line)
            f.write(line+"\n")
    #print(adversarial_set)
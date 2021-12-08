import math
import numpy as np
import random

input_original_dialog_filename = "./train/pair-1/original_dialog.text"
input_filename = "./train/pair-1/original_dialog_response.text"
response_output_filename = "./adversarial_word_overlap_response.text"
original_dialog_output_filename = './original_dialog_word_overlap.text'
lexical_negative_samples_output_filename = './adversarial_word_overlap.text'
results_original = []
results_adversarial = []
responses = []

with open(original_dialog_output_filename,"w") as f3: 
    with open(input_original_dialog_filename,"r") as f2:
        texts = f2.readlines()
        i = 0
        while i != 10:
            f3.write(texts[i])
            i+=1


with open(input_filename,"r") as f:
    texts = f.readlines()
    i = 0
    while i != 10:
        responses.append(texts[i])
        text = texts[i]
        text =  text.rstrip('\n')
        words = text.split(' ')
        
        collector = []
        for k in range(5):
            filter_words = [word for word in words if len(word) > 2]
            response_length  = math.ceil(0.75*len(filter_words))
            filtered_sample = random.sample(set(filter_words), response_length)
            response_msg = ' '.join(filtered_sample)
            collector.append(response_msg)

        results_adversarial.append('|||'.join(collector))
        i +=1

with open(lexical_negative_samples_output_filename,"w") as f1:
    for result in results_adversarial:
        f1.write(result+'\n')
        

with open(response_output_filename,"w") as f4:
    for result in responses:
        f4.write(result)
import pickle

with open('..gt_preference_label.pkl', 'rb') as f:
    data = pickle.load(f)

print(data['gt_preference_label'])
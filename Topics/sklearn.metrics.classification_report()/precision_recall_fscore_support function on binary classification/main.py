from sklearn.metrics import precision_recall_fscore_support
import pandas as pd

def solution(true_labels, predicted_labels):
    df = pd.DataFrame({'TL': true_labels, 'PL': predicted_labels})
    precision_scores, recall_scores, f1_scores, supports = precision_recall_fscore_support(df['TL'], df['PL'])
    print(precision_scores[0])

from sklearn.metrics import classification_report
import pandas as pd

def solution(true_labels, predicted_labels):
    df = pd.DataFrame({'TL': true_labels, 'PL': predicted_labels})
    print(classification_report(df['TL'], df['PL'], labels=['apple', 'banana']))
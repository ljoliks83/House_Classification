from sklearn.metrics import classification_report
import pandas as pd

def solution(true_labels, predicted_labels):
    df = pd.DataFrame({'True_labels': true_labels, 'Predicted_labels': predicted_labels})
    print(classification_report(df['True_labels'], df['Predicted_labels'],
                                target_names=['ApPlE', 'BaNaNa', 'OrAnGe', 'PeAr']))
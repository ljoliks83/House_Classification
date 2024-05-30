# Total = 500
# Selection = 200
# Liked_of_Selection = 182
# Liked_of_Non_Selected = 10 / 300

#       TP  TN
#   TP  182 290 TN
#   FP  18  10  FN
#       FP  FN
#

precision = 182 / (182 + 18)
recall = 182 / (182 + 10)
f_score = 2 * precision * recall / (precision + recall)

print(round(f_score, 2))

#       TP  TN
#   TP  4   1   TN
#   FP  2   3   FN
#       FP  FN
#

precision = 4 / (4 + 2)
recall = 4 / (4 + 3)
f_score = 2 * precision * recall / (precision + recall)

print(round(precision, 3))
print(round(recall, 3))
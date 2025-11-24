import json
from utils import plot_metrics_comparison

# Load metrics
knn = json.load(open("knn_metrics.json"))
svm = json.load(open("svm_metrics.json"))
tree = json.load(open("tree_metrics.json"))

plot_metrics_comparison(knn, svm, tree)

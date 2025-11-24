import json
from utils import plot_metrics_comparison

# Load metrics
knn = json.load(open("../../data/processed/knn_metrics.json"))
svm = json.load(open("../../data/processed/svm_metrics.json"))
tree = json.load(open("../../data/processed/dt_metrics.json"))

plot_metrics_comparison(knn, svm, tree)

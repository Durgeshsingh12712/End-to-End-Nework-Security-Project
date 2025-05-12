import sys
from networkSecurity.entity.artifact_entity import ClassificationMetricArtifact
from networkSecurity.exception.exception import NetworkSecurityException
from sklearn.metrics import f1_score, precision_score, recall_score

def get_classification_score(y_actual, y_pred) -> ClassificationMetricArtifact:
    try:

        model_f1_score = f1_score(y_actual, y_pred)
        model_recall_score = recall_score(y_actual, y_pred)
        model_precision_score = precision_score(y_actual, y_pred)

        classification_metric = ClassificationMetricArtifact(
            f1_score=model_f1_score,
            precision_score=model_precision_score,
            recall_score= model_recall_score
        )

        return classification_metric
    except Exception as e:
        raise NetworkSecurityException(e, sys)
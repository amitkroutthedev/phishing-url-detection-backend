import os
import pickle
from django.apps import AppConfig
from django.conf import settings

class PhishingurldetectionappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'phishingUrlDetectionApp'
    MODEL_FILE = os.path.join(settings.BASE_DIR,"phishingUrlDetectionApp/ML/model/XGBoostClassifier.sav")
    model = pickle.load(open(MODEL_FILE,'rb'))

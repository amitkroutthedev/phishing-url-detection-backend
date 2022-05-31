import imp
from django.shortcuts import render
# Create your views here.
import numpy as np
import pandas as pd
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from .apps import *
from .feature import featureExtraction

class Home(APIView):
     def get(self, request):
         response_dict = {"home":"api/?url=(enter the url)"}
         print(response_dict)
         return Response(response_dict, status=200)

class Prediction(APIView):
     def get(self, request):
         url_features=[]
         feature_names = ['having_ip_address', 'long_url', 'shortening_service', 'having_@_symbol', 'redirection_//_symbol', 'prefix_suffix_seperation', 'sub_domains', 'https_token', 'age_of_domain', 'dns_record', 'web_traffic', 'domain_registration_length', 'statistical_report', 'iframe', 'mouse_over']
         url= request.GET.get('url')
         res_temp = np.array(featureExtraction(url))
         url_features.append(res_temp)
         testdata = pd.DataFrame(url_features, columns= feature_names)
         xgboostcls = PhishingurldetectionappConfig.model
         PredictionMade = xgboostcls.predict(testdata)[0]
         url_success_rate = xgboostcls.predict_proba(testdata)[0,0]
         url_phished_rate = xgboostcls.predict_proba(testdata)[0,1]
         url_success_rate = round(url_success_rate*100,2)
         url_phished_rate = round(url_phished_rate*100,2)
         response_dict = {"url": url,"featureExtractionResult":res_temp,"predictionMade":PredictionMade,"successRate":url_success_rate,"phishRate":url_phished_rate}
         print(response_dict)
         return Response(response_dict, status=200)
#imports
#import requests
#import pandas as pd
#import re
#import json
#import math
import os
from dotenv import load_dotenv    #Aquí es donde vy a cargar mi archivo .env y es el unico que necesito, las otra son para las funciones y la dejamos en module.py


#Cogemos todo esto de acquisition method

load_dotenv('.env')
TOKEN = os.environ.get("API_TOKEN")

API_TOKEN = TOKEN   #API TOKEN (REMEMBER: do not push these to your repo)
USERNAME = 'eleluqrey'   #USERNAME
BASE_URL = 'https://api.github.com/'
KEY = 'repos/'
OWNER = 'ih-datapt-mad/'
REPO = 'dataptmad0923_labs/'   #LAB_REPOSITORY
SEARCH = 'search/issues?q=repo:'+OWNER+REPO+'+type:pr+state:{}'
PULLS = 'pulls?page={}&per_page=100&state={}'
COMMITS = 'pulls/{}/commits'
STATE = 'open'

BASE_URL + KEY + OWNER + REPO + PULLS

field_list1 = ['number',
               'title',
               'state',
               'created_at',
               'updated_at',
               'closed_at',
               'html_url',
               'base.repo.full_name',
               'base.ref',
               'head.repo.full_name',
               'head.ref',
               'head.repo.pushed_at']


field_list2 = ['student_name',
               'number',
               'lab_name',
               'state',
               'lab_status',
               'created_at',
               'updated_at',
               'closed_at',
               'html_url',
               'base.repo.full_name',
               'base.ref',
               'head.repo.full_name',
               'head.ref',
               'head.repo.pushed_at']

field_sort1 = ['lab_status',
               'lab_name',
               'student_name']


field_name1 = ['Student Name',
               'PR Number',
               'Lab Name',
               'PR Status',
               'Lab Status',
               'PR Created at',
               'PR Updated at',
               'PR Closed at',
               'PR URL',
               'base repository',
               'base',
               'head repository',
               'compare',
               'Pushed at']


#FUNCIONES
#La hemos copiado en module.py, por ello lo importamos
#AUXILIARY FUNCTIONS
# Aux Function 1: You can get only 100 results per page so it is important to know the number of pages you'll need.

from modules import module as mod

# Damned Pipelines!!!


if __name__ == '__main__':
    DF_PULLS = mod.get_pulls(BASE_URL, KEY, OWNER, REPO, PULLS, SEARCH, STATE, USERNAME, API_TOKEN, field_list1)
    DF_STATUS = mod.df_status(DF_PULLS, BASE_URL, KEY, OWNER, REPO, COMMITS, USERNAME, API_TOKEN, field_list2)
    DF_CSV = mod.create_csv(DF_STATUS, field_sort1, field_name1)


print(DF_CSV)
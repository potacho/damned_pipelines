#Imports 

import requests
import pandas as pd
import re
import json
import math
import os
from dotenv import load_dotenv

from modules import mfunctions

#Inputs

load_dotenv('.env')
TOKEN = os.environ.get("API_TOKEN")

API_TOKEN = TOKEN #API TOKEN (REMEMBER: do not push these to your repo)
USERNAME = "silviluliuma" #USERNAME
BASE_URL = 'https://api.github.com/'
KEY = 'repos/'
OWNER = 'ih-datapt-mad/'
REPO = "dataptmad0923_labs/" #LAB_REPOSITORY
SEARCH = 'search/issues?q=repo:'+OWNER+REPO+'+type:pr+state:{}'
PULLS = 'pulls?page={}&per_page=100&state={}'
COMMITS = 'pulls/{}/commits'
STATE = 'open'

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


def main():
    DF_PULLS = mfunctions.get_pulls(BASE_URL, KEY, OWNER, REPO, PULLS, SEARCH, STATE, USERNAME, API_TOKEN, field_list1)
    DF_STATUS = mfunctions.df_status(DF_PULLS, BASE_URL, KEY, OWNER, REPO, COMMITS, USERNAME, API_TOKEN, field_list2)
    DF_CSV = mfunctions.create_csv(DF_STATUS, field_sort1, field_name1)
    DF_CSV

if __name__ == "__main__":
    main()
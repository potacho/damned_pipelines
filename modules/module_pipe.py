import requests
import pandas as pd
import re
import json
import math

# Pipeline Function 1: And finally get the 'pull requests'.

def get_pulls(base_url, key, owner, repo, pulls, search, state, username, api_token, field_list):
    pulls_list = []
    max_pages = pages(base_url, search, state, username, api_token)
    for i in range(max_pages):
        r_pulls = requests.get(base_url + key + owner + repo + pulls.format(i+1, state),
                               auth=(username, api_token)).json()
        df_pulls = pd.json_normalize(r_pulls)
        pulls_list.append(df_pulls)
    df_pulls = pd.concat(pulls_list)
    df_pulls = df_pulls[field_list]
    return df_pulls


# Pipeline Function 2: Apply!!!!!!

def df_status(df_pulls, base_url, key, owner, repo, commits, username, api_token, field_list):
    df_pulls['student_name'] = df_pulls['title'].apply(student_name)
    df_pulls['lab_name'] = df_pulls['title'].apply(lab_name)
    df_pulls['created_at'] = df_pulls['created_at'].apply(time_parser)
    df_pulls['updated_at'] = df_pulls['updated_at'].apply(time_parser)
    df_pulls['head.repo.pushed_at'] = df_pulls['head.repo.pushed_at'].apply(time_parser)
    df_pulls['lab_status'] = df_pulls.apply(lambda col: get_commits(base_url,
                                                                    key,
                                                                    owner,
                                                                    repo,
                                                                    commits,
                                                                    col['number'],
                                                                    username,
                                                                    api_token), axis=1)
    df_status = df_pulls[field_list]
    return df_status


# Pipeline function 3: And there you have it!!!

def create_csv(df_status, field_sort, field_name):
    df_csv = df_status.sort_values(by=field_sort, ascending=False)
    df_csv.columns = field_name
    df_csv.to_csv('./data/labs_status.csv', index=False)
    return df_csv
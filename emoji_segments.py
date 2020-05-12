# Import needed libraries
import os
import sys

import pandas as pd
import requests
import jwt
from datetime import datetime  
from datetime import timedelta 

# This snippet uses Julien Piccini's Adobe Analytics 2 Python Wrapper
# https://github.com/pitchmuc/adobe_analytics_api_2.0
# make sure to read all the documentation in the repository and in his blog
import adobe_analytics_2.aanalytics2 as api2
api2.importConfigFile('config_analytics_api.json')
cids = api2.getCompanyId()
cid = cids[0]['globalCompanyId']
api2.updateHeader(cid)


# Define needed variables

def emoji_segments(emoji, report_suite, identification_string, prefix = 1):
    # get segments without additional info and every loop returns 1000 items. 
    df_segments = api2.getSegments(extended_info=False)
    # create a numpy array with the segments to be edited with the given parameters
    segments_update = df_segments.loc[(df_segments['rsid'] == report_suite)
                                      & (df_segments['name'].str.contains(identification_string))].to_numpy()
    for i in segments_update:
        # update the segments name
        api2.updateSegment(i[2], {'name' : emoji + " " + i[0] if prefix == 1 else i[0] + " " + emoji})
        
def remove_emojis(emoji, report_suite, identification_string):
    # get segments without additional info and every loop returns 1000 items.
    df_segments = api2.getSegments(extended_info=False)
    # create a numpy array with the segments to be edited with the given parameters
    segments_update = df_segments.loc[(df_segments['rsid'] == report_suite)
                                      & (df_segments['name'].str.contains(identification_string))].to_numpy()
    for i in segments_update:
        # remove emojis from the preselected segments
        api2.updateSegment(i[2], {'name' : i[0].replace(emoji + ' ', '')})
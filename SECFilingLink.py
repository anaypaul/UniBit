import json 
import requests
def getSECFilingLink(baseUrl, endpoint, ticker, AccessKey):
    requestUrl = '{0}/{1}/{2}?AccessKey={3}'.format(baseUrl, endpoint, ticker, AccessKey )
    response = requests.get(requestUrl)
    responseData = response.json()

    for each in responseData:
        for e in each:
            print(e,":", each[e])
        print("*********")
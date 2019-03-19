import json
import requests
def getCIKNumber(baseUrl, endpoint, ticker, AccessKey):
    requestUrl = '{0}/{1}/{2}?AccessKey={3}'.format(baseUrl, endpoint, ticker, AccessKey)
    response = requests.get(requestUrl)
    responseData = response.json()

    print("CIK number ")
    for each in responseData:
        print(each  ,":", responseData[each])
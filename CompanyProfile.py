import json
import requests

def getCompanyProfile(baseUrl, endpoint, ticker, AccessKey):
    requestUrl = '{0}/{1}/{2}?AccessKey={3}'.format(baseUrl, endpoint, ticker, AccessKey)
    response = requests.get(requestUrl)
    responseData = response.json()
    print("Company Profile Information")
    for each in responseData:
        print(each,":", responseData[each])
    print("")
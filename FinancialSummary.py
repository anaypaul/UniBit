import json
import requests

def getFinancialSummary(baseUrl, endpoint, ticker, AccessKey):
    requestUrl = '{0}/{1}/{2}?AccessKey={3}'.format(baseUrl, endpoint, ticker, AccessKey)
    response = requests.get(requestUrl)
    responseData = response.json()
    print("Company's Financial Summary")
    if(responseData.get('message') == None):
        for each in responseData:
            print(each,":", responseData[each])
    else:
        print("error message : ", responseData['message'])
    print("")

import json
import requests
def getCompanyFinancials(baseUrl, endpoint, ticker, docType, interval, AccessKey):
    requestUrl = '{0}/{1}/{2}?type={3}&interval={4}&AccessKey={5}'.format(baseUrl, endpoint, ticker, docType, interval, AccessKey)

    response = requests.get(requestUrl)
    responseData = response.json()
    print("Company's Financial information")
    if(type(responseData) == type([])):
        for each in responseData:
            for e in each:
                print(e,":", each[e])
            print("***********")
    else:
        print(responseData['message'])
    print("")
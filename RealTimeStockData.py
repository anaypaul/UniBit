import requests
import json
def getRealTimeStockData(baseUrl, endpoint, ticker, AccessKey):
    # request_url = "https://api.unibit.ai/realtimestock/{0}?AccessKey={1}".format(ticker, AccessKey)
    request_url = "{0}/{1}/{2}?AccessKey={3}".format(baseUrl,endpoint,ticker,AccessKey)
    response = requests.get(request_url)
    responseData = response.json()
    print("Company's Real Time Stock Data")
    if(type(responseData) == type([])):
        for each in responseData:
            for row in each:
                print(row,":", each[row])
            print("********")
    else:
        print("bad response")
        print(responseData.get('message'))
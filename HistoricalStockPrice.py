import requests
import json
def getHistoricalStockPrice(baseUrl, endpoint, ticker, _range, AccessKey,interval=None):
    if(interval == None):
        requestUrl = '{0}/{1}/{2}?range={3}&AccessKey={4}'.format(baseUrl, endpoint, ticker, _range, AccessKey )   
    else:
        requestUrl = '{0}/{1}/{2}?range={3}&interval={4}&AccessKey={5}'.format(baseUrl, endpoint, ticker, _range, interval, AccessKey )
    response = requests.get(requestUrl)
    responseData = response.json()
    print("Company's Historical Stock Price information")
    if(type(responseData) == type([])):
        for each in responseData:
            for row in each:
                print(row,":", each[row])
            print("********") 
    else:
        print("bad response")
        print(responseData.get('message'))
    print("")
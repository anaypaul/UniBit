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
                print(row, each[row])
            print("********")
    else:
        print("bad response")
        print(responseData.get('message'))
    
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
                print(row, each[row])
            print("********") 
    else:
        print("bad response")
        print(responseData.get('message'))
    print("")
def getCompanyFinancials(baseUrl, endpoint, ticker, docType, interval, AccessKey):
    requestUrl = '{0}/{1}/{2}?type={3}&interval={4}&AccessKey={5}'.format(baseUrl, endpoint, ticker, docType, interval, AccessKey)

    response = requests.get(requestUrl)
    responseData = response.json()
    print("Company's Financial information")
    if(type(responseData) == type([])):
        for each in responseData:
            for e in each:
                print(e, each[e])
            print("***********")
    else:
        print(responseData['message'])
    print("")
def getCompanyProfile(baseUrl, endpoint, ticker, AccessKey):
    requestUrl = '{0}/{1}/{2}?AccessKey={3}'.format(baseUrl, endpoint, ticker, AccessKey)
    response = requests.get(requestUrl)
    responseData = response.json()
    print("Company Profile Information")
    for each in responseData:
        print(each, responseData[each])
    print("")

def getFinancialSummary(baseUrl, endpoint, ticker, AccessKey):
    requestUrl = '{0}/{1}/{2}?AccessKey={3}'.format(baseUrl, endpoint, ticker, AccessKey)
    response = requests.get(requestUrl)
    responseData = response.json()
    print("Company's Financial Summary")
    if(responseData.get('message') == None):
        for each in responseData:
            print(each, responseData[each])
    else:
        print("error message : ", responseData['message'])
    print("")

def getOwnershipStructure(baseUrl, endpoint, ticker, ownershipType, AccessKey):
    requestUrl = '{0}/{1}/{2}?ownership_type={3}&AccessKey={4}'.format(baseUrl, endpoint, ticker,ownershipType, AccessKey )
    response = requests.get(requestUrl)
    responseData = response.json()
    
    print("Company Ownership information")
    for each in responseData:
        print(type(responseData[each]))
        if(type(responseData[each]) == type({})):
            for e in responseData[each]:
                print(e, responseData[each][e])
        elif(type(responseData[each]) == type([])):
            temp = responseData[each]
            for each in temp:
                for e in each:
                    print(e, each[e])
        elif(type(responseData[each]) == type("")):
            print(each , responseData[each])

def getInsiderTransaction(baseUrl, endpoint, ticker, AccessKey):
    requestUrl = '{0}/{1}/{2}?AccessKey={3}'.format(baseUrl, endpoint, ticker, AccessKey)
    response = requests.get(requestUrl)
    responseData = response.json()
    
    print("Company Insider Transaction")
    for each in responseData:
        for e in each:
            print(e, each[e])
        print("*********")

def main():
    AccessKey = '0uol5RvbDpBHJTPLriKKvNptW7kPYiFk'
    ticker = 'AMZN'
    base_url = 'https://api.unibit.ai'
    #realtime stock price
    realTimeStockEndpoint = 'realtimestock'

    #historical stock price
    historialStockEndpoint = 'historicalstockprice'
    _range = ['1m','3m','1y','3y','5y','10y','20y']
    interval = 1

    # Company financial 
    companyfinancialEndpoint = 'financials'
    docType = ['income_statement', 'balance_sheet', 'cash_flow']
    _interval = ['annual', 'quarterly']

    # Company profile
    companyProfileEndpoint = 'companyprofile'

    # Company financial summary
    companyFinancialSummaryEndpoint = 'financials/summary'

    #Company ownership Structure
    companyOwnershipStructureEndpoint = 'ownership'
    ownershipType = ['majority_holder', 'top_institutional_holder', 'top_mutual_fund_holder']

    # Company insider transaction
    companyInsiderTransaction = 'insidertrading'
    x = 0
    while True:
        print("Menu :(Select one of the following operations by pressing the corresponding number)")
        print("0. Exit program")
        print("1. Get Real Time Stock Data ")


    getRealTimeStockData(base_url,realTimeStockEndpoint,ticker, AccessKey)
    getHistoricalStockPrice(base_url, historialStockEndpoint, ticker, _range[0], AccessKey, interval)
    getCompanyFinancials(base_url, companyfinancialEndpoint, ticker, docType[0], _interval[0], AccessKey )
    getCompanyProfile(base_url, companyProfileEndpoint, ticker,  AccessKey)
    getFinancialSummary(base_url, companyFinancialSummaryEndpoint, ticker, AccessKey)
    getOwnershipStructure(base_url, companyOwnershipStructureEndpoint, ticker, ownershipType[1], AccessKey)
    getInsiderTransaction(base_url, companyInsiderTransaction, ticker, AccessKey)

if __name__ == '__main__':
    main()
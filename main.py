import requests
import json
from RealTimeStockData import *
from HistoricalStockPrice import * 
from CompanyFinancials import *
from CompanyProfile import *
from FinancialSummary import *
from OwnershipStructure import *
from InsiderTransaction import *
from CIKNumber import *
from SECFilingLink import *


def main():
    AccessKey = '0uol5RvbDpBHJTPLriKKvNptW7kPYiFk'
    base_url = 'https://api.unibit.ai'
    Endpoints = {'realTimeStockEndpoint':'realtimestock', 'historialStockEndpoint':'historicalstockprice','companyfinancialEndpoint':'financials','companyProfileEndpoint':'companyprofile','companyFinancialSummaryEndpoint':'financials/summary','companyOwnershipStructureEndpoint':'ownership','companyInsiderTransactionEndpoint':'insidertrading','CIKNumberEndpoint':'company/cik','SECFilingLinkEndpoint':'company/sec'}
    
    #historical stock price
    _range = ['1m','3m','1y','3y','5y','10y','20y']

    # Company financial 
    docType = ['income_statement', 'balance_sheet', 'cash_flow']
    _interval = ['annual', 'quarterly']
    
    #Company ownership Structure
    ownershipType = ['majority_holder', 'top_institutional_holder', 'top_mutual_fund_holder']
    
    ticker = 'AMZN' #Amazon stock code.

    x = 0
    while True:
        print("Menu :(Select one of the following operations by pressing the corresponding number)")
        print("0. Exit program")
        print("1. Get RealTime Stock Data ")
        print("2. Get Historical Stock Price")
        print("3. Get Company Financials")
        print("4. Get Company information")
        print("5. Get Company Financial Summary")
        print("6. Get Ownership Structure of a Stock")
        print("7. Get Insider Transactions")
        print("8. Get CIK Number")
        print("9. Get SEC Filing Link")
        x = int(input())
        if(x == 0):
            print("Terminating program.")
            break
        elif(x==1):
            getRealTimeStockData(base_url,Endpoints['realTimeStockEndpoint'],ticker, AccessKey)
        elif(x==2):
            print("Select the range by pressing the number correspondig to the below list")
            for i in range(len(_range)):
                print(i, _range[i])
            _rangeIndex = int(input())
            interval = int(input("Enter the value of interval(n) to get every nth record from historical record"))
            getHistoricalStockPrice(base_url, Endpoints['historialStockEndpoint'], ticker, _range[_rangeIndex], AccessKey, interval)
        elif(x==3):
            print("Select one of the document types below:")
            for i in range(len(docType)):
                print(i,docType[i])
            docTypeIndex = int(input())
            print("Select the interval type from below by pressing the corresponding option number")
            for i in range(len(_interval)):
                print(i, _interval[i])
            _intervalIndex = int(input())
            getCompanyFinancials(base_url, Endpoints['companyfinancialEndpoint'], ticker, docType[docTypeIndex], _interval[_intervalIndex], AccessKey )
        elif(x==4):
            getCompanyProfile(base_url, Endpoints['companyProfileEndpoint'], ticker,  AccessKey)
        elif(x==5):
            getFinancialSummary(base_url, Endpoints['companyFinancialSummaryEndpoint'], ticker, AccessKey)
        elif(x==6):
            print("Select the ownership type by pressing the corresponding option number")
            for i in range(len(ownershipType)):
                print(i, ownershipType[i])
            ownwershipTypeIndex = int(input())
            getOwnershipStructure(base_url, Endpoints['companyOwnershipStructureEndpoint'], ticker, ownershipType[ownwershipTypeIndex], AccessKey)
        elif(x==7):
            getInsiderTransaction(base_url, Endpoints['companyInsiderTransactionEndpoint'], ticker, AccessKey)
        elif(x==8):
            getCIKNumber(base_url, Endpoints['CIKNumberEndpoint'], ticker, AccessKey)
        elif(x==9):
            getSECFilingLink(base_url, Endpoints['SECFilingLinkEndpoint'], ticker, AccessKey)
        else:
            print("Select a valid option. Try Again.")
    

if __name__ == '__main__':
    main()
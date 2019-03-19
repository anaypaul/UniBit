import json
import requests

def getOwnershipStructure(baseUrl, endpoint, ticker, ownershipType, AccessKey):
    requestUrl = '{0}/{1}/{2}?ownership_type={3}&AccessKey={4}'.format(baseUrl, endpoint, ticker,ownershipType, AccessKey )
    response = requests.get(requestUrl)
    responseData = response.json()
    
    print("Company Ownership information")
    for each in responseData:
        print(type(responseData[each]))
        if(type(responseData[each]) == type({})):
            for e in responseData[each]:
                print(e,":", responseData[each][e])
        elif(type(responseData[each]) == type([])):
            temp = responseData[each]
            for each in temp:
                for e in each:
                    print(e,":", each[e])
        elif(type(responseData[each]) == type("")):
            print(each ,":", responseData[each])

import urllib.request
import json

def searchNaverNews(keyword, start, display) :

    client_id = "8os69VYnBk5H5QpLkte1"
    client_secret = "kPicTeAw_3"

    encText = urllib.parse.quote(keyword)

    url = "https://openapi.naver.com/v1/search/news?query=" + encText

    new_url = url + f"&start={start}&display={display}"
    request = urllib.request.Request(new_url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)

    resultJSON = None

    try :
        response = urllib.request.urlopen(request)

        rescode = response.getcode()
        if(rescode==200):
            response_body = response.read()
            resultJSON = json.loads(response_body.decode('utf-8'))
        else:
            print("Error Code : " + rescode)
    except Exception as e :
        print(e)
        print(f"Error : {new_url}")
    
    return resultJSON 

def setNewsSearchResult(resultAll, resultJSON):
    for result in resultJSON['items'] :
        resultAll.append(result)    

def saveSearchResult_CSV(json_list, filename):
    import pandas as pd
    data_df = pd.DataFrame(json_list)
    data_df.to_csv(filename)
    print(f"{filename} SAVED")

keyword = ''

resultAll = []

start = 1
display = 10
resultJSON = searchNaverNews(keyword, start, display)

while (resultJSON != None) and (resultJSON['display'] > 0 and start != 201) :

    setNewsSearchResult(resultAll, resultJSON)

    start += display
    
    resultJSON = searchNaverNews(keyword, start, display)

    if resultJSON != None :
        print(f"{keyword} [{start}] : Search Request Success")
    else :
        print(f"{keyword} [{start}] : error")

filename = f"./KeywordVisualizerApp/data/{keyword}_naver_news.csv"
saveSearchResult_CSV(resultAll, filename)
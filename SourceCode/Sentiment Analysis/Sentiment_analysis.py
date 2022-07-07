import pandas as pd
import urllib3
import json
import time
import numpy

data=pd.read_csv('.csv')
review_list=data.review

labels=[]
label_prediction =[]

access_token='24.def0b4f1b57ad636ca638ba559b45992.2592000.1650805234.282335-25847279'
http=urllib3.PoolManager()
url='https://aip.baidubce.com/rpc/2.0/nlp/v1/sentiment_classify?access_token='+access_token
print(url)

for i in range(len(review_list)):
    if (i + 1) % 2 == 0:
        time.sleep(1)
    params={'text':review_list[i]}
    encoded_data = json.dumps(params).encode('utf-8')
    request = http.request('POST',
                           url,
                           body=encoded_data,
                           headers={'Content-Type': 'application/json'})
    try:
        result = str(request.data, 'GBK')
        a = json.loads(result)
        output = a['items'][0]
        labels.append(output['sentiment'])
        label_prediction.append(output['positive_prob'])
        print("第 " + str(i + 1) + "条评论已完成分析")
    except:
        data.drop(data.index[i],inplace=True)
        pass

data['label']=labels   # 0 Negative 1 Neutral 2 Positive
data['positive_prob']=label_prediction
data.to_csv('reviews_details_all_US_Apple_fitbit_89274_last.csv',encoding="utf-8")


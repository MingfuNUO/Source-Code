import pandas as pd
import json
import urllib.request
import urllib.parse
import urllib.request

data=pd.read_csv('')

review_list=data.review

url = "https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials"
values = {
 'host':'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials',
 'client_id':'HXGkE5QzaOizqryXaYMVkuIN',  #API KEY
 'client_secret' : 'WLcCv99H6NTs35koMaiGzpNI167o02no' #Secret Key
}
# client_id AND client_secret
host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=HXGkE5QzaOizqryXaYMVkuIN&client_secret=WLcCv99H6NTs35koMaiGzpNI167o02no'
request = urllib.request.Request(host)
request.add_header('Content-Type', 'application/json; charset=UTF-8')
response = urllib.request.urlopen(request)
content = response.read()
if (content):
    print(content)  # access token

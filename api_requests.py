import urllib.request
import urllib.parse

url="https://www.carmax.com/cars/api/search/run"
#url="https://api.carmax.com/v1/api/vehicles"
user_agent='Mozilla/5.0 (X11; Linux x86_64; rv:81.0) Gecko/20100101 Firefox/81.0'

def open_request(req):
    response = None
    with urllib.request.urlopen(req,timeout=2) as resp:
        response = resp.read()
    return response

def car_request(uri,radius,zip):
    values = {}
    values['uri']=uri
    #values['skip']=0
    #values['take']=24
    #values['radius']=radius
    #values['zipCode']=zip
    #values['sort']=14
    data = urllib.parse.urlencode(values)
    
    headers = {'User-Agent' : user_agent,
        'Host' : 'www.carmax.com',
        'Accept' : '*/*;q=0.8',
        'Accept-Language' : 'en-US,en;q=0.5',
        'Accept-Encoding' : 'gzip, deflate, br',
        #'Content-Type' : 'application/json',
        'DNT' : '1',
        'Connection' : 'keep-alive',
        'Upgrade-Insecure-Requests' : '1'}
    
    full_url = url + "?" + data
    print(full_url)
    req = urllib.request.Request(full_url,data=None,headers=headers,method='GET')
    print(req.method)
    print(req.data)
    print(req.full_url)
    return open_request(req)
    



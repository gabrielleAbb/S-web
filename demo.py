import requests
res = requests.get('https://images-na.ssl-images-amazon.com/images/I/81OaK1m93CL._SX466_.jpg')
#print(res.headers)
#print(res.json())
with open("FACEMASK.png",'wb') as f:
    f.write(res.content)

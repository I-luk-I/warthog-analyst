import requests
url='http://188.234.5.83:3000'
height=requests.get(f"{url}/chain/head").json()['data']['height']

miners=f'{url}/chain/block/'
          
list_miners={}

for i in range (height-4000,height):
    url_block_info=requests.get(f'{url}/chain/block/{i}').json()
    if url_block_info['data']['body']['rewards'][0]['toAddress'] in list_miners:
        list_miners[url_block_info['data']['body']['rewards'][0]['toAddress']]+=3
    else:
        list_miners[url_block_info['data']['body']['rewards'][0]['toAddress']]=3
with open ('values.txt','w') as file:
    file.write(str(list_miners.items()))


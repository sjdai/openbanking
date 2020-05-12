import yaml
import json
import base64
#from ruamel.yaml import YAML
import requests


def test_get_access_token():
    client_id = '2ph676ka96q2h7j163tienpbaa'
    client_secret = '199jnnko86u604bgbfkhojqh0afv9s69pg2da79d5pbpkrp9aopf'
    url = 'https://labrochure-test.auth.us-east-1.amazoncognito.com'
    path = '/oauth2/token?grant_type=client_credentials&users/users.create'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': generate_authorization_header(client_id, client_secret),
    }
    #response = requests.post(url+path, headers=headers)
    #print(response.json())
    #assert 'access_token' in response.json()
    #assert response.headers['Content-Type'] == "application/json"
    #assert response.status_code == 200



def main():
    url = 'http://127.0.0.1:5000/test/oauth'
    #myobj = {'somekey': 'somevalue'}

    x = requests.get(url)
    #assert response.status_code == 200
    #print(dir(x))
    #print(type(x.text))
    #print(type("success"))
    
    print('連線成功')
        #print(type(x))
    print('測試主機URL:',x.url)

    y = requests.get(x.text.replace("\"", "").strip())

    print('授權主機URL:',y.url)

    print('授權呼叫授權主機成功:',y.url)

    payload = {'username': 'username', 'password': 'password'}
    z = requests.get(y.text.replace("\"", "").strip(), params=payload)


    
    print('登入狀態:',z.text)

    

    
    


if __name__ == "__main__":
    main()

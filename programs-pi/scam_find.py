import ConfigParser
import requests
import json
def find_object():
        url = "http://api.imagga.com/v1/content"
        files = {"file": open("input.jpg", "rb")}
        config = ConfigParser.ConfigParser()
        config.read('web_service.conf')
        authorization = config.get('imagga', 'authorization')
        headers = { 
            "accept": "application/json",
            "authorization": authorization
            }   
        response = requests.post(url, files=files, headers=headers)
        #print response.text
        data = json.loads(response.text.encode("ascii"))
        uid = data["uploaded"][0]["id"]
        url = "http://api.imagga.com/v1/tagging"
        querystring = {"content": data["uploaded"][0]["id"]}
        response = requests.request("GET", url, headers=headers, params=querystring)
        data = json.loads(response.text.encode("ascii"))
        tag = data["results"][0]["tags"][0]["tag"].encode("ascii")
        tag1 = data["results"][0]["tags"][1]["tag"].encode("ascii")
        tag2 = data["results"][0]["tags"][2]["tag"].encode("ascii")
        print "Object is"
        print "<< " + tag +" >>"
        return tag
find_object()

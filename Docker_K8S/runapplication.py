import requests

url = "http://a20f66dec1b9e4c1eafcad89b2099f8f-650654308.eu-north-1.elb.amazonaws.com/predict" # load balancer dns

data = {
    "cgpa": 7.32,
    "iq": 97,
    "profile_score": 54
}

response = requests.post(url, json=data)

print(response.json())

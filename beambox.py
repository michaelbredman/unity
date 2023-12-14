
import requests
data = "body: {limit: 2, offset: 0, timestamp: '2022-11-23'}"
r = requests.get("https://beambox.com/api/v1/9628bc4153ef44b56c32/guests", data=data )
ID = r.json()
for key in ID:{
    print(key, "|||||||||-------\n\n\n", ID) 
}



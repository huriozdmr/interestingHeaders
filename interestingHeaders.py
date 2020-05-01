import requests
import re 
import os

headers=[]

global i
i=0

X_file = open("xHeaders.txt", "a")
H_file = open("headers.txt", "a")

with open('alexa-tops.txt','r') as file:
    sites=file.readlines()
    for site in sites:
        site=sites[i]
        req = sites[i].strip()
        url="http://"+req
        try:
            response = requests.get(url)
            dictHeaders=dict(response.headers)
            headers.append(list(dictHeaders.keys()))
            i+=1
            for j in headers[-1]:
                if re.match(r"^X",j, re.IGNORECASE):
                    X_file.write(j+'\n') 
                else:
                    H_file.write(j+'\n')
                        
        except (requests.exceptions.RequestException, ConnectionResetError) as err:
            print(err)
            print('\n En son {}. siteye istek yapıldı'.format(i))
            continue

print(i)
    
X_file.close()
H_file.close()


command = 'sort -u xHeaders.txt | tee uniqList.txt > /dev/null'
os.system(command)
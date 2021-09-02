import requests
import time
import json
import pandas

file_path = str(input('Please enter the file: '))
domain_CSV = pandas.read_csv((file_path))

Urls = domain_CSV['Domain'].tolist()
print("Urls: ", Urls)
API_key = '7e5ad3a7cce19de66a0b55171ab75d7b4896e0213cee2398b34c7e928bc2b01e'
url = 'https://www.virustotal.com/vtapi/v2/url/report'

parameters = {'apikey': API_key, 'resource': Urls}

for i in Urls:
    parameters = {'apikey': API_key, 'resource': i}
    response = requests.get(url, parameters)
    print("response.text: ", response.text)
    json_response = json.loads(response.text)
    
    if json_response['response_code'] <= 0:
        with open('Not Found result.txt', 'a')  as notfound:
            notfound.write(i) and notfound.write("\t NOT found, please scan it manually\n")
    elif json_response['response_code'] >= 1:

        if json_response['positives'] <= 0:
            with open('Virustotal Clean result.txt', 'a')  as clean:
                clean.write(i) and clean.write("\t NOT malicious \n")
        else:
            with open('Virustotal Malicious result.txt', 'a')  as malicious:
                malicious.write(i) and malicious.write("\t Malicious \n") 

    time.sleep(15)

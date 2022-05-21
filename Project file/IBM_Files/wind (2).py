import requests

# NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
API_KEY = "8r_73r_kobxkRh4xVZMTU29nikPAwCq3_2et93LJDKCj"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey": API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

# NOTE: manually define and pass the array(s) of values to be scored in the next line
payload_scoring = {"input_data": 
			[{"field": [["Theoretical_Power_Curve (KWh)", "WindSpeed(m/s)"]], 
			"values": [[609.081469,5.952496]]}]}

response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/f33e7f01-076e-46b1-846a-7a3a74afa11b/predictions?version=2021-10-28', json=payload_scoring, headers={'Authorization': 'Bearer ' + mltoken})
print("Scoring response")
predictions =response_scoring.json()
print(predictions)
print('Final Prediction Result',predictions['predictions'][0]['values'][0][0])

#['Theoretical_Power_Curve (KWh)', 'WindSpeed(m/s)']
from pdo import cnx
import requests
import base64
import json

sql_select_query = "select * from settings"
cursor = cnx.cursor()
cursor.execute(sql_select_query)
records = cursor.fetchall()

for row in records:

    clientid = row[0]
    refresh_token = row[4]
    clientSecret = row[5]
    

headers = {'Authorization': 'Basic ' + base64.b64encode(clientid+":" +clientSecret),'Content-Type': 'application/x-www-form-urlencoded'}
params = {'refresh_token' : refresh_token, 'grant_type':'refresh_token'}
response = requests.post('https://api.fitbit.com/oauth2/token',headers=headers, params=params)

jsonresponse = json.loads(response.content)

refresh_token = jsonresponse['refresh_token'] 
access_token = jsonresponse['access_token'] 

sql_select_query = """update settings set refresh_token=%s, acces_token=%s """

cursor.execute(sql_select_query,(refresh_token,access_token))

cnx.commit()



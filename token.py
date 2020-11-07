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
    authorization_code = row[1]
    redirect_uri = row[2]
    clientSecret = row[5]


headers = {'Authorization': 'Basic ' + base64.b64encode(clientid+":" +clientSecret),'Content-Type': 'application/x-www-form-urlencoded'}
params = {'code' : authorization_code, 'clientId':clientid,'grant_type':'authorization_code','redirect_uri':redirect_uri}
response = requests.post('https://api.fitbit.com/oauth2/token',headers=headers, params=params)

jsonresponse = json.loads(response.content)

acces_token = jsonresponse['access_token'] 
refresh_token = jsonresponse['refresh_token'] 


sql_select_query = """update settings set refresh_token=%s, acces_token=%s """

cursor.execute(sql_select_query,(refresh_token,acces_token))

cnx.commit()
cnx.close()


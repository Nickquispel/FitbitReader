import refreshtoken
import requests
import json

sql_select_query = "select * from settings"
refreshtoken.cursor.execute(sql_select_query)
records = refreshtoken.cursor.fetchall()

for row in records:

    access_token = row[3]

params = {'afterDate': '2020-07-24','offset':'0','limit':20,'sort':'asc'}
headers = {'Authorization': 'Bearer ' + access_token}
# response = requests.get('https://api.fitbit.com/1/user/-/activities/heart/date/today/1d.json',headers=headers)
# response = requests.get('https://api.fitbit.com/1/user/-/activities/heart/date/2020-07-27/1d/1sec/time/00:00/00:01.json',headers=headers)
# response = requests.get('https://api.fitbit.com/1/user/-/activities/list.json',headers=headers,params=params)
response = requests.get('https://api.fitbit.com/1/user/-/activities/date/2020-07-28.json',headers=headers)
jsonresponse = json.dumps(json.loads(response.content))

print(jsonresponse)

# for activity_heart in jsonresponse['activities-heart']:
#     print (activity_heart['value']['restingHeartRate'])
#     for heartratezone in activity_heart['value']['heartRateZones']:
#         print('Max = ', heartratezone['max'])
#         print('Min = ' , heartratezone['min'])
#         print('Minutes = ' , heartratezone['minutes'])
#         print('Name = ' , heartratezone['name'])
#         print('Calories = ' , heartratezone['caloriesOut'])

refreshtoken.cnx.close()


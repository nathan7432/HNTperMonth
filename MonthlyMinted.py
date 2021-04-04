import datetime
import requests

x = datetime.datetime.now()
current_year = int(x.strftime('%G'))
current_month = int(x.strftime('%m'))
years = range(2019, current_year+1)
param_list = []

for year in years:
    if year == 2019:
        months = range(7,13)
        for month in months:
            month = str(month).zfill(2)
            param_list.append(f'{year}-{month}-01T00:00:00Z')
    elif year == current_year:
        months = range(1, current_month+1)
        for month in months:
            month = str(month).zfill(2)
            param_list.append(f'{year}-{month}-01T00:00:00Z')
    else:
        months = range(1, 13)
        for month in months:
            month = str(month).zfill(2)
            param_list.append(f'{year}-{month}-01T00:00:00Z')

print(param_list)

sum = 0
for i in range(0,len(param_list)-1):
    parameters = {
            'min_time': param_list[i],
            'max_time': param_list[i+1]
    }
    response = requests.get(f'https://api.helium.io/v1/rewards/sum', params=parameters)
    resp = dict(response.json())
    print(f"Month:{param_list[i][:7]} HNT Minted:{resp['data']['total']}")
    sum = sum + resp['data']['total']

parameters = {
    'min_time': param_list[-1]
}
response = requests.get(f'https://api.helium.io/v1/rewards/sum', params=parameters)
resp = dict(response.json())
print(f"Month:{param_list[-1][:7]} HNT Minted:{resp['data']['total']}")
sum = sum + resp['data']['total']



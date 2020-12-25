import requests
print(requests.post('https://api-fns.ru/api/egr?req=772627326802&key=cb5a1bc342a93026c99f064af4aed24053dc0970').json()['items'][0]['ИП']['ФИОПолн'])
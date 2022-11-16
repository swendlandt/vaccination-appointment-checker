import requests

cookies = {
    'bm_sz': '',
    'ak_bmsc': '',
    'bm_sv': '',
    'akavpau_User_allowed': '',
    '_abck': '',
}

headers = {
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
    'Accept': 'application/json, text/plain, */*',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
    'Content-Type': 'application/json',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://005-iz.impfterminservice.de/impftermine/service?plz=76137',
    'Accept-Language': 'de-DE,de;q=0.9',
}

params = (
    ('plz', '76137'),
    ('leistungsmerkmale', 'L920,L921,L922,L923'),
)

response = requests.get('https://005-iz.impfterminservice.de/rest/suche/termincheck', headers=headers, params=params, cookies=cookies)

print(response.status_code)
print(response.json())

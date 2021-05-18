import requests

cookies = {
    'bm_sz': 'C7A4773001A5D93E87776315B0F08A39~YAAQBFhlX6GJKz95AQAAI7lSQwsymwGiLUHYOPs9+Ekz0P2153/GnyQkboir5zqz2nVdkTpoIfRBgjImottrfP0oxnDF/I+xkeEJU1XzGe0pQdAhy2EvtoRtGOpd5/hfZCw+ayqf9V6yrbw2QVMwXTusQKkTQe9ABRi+HkeuH1vQUQbOLKITxZxa+H/LGhXCQJb66djerZDY7A==',
    'ak_bmsc': '6C669504930F790B9ACB9089D4A6EC165F6558042C280000854E94603B28D31E~pl0uFG6o5FpRRhuA2bGyf98TDuHq2EoMAs+pfL2iozXmdbC/S10Zl+5o7p1KLLkF4EupnPzaP9jxet4jABqPmxaW5JmU9aBENgp8B2xUSD4bxhL9hbSbrCOXF2f9gqNhwVa0SQgJYbQl4aB4g0zs1OH4r+UxiiAAtndoD+oTCmwYL4RItJvrs1Dv42YwaXtyh/GYgycF49imzBmKwc8vGlw1lffOjhmbE8vnhfuowziaVR2WlX/zjMsXBtMEPcL49z',
    'bm_sv': '797A9CC5D40D77270CC4C9F701B11330~bmCoFEa8/bT1QpigB0u6u3IZi/pI5CaBFJVkwtw8tuT9UHKfj0OkUhJ+C3S+4YzbrclJInwUi8LLGzvgzZwEC+098pWViiT+Phlv+Y50fhBaoi0J6JcLyxF5SUxts3dXPpVqSs5k7BQthk8OZR7hoML8uAv58Ek77qNlhf7GKjQ=',
    'akavpau_User_allowed': '1620332810~id=79c89548a51d76717cbb3ace0353fad7',
    '_abck': 'D26F788FDCD902F6821A73C02D327A93~-1~YAAQDLUQAgLPBEF5AQAAruhbQwUaoCPUoJ2+jMHQDt6nz9PbA6nr0pIUpp+Gzm62U6ndu150MCA/yO4LdvtsoPrCCVtGZUFckt4u7x3Fiy1aaCwieB6lplMSYo0Ld3C3qOg2X09+sjgUERSuU8p4VAsPbRmUFvUOeJdu2LU30XPMspvFmlm0q/3wr7+jaV6yEPKKi7DEkj181Qr1enmHAlrYzcmmqVIUAyPGiTkYtgSo3VGDRNmSljefcj9fLoJCDZDSSzEUNn2kYqOkU6V3I1zKVNfx+Hv7DXlmzlNa3lmn56JyDtBVdsKEsXAnV/oDAm4jBq3YoYBaq4p1IflxLug957v6MlALV2nJX9DgGF2upkUqX/xzzs7K~-1~-1~-1',
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

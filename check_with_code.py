import ssl
import time

port = 465  # For SSL
password = ""

# Create a secure SSL context
context = ssl.create_default_context()

sender_email = ""
receiver_email = ""
message = "Subject: Impftermine verfügbar!".encode("utf-8")

import requests

cookies = {
    "bm_sz": "",
    "ak_bmsc": "",
    "akavpau_User_allowed": "",
    "bm_sv": "",
    "_abck": "",
}

headers = {
    "Connection": "keep-alive",
    "Pragma": "no-cache",
    "Cache-Control": "no-cache",
    "sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
    "Accept": "application/json, text/plain, */*",
    "Authorization": "Basic Okg2NFUtV1hIWC0yUVBH",
    "sec-ch-ua-mobile": "?0",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36",
    "Content-Type": "application/json",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://005-iz.impfterminservice.de/impftermine/suche/H64U-WXHX-2QPG/76137",
    "Accept-Language": "de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7",
}

states = requests.get(
    "https://www.impfterminservice.de/assets/static/impfzentren.json", headers=headers
).json()

print(states)

sleep_time = 30


def check_vaccination_center(vaccination_center):
    plz = vaccination_center["PLZ"]
    print(plz)

    params = (("plz", plz),)
    response = requests.get(f"{vaccination_center['URL']}rest/login")
    print(response.json())
    url = f"{vaccination_center['URL']}rest/suche/impfterminsuche"
    response = requests.get(
        url,
        headers=headers,
        params=params,
        cookies=cookies,
    )

    print(response.status_code)
    try:
        response_json = response.json()
        print(response_json)
        if (
            response.status_code == 429
            or "termineVorhanden" not in response_json.keys()
        ):
            time.sleep(sleep_time)
            cookies["_abck"] = input("Enter new cookie:")
            check_vaccination_center(vaccination_center)
    except JSONDecodeError:
        print("waitroom")
    time.sleep(sleep_time)


for state in states.values():
    print(state)
    for current_vaccination_center in state:
        check_vaccination_center(current_vaccination_center)

# with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
#     server.login(sender_email, password)
# server.sendmail(sender_email, receiver_email, message)

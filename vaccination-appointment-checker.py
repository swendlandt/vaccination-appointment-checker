import json
import ssl
import time
from json import JSONDecodeError

import requests


class bcolors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


port = 465  # For SSL
password = ""

# Create a secure SSL context
context = ssl.create_default_context()

sender_email = ""
receiver_email = ""
message = "Subject: Impftermine verfügbar!".encode("utf-8")

headers = {
    "Connection": "keep-alive",
    "Pragma": "no-cache",
    "Cache-Control": "no-cache",
    "sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
    "Accept": "application/json, text/plain, */*",
    "sec-ch-ua-mobile": "?0",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
    "Content-Type": "application/json",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://005-iz.impfterminservice.de/impftermine/service?plz=76137",
    "Accept-Language": "de-DE,de;q=0.9",
}

states = requests.get(
    "https://www.impfterminservice.de/assets/static/impfzentren.json", headers=headers
).json()

vaccination_list = requests.get(
    "https://www.impfterminservice.de/assets/static/its/vaccination-list.json",
    headers=headers,
).json()

print(vaccination_list)

sleep_time = 90

waitroom_counter = 0

start_plz = int(input("Enter PLZ to start:"))

with open("cookies.json") as cookies_file:
    cookies = json.load(cookies_file)

def check_vaccination_center(vaccination_center):
    global waitroom_counter
    global cookies
    plz = vaccination_center["PLZ"]

    if int(plz) < start_plz:
        return

    print(plz)
    params = (
        ("plz", plz),
        ("leistungsmerkmale", "L920,L921,L922,L923"),
    )
    url = f"{vaccination_center['URL']}rest/suche/termincheck"

    headers = {
        "Connection": "keep-alive",
        "Pragma": "no-cache",
        "Cache-Control": "no-cache",
        "sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
        "Accept": "application/json, text/plain, */*",
        "sec-ch-ua-mobile": "?0",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
        "Content-Type": "application/json",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://005-iz.impfterminservice.de/impftermine/service?plz=76137",
        "Accept-Language": "de-DE,de;q=0.9",
    }

    center_url = f"{vaccination_center['URL']}impftermine/service?plz={plz}"

    headers["Referer"] = center_url

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
            input(bcolors.WARNING + "Enter new cookies" + bcolors.ENDC)
            with open("cookies.json") as cookies_file:
                cookies = json.load(cookies_file)
                check_vaccination_center(vaccination_center)
        if "termineVorhanden" in response_json and response_json["termineVorhanden"]:
            found_vaccinations = (
                v
                for v in vaccination_list
                if v["qualification"] in response_json["vorhandeneLeistungsmerkmale"]
            )
            print(
                bcolors.FAIL
                + "Found"
                + ", ".join(str(v) for v in found_vaccinations)
                + " in "
                + plz
                + "\n Click here: "
                + center_url
                + bcolors.ENDC
            )

    except JSONDecodeError:
        print("waitroom")
        waitroom_counter += 1
        if waitroom_counter < 5:
            time.sleep(sleep_time)
            check_vaccination_center(vaccination_center)
    time.sleep(sleep_time)


for state in states.values():
    print(state)
    for current_vaccination_center in state:
        check_vaccination_center(current_vaccination_center)
        waitroom_counter = 0
# with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
#     server.login(sender_email, password)
# server.sendmail(sender_email, receiver_email, message)

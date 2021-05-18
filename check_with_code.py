import ssl
import time

port = 465  # For SSL
password = "yJw$YWPG5lmx0W"

# Create a secure SSL context
context = ssl.create_default_context()

sender_email = "simonsthrowaway012@gmail.com"
receiver_email = "simonwendlandt@gmail.com"
message = "Subject: Impftermine verfügbar!".encode("utf-8")

import requests

cookies = {
    "bm_sz": "4AC70D7068AB7544AE6B4BE8D5B15476~YAAQ2OF7XHsTPzt5AQAAnHFSSAurs9GDaQIt4zKYd6Aip99VqngNW3t/4LSWt/IY9+80rIcKjCj6JgJVdMDWHLsaxcK4PALkvMQGwl6p7kYOnmBr/zUtvj+wisER1XKHRCDAW5eGukeg6xR3jSC4LKvY1gHDDo478QIkA8P5aYzwhXqnGToO0w/0V8er6lhFWV5Cv7zITYfU0g==",
    "ak_bmsc": "95DA089A5C74354FC7CA982147AB72255C7BE1D8EA010000219695607599A812~pl/uMqOp3p/TL3Trc1etesR0dqQ5ZrJCOY/t7pgzxiFMBUAiZwxPf7FI+wgd3Muj78X5A71XiDMV7cJpmSaRqTwaqmQXteJzEHBKPaVDrpU1Y6W2pFq6IRQaXPbgf6m0XFxCIPxKKe8dN30U8D6VjfkaPnj7pllwKDanQczUq5itVxe+5lCig6mEtJZAui9FcIVhtiBN5bXWsBQL5/OVcXrmqFByyfOlQPFPsp2LEYcZeNmFIHFaF6XnOyJyJcX4y2",
    "akavpau_User_allowed": "1620416723~id=276b082be76f9dd430a4f56503c13be4",
    "bm_sv": "3425A4B26C5FBF6BC43BF3375CD27444~FckFUgNEfDLaZciLvhJixZNtw7wcWd4dtZHgXEbbRtG4mzHST0o/f1qEFtu8ENuVJD34cBjxv5NtxiGPIXpWYQAbaOmmxGOj9jNKvv03zEhi+zXh1+og2t5zBakFv092SwxCMfChfTFRXg6uY7xDcsBcFt+pj/y65e97/V38ISY=",
    "_abck": "3B3764C81A753BD0B05D2AFD6C79F44A~-1~YAAQZeF7XFYB1zR5AQAA8oxkSAXQyqXQ09WtBAJem2panp4Otrc62G0k+81OJLiOmKi7Nio4yJ/245XLP4rZFxgdTZd0XvcQDFNvqAQyc4A4DlPbIszdtP+sxrUZ56TPhLd4uJ6p3FtsjZUhmpphN7xgA0gX+OXfDYX/zFgbI7vwXNWXBLlOcoxZIbZfCdcZvR5Sp9N+Qz+qFOtJwcx6KUIg3ZHCjaEvy1ovcHVskH/Gm+826RTcpiu6/BV2l7hqOvzgA6Ez0Z0ySK9e3V/cSKtB2Crv+WKnpvBkZCXZZIx9BIFu+iuauNXiL3o98rFWrlGlmH8MvOpKhlZC/8937cgZwhrIy45QkXOPCYhffRJ60D4OqFW4SzmijYono4Te+jWHdAqOjvUfNSeMSk6aOg1fISw=~-1~-1~-1",
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

from whatsapp_api_client_python import API

bot = API.GreenAPI(
    "1103957775", "92dbb6ee76844a009ccf752afec40f2959592573d5b94e8ea9"
)


def send_info(text: str):
    response = bot.sending.sendMessage("79133783079@c.us", text)
    print(response.data)
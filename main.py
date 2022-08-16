import telebot
import requests
from bs4 import BeautifulSoup

bot = telebot.TeleBot('5470180373:AAGitG7EN1R6sQyTstg84lkyXnxMC3Y2XQY')


@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Привет, <b><u>{message.from_user.first_name}</u></b>. Если хочешь узнать погоду в Москве - напиши (Погода Москва)\nДанные обновляются автоматически прямо из гугла.'
    bot.send_message(message.chat.id, mess, parse_mode='html')


@bot.message_handler()
def get_user_text(message):
    if message.text == "Погода Москва":
        WEATHER_MOSCOW = 'https://www.google.com/search?q=google+%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0+%D0%B2+%D0%BC%D0%BE%D1%81%D0%BA%D0%B2%D0%B5'
        WEATHER_MOSCOW_TOM = 'https://www.google.com/search?q=%D0%9F%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0+%D0%B2+%D0%BC%D0%BE%D1%81%D0%BA%D0%B2%D0%B5+%D0%B7%D0%B0%D0%B2%D1%82%D1%80%D0%B0&sxsrf=ALiCzsbJIE0efvWZRG1aGe3om-J5HW53hg%3A1660642099032&ei=M2P7YvLKAZOWrwSmqKvYDw&ved=0ahUKEwiysKXzhcv5AhUTy4sKHSbUCvsQ4dUDCA0&uact=5&oq=%D0%9F%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0+%D0%B2+%D0%BC%D0%BE%D1%81%D0%BA%D0%B2%D0%B5+%D0%B7%D0%B0%D0%B2%D1%82%D1%80%D0%B0&gs_lcp=Cgdnd3Mtd2l6EAMyDAgjECcQnQIQRhCAAjIKCAAQgAQQhwIQFDIFCAAQgAQyBQgAEIAEMgUIABCABDIKCAAQgAQQhwIQFDIFCAAQgAQyBQgAEIAEMgUIABCABDIICAAQgAQQyQM6CggAEEcQsAMQyQM6BwgAEEcQsAM6BwgjECcQnQI6BAgjECc6BwgAEMkDEEM6EAguELEDEIMBEMcBENEDEEM6EAgAEIAEEIcCELEDEIMBEBQ6CwgAEIAEELEDEIMBOgcIIxDqAhAnOgQIABBDOgoIABCxAxCDARBDOggIABCxAxCDAToICAAQgAQQsQM6CAgAEIAEEIsDOg4IABCABBCxAxCDARCLAzoLCAAQgAQQsQMQiwNKBAhBGABKBAhGGABQ2AlY-TZgqThoBXABeAeAAf8DiAG5K5IBDDQuMTYuNC4xLjIuMZgBAKABAbABCsgBCLgBAsABAQ&sclient=gws-wiz'
        WEATHER_MOSCOW_3D = 'https://www.google.com/search?q=%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0+%D0%B2+%D0%BC%D0%BE%D1%81%D0%BA%D0%B2%D0%B5+%D0%BF%D0%BE%D1%81%D0%BB%D0%B5%D0%B7%D0%B0%D0%B2%D1%82%D1%80%D0%B0&sxsrf=ALiCzsZu4zwMUO8A5DqP_V9vDS3qF67-aw%3A1660643865082&ei=GWr7YsfHBJX7rgTPxoEo&oq=%D0%9F%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0+%D0%B2+%D0%BC%D0%BE%D1%81%D0%BA%D0%B2%D0%B5+%D0%BF%D0%BE%D1%81%D0%BB%D0%B5%D0%B7%D0%B0&gs_lcp=Cgdnd3Mtd2l6EAMYADIKCAAQgAQQRhCAAjIGCAAQHhAWMgYIABAeEBYyBggAEB4QFjoKCAAQRxCwAxDJAzoHCAAQRxCwAzoKCAAQgAQQhwIQFDoFCAAQgAQ6CAgAEB4QFhAKSgQIQRgASgQIRhgAUOMCWNoXYPgdaAFwAXgAgAFaiAHFBJIBATeYAQCgAQHIAQjAAQE&sclient=gws-wiz'
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:103.0) Gecko/20100101 Firefox/103.0'}
        full_page = requests.get(WEATHER_MOSCOW, headers=headers)
        full_page_tom = requests.get(WEATHER_MOSCOW_TOM, headers=headers)
        full_page_3d = requests.get(WEATHER_MOSCOW_3D, headers=headers)
        soup = BeautifulSoup(full_page.content, 'html.parser')
        soup_tom = BeautifulSoup(full_page_tom.content, 'html.parser')
        soup3d = BeautifulSoup(full_page_3d.content, 'html.parser')
        convert_msc_3d2 = soup3d.findAll("div", {"class": "wob_dcp"})
        convert_msc_tom2 = soup_tom.findAll("div", {"class": "wob_dcp"})
        convert_msc2 = soup.findAll("div", {"class": "wob_dcp"})
        convert_msc_3d = soup3d.findAll("span", {"class": "wob_t q8U8x"})
        convert_msc_tom = soup_tom.findAll("span", {"class": "wob_t q8U8x"})
        convert_msc = soup.findAll("span", {"class": "wob_t q8U8x"})

        bot.send_message(message.chat.id,
                         f"Сейчас в Москве: +" + convert_msc[0].text + " " + convert_msc2[0].text + "\nЗавтра: +" +
                         convert_msc_tom[0].text + " " + convert_msc_tom2[0].text + "\nПослезавтра: +" + convert_msc_3d[
                             0].text + " " + convert_msc_3d2[0].text, parse_mode="html")

    if message.text == "Погода Чехов":
        WEATHER_CHECKOV = 'https://www.google.com/search?q=google+%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0+%D0%B2+%D1%87%D0%B5%D1%85%D0%BE%D0%B2%D0%B5&sxsrf=ALiCzsZ-1F9b5AmQoYy9AD5dRJgHE6j4dA%3A1660640952208&ei=uF77YtCqDMjMrgTN-4XADQ&ved=0ahUKEwjQ5rjQgcv5AhVIposKHc19AdgQ4dUDCA0&uact=5&oq=google+%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0+%D0%B2+%D1%87%D0%B5%D1%85%D0%BE%D0%B2%D0%B5&gs_lcp=Cgdnd3Mtd2l6EAMyBggAEB4QFjoHCAAQRxCwAzoKCAAQRxCwAxDJAzoICAAQkgMQsAM6DAgjECcQnQIQRhCAAjoHCAAQyQMQQzoECAAQQzoFCAAQgAQ6CggAEIAEEIcCEBQ6CAgAEIAEEMkDOggIIRAeEBYQHUoECEEYAEoECEYYAFDnEVi-JWD3J2gCcAF4AIABmASIAe0MkgELMS40LjAuMS4wLjGYAQCgAQHIAQrAAQE&sclient=gws-wiz'
        WEATHER_CHECKOV_TOM = 'https://www.google.com/search?q=%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0+%D0%B2+%D1%87%D0%B5%D1%85%D0%BE%D0%B2%D0%B5+%D0%B7%D0%B0%D0%B2%D1%82%D1%80%D0%B0&sxsrf=ALiCzsaQXP5VWPVjAGr8Hl1DUUpKi1mUoA%3A1660641699926&ei=o2H7YsCaOKusrgSHqYGwCA&ved=0ahUKEwiA-P20hMv5AhUrlosKHYdUAIYQ4dUDCA0&uact=5&oq=%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0+%D0%B2+%D1%87%D0%B5%D1%85%D0%BE%D0%B2%D0%B5+%D0%B7%D0%B0%D0%B2%D1%82%D1%80%D0%B0&gs_lcp=Cgdnd3Mtd2l6EAMyBQgAEIAEMgUIABCABDIGCAAQHhAHMgoIABAeEA8QBxAFOgQIABBHOggIABAeEAgQBzoECAAQDUoECEEYAEoECEYYAFCTAVi_D2CsFGgAcAJ4AIABVIgBugOSAQE2mAEAoAEByAEIwAEB&sclient=gws-wiz'
        WEATHER_CHECKOV_3D = 'https://www.google.com/search?q=%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0+%D0%B2+%D1%87%D0%B5%D1%85%D0%BE%D0%B2%D0%B5+%D0%BF%D0%BE%D1%81%D0%BB%D0%B5%D0%B7%D0%B0%D0%B2%D1%82%D1%80%D0%B0&sxsrf=ALiCzsYRx6xTa1hv7rA5TBTS-oKPdy_1Uw%3A1660641861077&ei=RWL7Yq2hBK6orgTW45SYCw&oq=%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0+%D0%B2+%D1%87%D0%B5%D1%85%D0%BE%D0%B2%D0%B5+%D0%BF%D0%BE%D1%81%D0%BB&gs_lcp=Cgdnd3Mtd2l6EAMYADIFCCEQoAE6CggAEEcQsAMQyQM6BwgAEEcQsAM6BQgAEIAEOgkIABAeEMkDEBY6BggAEB4QFjoECCEQFUoECEEYAEoECEYYAFDABViPC2DJE2gBcAF4AIABeogBiQOSAQMyLjKYAQCgAQHIAQjAAQE&sclient=gws-wiz'
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:103.0) Gecko/20100101 Firefox/103.0'}
        full_page_ch = requests.get(WEATHER_CHECKOV, headers=headers)
        full_page_ch_tom = requests.get(WEATHER_CHECKOV_TOM, headers=headers)
        full_page_ch_3d = requests.get(WEATHER_CHECKOV_3D, headers=headers)
        soup_tom = BeautifulSoup(full_page_ch_tom.content, 'html.parser')
        soup_3d = BeautifulSoup(full_page_ch_3d.content, 'html.parser')
        soup = BeautifulSoup(full_page_ch.content, 'html.parser')
        convert_ch = soup.findAll("span", {"class": "wob_t q8U8x"})
        convert_ch2 = soup.findAll("div", {"class": "wob_dcp"})
        convert_ch_tom2 = soup_tom.findAll("div", {"class": "wob_dcp"})
        convert_ch_3d2 = soup_3d.findAll("div", {"class": "wob_dcp"})
        convert_ch_tom = soup_tom.findAll("span", {"class": "wob_t q8U8x"})
        convert_ch_3d = soup_3d.findAll("span", {"class": "wob_t q8U8x"})

        bot.send_message(message.chat.id,
                         f"Сейчас в Чехове: +" + convert_ch[0].text + " " + convert_ch2[0].text + '\nЗавтра: +' +
                         convert_ch_tom[0].text + " " + convert_ch_tom2[0].text + '\nПослезавтра: +' + convert_ch_3d[
                             0].text + " " + convert_ch_3d2[0].text, parse_mode="html")

bot.polling(none_stop=True)

import requests
from bs4 import BeautifulSoup
import smtplib
import time
# Give the Amazon URL of your desired product
URL='https://www.amazon.in/Test-Exclusive-608/dp/B07HGBMJT6/ref=sr_1_1?keywords=oneplus&qid=1562348359&s=gateway&smid=A35FCS7U51TK3C&sr=8-1'

headers={"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}

def check_price():
    page=requests.get(URL,headers=headers)

    soup=BeautifulSoup(page.content,'html.parser')

    print(soup.prettify())

    title=soup.find(id="productTitle").get_text()

    price=soup.find(id="priceblock_dealprice").get_text()
    converted_price=price[0:8]
    if(converted_price >'₹ 35,000'):  #Set price accordingly
        send_mail()
    else:
        print("Aukaat k bahar hai bhai!")
    
    print(converted_price)
    print(title.strip())

def send_mail():
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('*********@gmail.com','password****') #Your Email and Password with less secure apps or two step verification of ur id
    subject='Beta, maal sasta bik raha hai ,jaldi se khareedlo'
    body='Link ye raha https://www.amazon.in/Test-Exclusive-608/dp/B07HGBMJT6/ref=sr_1_1?keywords=oneplus&qid=1562348359&s=gateway&smid=A35FCS7U51TK3C&sr=8-1'

    msg=f"Subject:{subject}\n\n{body}"

    server.sendmail(
        'from@gmail.com',
        'to@gmail.com',
        msg
    )
    print('Maal sasta bik raha hai abhi, mail dekh linkwa wahi bheje hai!')
    server.quit()    


while(True):
    check_price()
    time.sleep(60*60*24)



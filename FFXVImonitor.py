import requests
from bs4 import BeautifulSoup
import smtplib
import email.message


Req = "https://store.playstation.com/pt-br/product/UP0082-PPSA10664_00-FF16SIEA00000002"

#Substituir o "browserA' pelo seu Browser agent > https://www.whatismybrowser.com/detect/what-is-my-user-agent/
headers = {'User-Agent': "browserA"}

store = requests.get(Req, headers=headers)

soup = BeautifulSoup(store.content, 'html.parser')

ff = soup.find('h1', class_ = 'psw-m-b-5').get_text()
valor = soup.find('span', class_= 'psw-l-line-left psw-l-line-wrap').get_text()

nvalor = valor[2:6]
nvalor = nvalor.replace(',','')
nvalor = float(nvalor)

def gomail():
    email_content = """ 
    Final Fantasy XVI acaba de entrar no valor desejado, aproveite! >>> 
    https://store.playstation.com/pt-br/product/UP0082-PPSA10664_00-FF16SIEA00000002
    """
    cont = email.message.Message()
    cont['Subject'] = 'FFXVI BARATINHO!'

    # Substitua o 'email' pelo seu email
    cont['From'] = 'email'

    # Substitua o 'email' pelo seu email
    cont['To'] = 'email'

    # Substitua 'pw' pela senha do seu email
    senha = 'pw'
    cont.add_header('Content-Type', 'text/html')
    cont.set_payload(email_content)

    # Substitua o "outlook.com" pelo dominio do seu email
    envio = smtplib.SMTP('smtp.outlook.com: 587')

    envio.ehlo()
    envio.starttls()
    envio.login(cont['From'], senha)
    envio.sendmail(cont['From'], [cont['To']], cont.as_string())
    envio.quit()


#200 reais é o valor máximo que eu pagaria por esse novo final fantasy, mas você pode substituir o "200" pelo valor que desejar :)
if (nvalor < 200):
    gomail()

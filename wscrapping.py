import requests
from bs4 import BeautifulSoup
import smtplib
import email.message


Req = "https://www.kabum.com.br/produto/506014/processador-intel-core-i9-14900k-14-geracao-3-6-ghz-6-0-ghz-turbo-cache-36mb-intel-lga1700-bx8071514900k"

# altere o "browserAgent" pelo seu Browser agent > https://www.whatismybrowser.com/detect/what-is-my-user-agent/
headers = {'User-Agent': 'browserAgent'}

store = requests.get(Req, headers=headers)
soup = BeautifulSoup(store.content, 'html.parser')
i9 = soup.find('h4', class_ = 'sc-5492faee-2 hAMMrD finalPrice').get_text()

valor = i9[2:8]
valor = float(valor)

def gomail():
    email_content = """ 
    Seu produto acaba de entrar no valor desejado, aproveite! >>> 
    https://www.kabum.com.br/produto/506014/processador-intel-core-i9-14900k-14-geracao-3-6-ghz-6-0-ghz-turbo-cache-36mb-intel-lga1700-bx8071514900k
    """
    cont = email.message.Message()
    cont['Subject'] = 'SEU PRODUTO BARATINHO!'

    # altere o exemplo para o seu email
    cont['From'] = 'email@exemplo.com'
    cont['To'] = 'email@exemplo.com'

    # altere para senha do seu email
    senha = 'sua senha'
    cont.add_header('Content-Type', 'text/html')
    cont.set_payload(email_content)

    # altere o "outlook.com" pelo dominio e "587" pela porta do seu email
    envio = smtplib.SMTP('smtp.outlook.com: 587')

    envio.ehlo()
    envio.starttls()
    envio.login(cont['From'], senha)
    envio.sendmail(cont['From'], [cont['To']], cont.as_string())
    envio.quit()

    print('Email enviado com sucesso')

if (valor < 2.500): # altere para o valor desejado
    gomail()

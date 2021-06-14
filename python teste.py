import pyautogui
#Pyautogui é um repositório para tirar e salvar prints no pyhton
import datetime
import pyautogui
import time
import os
from selenium import webdriver
nomeArquivo = datetime.datetime.now().strftime('%Y-%M-%d_%H%M%S'+'.png')
#loop para ficar tirando foto da tela de 10 em 10 segudos.
while True:
    foto = pyautogui.screenshot() #tira o print
    foto.save('C://Users/Douglas/Desktop/TestePython' + nomeArquivo) #salva na pasta indicada.
    time.sleep(2) #atraso de 2 segundos entre uma screenshot e outra
class Testecase(unittest.Testcase)
@classmethod
def setUp(self):
    #A partir desse momento criaremos um e-mail falso para receber a confirmação de cadastro
    self.driver = webdriver.Chrome('/desktop/drivers/chromedriver')
    self.driver.get(os.getenv'https://emailfake.com')
    self.driver.maximize_window()
    self.password = '123456'
def temp_mail_base(self, email: str = None):
    self.email_driver =
webdriver.Chrome('/desktop/drivers/chromedriver') 
url = "https://emailfake.com/"

        if email is not None:
            spl = self.email.split('@')
            url += spl[1] + '/' + spl[0]

        self.email_driver.get(url)

        self.email_driver.maximize_window()

        self.email  = self.email_driver.find_element_by_id("email_ch_text").text
    def end_mail_base(self):

        WebDriverWait(self.email_driver, 240).until(
            EC.presence_of_element_located((By.XPATH, "//*[contains(text(),'nao-responda@dominio.com')]"))
        ).click()
#Aqui começamos de fato o caso de teste        
import TestCase
class T01_RegisterTest(TestCase):

self.driver.get('https://www.natura.com.br/cadastre-se')

    def setUp(self) -> None:
        super().setUp()

    def test_01_register_user(self):

        #AQUI ABRIMOS O emailfake.com, e captamos o email salvando no atributo self.email
        self.temp_mail_base()

        self.username_input = self.driver.find_element_by_name('//*[@id="root"]/div/div[2]/div[1]/div/div/div[3]/form/div[1]/div/input')
#Inserindo nome
        self.username_input.send_keys('Douglas')

        self.username_input = self.driver.find_element_by_name('//*[@id="root"]/div/div[2]/div[1]/div/div/div[3]/form/div[2]/div/input')
#Inserindo sobrenome
        self.username_input.send_keys('Roy')

        self.email_input = self.driver.find_element_by_name('//*[@id="root"]/div/div[2]/div[1]/div/div/div[3]/form/div[3]/div/input')

        self.email_input.send_keys(self.email)

        self.password_input = self.driver.find_element_by_name('//*[@id="root"]/div/div[2]/div[1]/div/div/div[3]/form/div[4]/div[1]/div/div/input')

        self.password_input.send_keys(self.password)

        self.confirm_password_input = self.driver.find_element_by_name('//*[@id="root"]/div/div[2]/div[1]/div/div/div[3]/form/div[4]/div[2]/div/div/input')

        self.confirm_password_input.send_keys(self.password)

        self.cpf_input = self.driver.find_element_by_name('//*[@id="root"]/div/div[2]/div[1]/div/div/div[3]/form/div[5]/div/input')

        self.cpf_input.send_keys("45698714886")

        self.rg_input = self.driver.find_element_by_name('//*[@id="root"]/div/div[2]/div[1]/div/div/div[3]/form/div[6]/div/input')

        self.rg_input.send_keys('504488673')

        self.nasc_input = self.driver.find_element_by_name('//*[@id="root"]/div/div[2]/div[1]/div/div/div[3]/form/div[7]/div/input')

        self.nasc_input.send_keys('03/11/1996')

        #click abaixo refere-se ao gênero necessário para cadastro
        self.click = self.driver.find_element_by_name('//*[@id="root"]/div/div[2]/div[1]/div/div/div[3]/form/fieldset[1]')

        self.ddd_input = self.driver.find_element_by_name('//*[@id="root"]/div/div[2]/div[1]/div/div/div[3]/form/fieldset[2]/div/div[1]/div/input')
        
        self.ddd_input.send_keys('11')

        self.ddd_input = self.driver.find_element_by_name('//*[@id="root"]/div/div[2]/div[1]/div/div/div[3]/form/fieldset[2]/div/div[2]/div/input')
        
        self.ddd_input.send_keys('964451167')
        
        self.click = self.driver.find_element_by_name('//*[@id="root"]/div/div[2]/div[1]/div/div/div[3]/form/div[11]/label/span[1]/svg')

        self.driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[1]/div/div/div[3]/form/div[12]/button[2]').click()

        WebDriverWait(self.driver, 10).until(
             for (int second = 0;; second++) {
            if (second >= 65) {
                fail("timeout");
            }
            try {
                if ("Cadastrado com sucesso.".equals(driver.findElement(By.cssSelector(".popUp.tabela")).getText())) {
                    System.out.println("Cadastro foi inserido com inserido com sucesso");
                    break;
                }
            } catch (Exception e) {
            }
        ).click()
# Aqui estamos aguardando por até 240 segundos que algum elemento no'driver' do emailfake.com tenha o valor do email que envia a confirmação.
        WebDriverWait(self.email_driver, 240).until(
            EC.presence_of_element_located((By.XPATH, "//*[contains(text(),'nao-responda@dominio.com'')]"))
        ).click()
        #aqui iremos clicar no primeiro link da pagina dentro da tabela de email do emailfake.com, o emai lé temporário, deverá sempre ser o unico email recebido até o momento
        WebDriverWait(self.email_driver, 60).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="email-table"]/div[2]/div[4]/div[3]/div/div[2]/a'))
        ).click()

        #salvamos o email utilizado em um json para sabermos o email tanto para logar novamente, como para testar outros recursos como alteração de senha.
        file = open('/tests/files/email.json','w+')
        json.dump({'email':self.email}, file)
        file.close()
                                                                
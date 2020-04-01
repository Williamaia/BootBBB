from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import re

repeat = 20*'='
class BotBBB:
    def __init__(self):
        #print('{} INSTANCIANDO CLASSE {}'.format(repeat, repeat))
        options = Options()
        options.headless = True
        self.escolhido = None
        self.mensagemLogin = ""
        self.browser = webdriver.Firefox(options=options)

    def getTitulo(self):
        self.titulo = self.browser.find_element_by_xpath("//head/title").get_attribute('textContent') 

    def getParticipantes(self, participante:str):
        print('{} ENCONTRANDO PARTICIPANTES {}'.format(repeat, repeat))
        if (self.escolhido is None) or not self.escolhido.text == participante:
            elements = self.browser.find_elements_by_xpath("//div[contains(text(), '{}')]".format(participante))
            if not elements:
                print("Não foi possivel encontrar o participante '{}'".format(participante))
            else:
                print('Participante encontrado, pronto para votação')
                print(elements[1].text)
                self.escolhido = elements[1]
           

    def votar(self, quant_votos:int):
        if not self.escolhido:
            print('Não é possivel votar, nenhum participante escolhido')
        else:
            print(self.escolhido.text)
            self.escolhido.click()
            self.browser.save_screenshot('screenshot/votando-1.png')

    def fazerLogin(self, email:str, senha: str):
        print('{} REALIZANDO LOGIN {}'.format(repeat, repeat))
        self.browser.get('https://minhaconta.globo.com/')
        self.browser.implicitly_wait(10)
        self.browser.save_screenshot('screenshot/login-1.png')
        self.browser.find_element_by_id('login').send_keys(email)
        self.browser.find_element_by_id('password').send_keys(senha)
        self.browser.save_screenshot('screenshot/login-2.png')
        self.browser.find_elements_by_xpath("//button[@class='button ng-scope']")[0].click()
        self.browser.implicitly_wait(2)
        self.mensagemLogin = self.browser.find_elements_by_xpath("//span[@class='error ng-binding']")[0].text
        if not self.mensagemLogin:
            self.mensagemLogin = "Login realizado com sucesso"
            return True
        else:
            self.browser.save_screenshot('screenshot/login-3-error.png')
            return False

    def fechar(self):
        print('{} FECHANDO {}'.format(repeat, repeat))
        self.browser.quit()


if __name__ == "__main__":
    URLDefault = 'https://gshow.globo.com/realities/bbb/bbb20/votacao/paredao-bbb20-quem-voce-quer-eliminar-felipe-manu-ou-mari-a9f49f90-84e2-4c12-a9af-b262e2dd5be4.ghtml'
    emailDefault = 'teste@teste.com'
    senhaDefault = 'BBB@2020'
    participanteDefault = ""
    quantidadeVotosDefault = 1
    logado = False
    podeVotar = True

    #URLDefault = input('Insira a url: ') or URLDefault
    bot = BotBBB()
    
    while(not logado):
        email = input('Insira um email({}): '.format(emailDefault)) or emailDefault
        senha = input('Insira uma senha({}): '.format(senhaDefault)) or senhaDefault
        logado = bot.fazerLogin(email, senha)
        print(bot.mensagemLogin)

    bot.browser.get(URLDefault)
    bot.browser.implicitly_wait(10)
    bot.getTitulo()
    print(bot.titulo)
    bot.browser.save_screenshot('screenshot/home-1.png')
    nomes = bot.titulo.split('?')[1]
    nome = 'felipe'
    nome = nome.lower().capitalize()
    print(nome)
    if not nome in nomes:
        print('Informe um participante valido')
    else:
        bot.getParticipantes(nome)
    while(not podeVotar):
        participante = input('Em quem deseja votar({}): '.format(nomes)) or participanteDefault
        participante = participante.lower().capitalize()
        quantidadeVotos = int(input('Informe a quantidade de votos({}): '.format(quantidadeVotosDefault)) or quantidadeVotosDefault)
        if not participante in nomes:
            print('Informe um participante valido')
            podeVotar = False
        else:
            podeVotar = True

        if not (quantidadeVotos > 0 and quantidadeVotos <= 100):
            print('A Quantidade de votos tem que ser entre 0 e 101')
            podeVotar = False
        else:
            podeVotar = True
        if podeVotar:
            bot.getParticipantes(participante)
            bot.votar(quantidadeVotos)
    
    bot.fechar()
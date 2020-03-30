from selenium import webdriver
from selenium.webdriver.firefox.options import Options

class BotBBB:
    def __init__(self,URL:str):
        self.URL = URL
        options = Options()
        options.headless = True
        self.browser = webdriver.Firefox(options=options)
        self.browser.get(URL)    

    def getTitle(self):
        return self.browser.title

    def getParticipantes(self):
        repeat = 20*'='
        print('{} ENCONTRANDO PARTICIPANTES {}'.format(repeat, repeat))
        elements = self.browser.find_elements_by_class_name('_3l2BjojXxJ4MNadPvFe7Tk')
        print(self.browser.title)
        print(len(elements))
        for elem in elements:
            print(type(elem))
    
    def quit(self):
        self.browser.quit()


if __name__ == "__main__":
    URL = 'https://gshow.globo.com/realities/bbb/bbb20/votacao/paredao-bbb20-quem-voce-quer-eliminar-felipe-manu-ou-mari-a9f49f90-84e2-4c12-a9af-b262e2dd5be4.ghtml'
    bot = BotBBB(URL)
    bot.getParticipantes()
    print(bot.getTitle())
    
    bot.quit()
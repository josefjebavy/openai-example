# imports is self describing
import os
from io import StringIO
import openai
from IPython.display import display, HTML
from dotenv import load_dotenv

#links: 
#https://github.com/openai/openai-python
#genereate  api key and pay
#https://platform.openai.com/account/usage

#web page for test conection via API
#https://www.chatwithgpt.ai/


#there exist diferent languages models and configurations

#models a prices
#https://platform.openai.com/docs/deprecations




# get the OPENAI_API_KEY from the environment
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

openai.api_key = OPENAI_API_KEY


def opendata(filename):
    try:
        with open('data/input/'+filename+'.txt', 'r') as soubor:
            obsah = soubor.read()  # Načtení obsahu souboru do proměnné
            print( "----vstup---"+filename+"-----")  # Vypsání obsahu souboru
            print(obsah)  # Vypsání obsahu souboru
            return obsah
    except FileNotFoundError:
        print("Soubor nenalezen.")
    except Exception as e:
        print(f"Nastala chyba: {e}")




class TextFile:
    def __init__(self, nazev_souboru):
        self.nazev_souboru = nazev_souboru
        self.soubor = None

    def openfile(self, rezim='r'):
        try:
            self.soubor = open(self.nazev_souboru, rezim)
            print(f"Soubor {self.nazev_souboru} byl úspěšně otevřen v režimu '{rezim}'.")
        except FileNotFoundError:
            print("Soubor nenalezen.")
        except Exception as e:
            print(f"Nastala chyba při otevírání souboru: {e}")

    def filewrite(self, text, title):
        if self.soubor:
            try:
                self.soubor.write(title+"\n")

                self.soubor.write(text)
                print("Text byl úspěšně zapsán do souboru.")
            except Exception as e:
                print(f"Nastala chyba při zápisu do souboru: {e}")
        else:
            print("Soubor není otevřen. Nelze provést zápis.")

    def fileclose(self):
        if self.soubor:
            try:
                self.soubor.close()
                print(f"Soubor {self.nazev_souboru} byl úspěšně uzavřen.")
            except Exception as e:
                print(f"Nastala chyba při uzavírání souboru: {e}")
        else:
            print("Soubor není otevřen. Nelze provést uzavření.")




def convertfile(filename, temperature, title):
    data=opendata(filename)

    command=" Informace preformuluj tak, aby to bylo srozumitelne pro nelekare. " \
           " Latinske terminy a zkratky rozepis pro nelekare. Nepis žádný uvod ani zaver.  Vstupni  text: "

    soubor = TextFile('data/output/' + filename + '.txt')
    soubor.openfile('w')  # Otevření souboru pro zápis

    data=getdata(command,data,temperature)
    print("-- vystup --- "+filename+" --")

    print(data)
    soubor.filewrite(data, title)  # Zápis do souboru
    soubor.fileclose()  # Uzavření souboruext)

def getdata(prikaz, data,temperature):
    prompt=prikaz+" ``` "+data+"```"
    model="gpt-3.5-turbo"

    response = openai.ChatCompletion.create(
        model=model,  # Můžete použít jiný model podle vašich preferencí
                temperature=temperature,  # Nastavte teplotu pro kreativitu odpovědí
                max_tokens=500,  # Nastavte maximální počet tokenů v odpovědi
        messages=[
            {"role": "system", "content": "Ty: jak vam mohu pomoci paciente?"},
            {"role": "user", "content": prompt}
        ]
    )
    # Získat odpověď z modelu
    nova_odpoved = response.choices[0].message['content']
    return nova_odpoved


def run():

    #convertfile("diagnozy-firstline",0.6,"")
    #convertfile("doporucenaterapie",0.4,"")
    #convertfile("duvodhospitalizace",0.8,"")
    convertfile("prubehhospitalizace", 0.7, "")
    #convertfile("objektivnepriprijmu",0.7,"")



def main():
    print("start...")
    run()

if __name__ == "__main__":
    main()

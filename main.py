import requests
import csv
import time

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = 'https://maisesports.com.br/campeonatos/worlds-2023-mundial-lol-onde-assitir-tabela-jogos-horario/resultados/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 OPR/103.0.0.0'}
resp = requests.get(url, headers = headers)
soup = BeautifulSoup(resp.text, 'html.parser')

driver = webdriver.Chrome()
driver.get(url)

div = driver.find_element(By.CLASS_NAME, 'sc-b2541fc2-4.elaPVl')
partidas_links = div.find_elements(By.TAG_NAME, 'a')

urls = []
for link in partidas_links:
    href = link.get_attribute('href')
    urls.append(href)

############################################ jogos

def el_clicavel(driver, xpath):
    return WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, xpath))
    )

def el_presente(driver, xpath):
    return WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, xpath))
    )

############################################ csv file

with open ('worlds_23.csv', mode='w', newline='') as csvfile:
    fields = ['jogo', 'time', 'torre', 'inibidor', 'barao', 'dragao', 'arauto', 'ama', 'ouro', 'adversario', 'lado/status']
    writer = csv.DictWriter(csvfile, fieldnames = fields)
        
    writer.writeheader()

    ############################################ info

    for url in urls:
        driver.get(url)
        
        try: ### jogo 1    

            # time azul
            time_a = el_presente(driver, '//*[@id="__next"]/div[5]/div[1]/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/span').text
            torre_a = el_presente(driver, '//*[@id="__next"]/div[5]/div[1]/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div/div[1]/span').text
            inib_a = el_presente(driver, '//*[@id="__next"]/div[5]/div[1]/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div/div[2]/span').text
            barao_a = el_presente(driver, '//*[@id="__next"]/div[5]/div[1]/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div/div[3]/span').text
            drag_a = el_presente(driver, '//*[@id="__next"]/div[5]/div[1]/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div/div[4]/span').text
            arauto_a = el_presente(driver, '//*[@id="__next"]/div[5]/div[1]/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div/div[5]/span').text
            ama_a = el_presente(driver, '//*[@id="__next"]/div[5]/div[1]/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[2]/div[4]/div/div[1]/div[1]/div[1]/span[2]').text
            ouro_a = el_presente(driver, '//*[@id="__next"]/div[5]/div[1]/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[2]/div[4]/div/div[1]/div[1]/div[2]/span[2]').text
            lado_a = el_presente(driver, '//*[@id="__next"]/div[5]/div[1]/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[2]/div[6]/div[1]/p[1]').text
            adv_a = el_presente(driver, '//*[@id="__next"]/div[5]/div[1]/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[2]/div[1]/div[3]/span').text
            # time vermelho
            time_v = el_presente(driver, '//*[@id="__next"]/div[5]/div[1]/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[2]/div[1]/div[3]/span').text
            torre_v = el_presente(driver, '//*[@id="__next"]/div[5]/div[1]/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[2]/div[2]/div[2]/div[2]/div/div[1]/span').text
            inib_v = el_presente(driver, '//*[@id="__next"]/div[5]/div[1]/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[2]/div[2]/div[2]/div[2]/div/div[2]/span').text
            barao_v = el_presente(driver, '//*[@id="__next"]/div[5]/div[1]/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[2]/div[2]/div[2]/div[2]/div/div[3]/span').text
            drag_v = el_presente(driver, '//*[@id="__next"]/div[5]/div[1]/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[2]/div[2]/div[2]/div[2]/div/div[4]/span').text
            arauto_v = el_presente(driver, '//*[@id="__next"]/div[5]/div[1]/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[2]/div[2]/div[2]/div[2]/div/div[5]/span').text
            ama_v = el_presente(driver, '//*[@id="__next"]/div[5]/div[1]/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[2]/div[4]/div/div[1]/div[3]/div[1]/span[2]').text
            ouro_v = el_presente(driver, '//*[@id="__next"]/div[5]/div[1]/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[2]/div[4]/div/div[1]/div[3]/div[2]/span[2]').text
            lado_v = el_presente(driver, '//*[@id="__next"]/div[5]/div[1]/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[2]/div[8]/div[1]/p[1]').text
            adv_v = el_presente(driver, '//*[@id="__next"]/div[5]/div[1]/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/span').text
            # numero e tempo do jogo
            tempo = el_presente(driver, '//*[@id="__next"]/div[5]/div[1]/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[2]/div[1]/span'). text
            njogo = 'Jogo 1'

            info_a1 = {'time': time_a,
                'torre': torre_a,
                'inibidor': inib_a,
                'barao': barao_a,
                'dragao': drag_a,
                'arauto': arauto_a,
                'ama': ama_a,
                'lado/status': lado_a,
                'adversario': adv_a,
                'ouro': ouro_a,
                'jogo': njogo,
                'tempo': tempo
                }
            info_v1 = {'time': time_v,
                'torre': torre_v,
                'inibidor': inib_v,
                'barao': barao_v,
                'dragao': drag_v,
                'arauto': arauto_v,
                'ama': ama_v,
                'lado/status': lado_v,
                'adversario': adv_v,
                'ouro': ouro_v,
                'jogo': njogo,
                'tempo': tempo
                }

            writer.writerow(info_a1)
            writer.writerow(info_v1)

            time.sleep(2)

        except Exception as e:
            print(f"Erro na primeira parte: {e}")

        try: ### jogo 2    

            bottom = el_clicavel(driver, '//*[@id="__next"]/div[5]/div[1]/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[1]/div[2]')
            bottom.click()

            # time azul
            time_a = el_presente(driver, '//*[@id="__next"]/div[5]/div[1]/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/span').text
            torre_a = el_presente(driver, '//*[@id="__next"]/div[5]/div[1]/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div/div[1]/span').text
            inib_a = el_presente(driver, '//*[@id="__next"]/div[5]/div[1]/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div/div[2]/span').text
            barao_a = el_presente(driver, '//*[@id="__next"]/div[5]/div[1]/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div/div[3]/span').text
            drag_a = el_presente(driver, '//*[@id="__next"]/div[5]/div[1]/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div/div[4]/span').text
            arauto_a = el_presente(driver, '//*[@id="__next"]/div[5]/div[1]/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div/div[5]/span').text
            ama_a = el_presente(driver, '//*[@id="__next"]/div[5]/div[1]/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[2]/div[4]/div/div[1]/div[1]/div[1]/span[2]').text
            ouro_a = el_presente(driver, '//*[@id="__next"]/div[5]/div[1]/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[2]/div[4]/div/div[1]/div[1]/div[2]/span[2]').text
            lado_a = el_presente(driver, '//*[@id="__next"]/div[5]/div[1]/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[2]/div[6]/div[1]/p[1]').text
            adv_a = el_presente(driver, '//*[@id="__next"]/div[5]/div[1]/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[2]/div[1]/div[3]/span').text
            # time vermelho
            time_v = el_presente(driver, '//*[@id="__next"]/div[5]/div[1]/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[2]/div[1]/div[3]/span').text
            torre_v = el_presente(driver, '//*[@id="__next"]/div[5]/div[1]/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[2]/div[2]/div[2]/div[2]/div/div[1]/span').text
            inib_v = el_presente(driver, '//*[@id="__next"]/div[5]/div[1]/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[2]/div[2]/div[2]/div[2]/div/div[2]/span').text
            barao_v = el_presente(driver, '//*[@id="__next"]/div[5]/div[1]/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[2]/div[2]/div[2]/div[2]/div/div[3]/span').text
            drag_v = el_presente(driver, '//*[@id="__next"]/div[5]/div[1]/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[2]/div[2]/div[2]/div[2]/div/div[4]/span').text
            arauto_v = el_presente(driver, '//*[@id="__next"]/div[5]/div[1]/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[2]/div[2]/div[2]/div[2]/div/div[5]/span').text
            ama_v = el_presente(driver, '//*[@id="__next"]/div[5]/div[1]/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[2]/div[4]/div/div[1]/div[3]/div[1]/span[2]').text
            ouro_v = el_presente(driver, '//*[@id="__next"]/div[5]/div[1]/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[2]/div[4]/div/div[1]/div[3]/div[2]/span[2]').text
            lado_v = el_presente(driver, '//*[@id="__next"]/div[5]/div[1]/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[2]/div[8]/div[1]/p[1]').text
            adv_v = el_presente(driver, '//*[@id="__next"]/div[5]/div[1]/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/span').text
            # numero e tempo do jogo
            tempo = el_presente(driver, '//*[@id="__next"]/div[5]/div[1]/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[2]/div[1]/span'). text
            njogo = 'Jogo 2'

            info_a2 = {'time': time_a,
                'torre': torre_a,
                'inibidor': inib_a,
                'barao': barao_a,
                'dragao': drag_a,
                'arauto': arauto_a,
                'ama': ama_a,
                'lado/status': lado_a,
                'adversario': adv_a,
                'ouro': ouro_a,
                'jogo': njogo,
                'tempo': tempo
                }
            info_v2 = {'time': time_v,
                'torre': torre_v,
                'inibidor': inib_v,
                'barao': barao_v,
                'dragao': drag_v,
                'arauto': arauto_v,
                'ama': ama_v,
                'lado/status': lado_v,
                'adversario': adv_v,
                'ouro': ouro_v,
                'jogo': njogo,
                'tempo': tempo
                }

            writer.writerow(info_a2)
            writer.writerow(info_v2)

            time.sleep(2)

        except Exception as e:
            print(f"Erro na segunda parte: {e}")

        try: ### jogo 3    

            bottom = el_clicavel(driver, '//*[@id="__next"]/div[5]/div[1]/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[1]/div[3]')
            bottom.click()

            # time azul
            time_a = el_presente(driver, '//*[@id="__next"]/div[5]/div[1]/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/span').text
            torre_a = el_presente(driver, '//*[@id="__next"]/div[5]/div[1]/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div/div[1]/span').text
            inib_a = el_presente(driver, '//*[@id="__next"]/div[5]/div[1]/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div/div[2]/span').text
            barao_a = el_presente(driver, '//*[@id="__next"]/div[5]/div[1]/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div/div[3]/span').text
            drag_a = el_presente(driver, '//*[@id="__next"]/div[5]/div[1]/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div/div[4]/span').text
            arauto_a = el_presente(driver, '//*[@id="__next"]/div[5]/div[1]/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div/div[5]/span').text
            ama_a = el_presente(driver, '//*[@id="__next"]/div[5]/div[1]/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[2]/div[4]/div/div[1]/div[1]/div[1]/span[2]').text
            ouro_a = el_presente(driver, '//*[@id="__next"]/div[5]/div[1]/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[2]/div[4]/div/div[1]/div[1]/div[2]/span[2]').text
            lado_a = el_presente(driver, '//*[@id="__next"]/div[5]/div[1]/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[2]/div[6]/div[1]/p[1]').text
            adv_a = el_presente(driver, '//*[@id="__next"]/div[5]/div[1]/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[2]/div[1]/div[3]/span').text
            # time vermelho
            time_v = el_presente(driver, '//*[@id="__next"]/div[5]/div[1]/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[2]/div[1]/div[3]/span').text
            torre_v = el_presente(driver, '//*[@id="__next"]/div[5]/div[1]/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[2]/div[2]/div[2]/div[2]/div/div[1]/span').text
            inib_v = el_presente(driver, '//*[@id="__next"]/div[5]/div[1]/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[2]/div[2]/div[2]/div[2]/div/div[2]/span').text
            barao_v = el_presente(driver, '//*[@id="__next"]/div[5]/div[1]/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[2]/div[2]/div[2]/div[2]/div/div[3]/span').text
            drag_v = el_presente(driver, '//*[@id="__next"]/div[5]/div[1]/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[2]/div[2]/div[2]/div[2]/div/div[4]/span').text
            arauto_v = el_presente(driver, '//*[@id="__next"]/div[5]/div[1]/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[2]/div[2]/div[2]/div[2]/div/div[5]/span').text
            ama_v = el_presente(driver, '//*[@id="__next"]/div[5]/div[1]/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[2]/div[4]/div/div[1]/div[3]/div[1]/span[2]').text
            ouro_v = el_presente(driver, '//*[@id="__next"]/div[5]/div[1]/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[2]/div[4]/div/div[1]/div[3]/div[2]/span[2]').text
            lado_v = el_presente(driver, '//*[@id="__next"]/div[5]/div[1]/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[2]/div[8]/div[1]/p[1]').text
            adv_v = el_presente(driver, '//*[@id="__next"]/div[5]/div[1]/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/span').text
            # numero e tempo do jogo
            tempo = el_presente(driver, '//*[@id="__next"]/div[5]/div[1]/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[2]/div[1]/span'). text
            njogo = 'Jogo 3'

            info_a3 = {'time': time_a,
                'torre': torre_a,
                'inibidor': inib_a,
                'barao': barao_a,
                'dragao': drag_a,
                'arauto': arauto_a,
                'ama': ama_a,
                'lado/status': lado_a,
                'adversario': adv_a,
                'ouro': ouro_a,
                'jogo': njogo,
                'tempo': tempo
                }
            info_v3 = {'time': time_v,
                'torre': torre_v,
                'inibidor': inib_v,
                'barao': barao_v,
                'dragao': drag_v,
                'arauto': arauto_v,
                'ama': ama_v,
                'lado/status': lado_v,
                'adversario': adv_v,
                'ouro': ouro_v,
                'jogo': njogo,
                'tempo': tempo
                }

            writer.writerow(info_a3)
            writer.writerow(info_v3)

            time.sleep(2)

        except Exception as e:
            print(f"Erro na terceira parte: {e}")

        try: ### jogo 4    

            bottom = el_clicavel(driver, '//*[@id="__next"]/div[5]/div[1]/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[1]/div[4]')
            bottom.click()

            # time azul
            time_a = el_presente(driver, '//*[@id="__next"]/div[5]/div[1]/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/span').text
            torre_a = el_presente(driver, '//*[@id="__next"]/div[5]/div[1]/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div/div[1]/span').text
            inib_a = el_presente(driver, '//*[@id="__next"]/div[5]/div[1]/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div/div[2]/span').text
            barao_a = el_presente(driver, '//*[@id="__next"]/div[5]/div[1]/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div/div[3]/span').text
            drag_a = el_presente(driver, '//*[@id="__next"]/div[5]/div[1]/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div/div[4]/span').text
            arauto_a = el_presente(driver, '//*[@id="__next"]/div[5]/div[1]/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div/div[5]/span').text
            ama_a = el_presente(driver, '//*[@id="__next"]/div[5]/div[1]/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[2]/div[4]/div/div[1]/div[1]/div[1]/span[2]').text
            ouro_a = el_presente(driver, '//*[@id="__next"]/div[5]/div[1]/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[2]/div[4]/div/div[1]/div[1]/div[2]/span[2]').text
            lado_a = el_presente(driver, '//*[@id="__next"]/div[5]/div[1]/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[2]/div[6]/div[1]/p[1]').text
            adv_a = el_presente(driver, '//*[@id="__next"]/div[5]/div[1]/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[2]/div[1]/div[3]/span').text
            # time vermelho
            time_v = el_presente(driver, '//*[@id="__next"]/div[5]/div[1]/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[2]/div[1]/div[3]/span').text
            torre_v = el_presente(driver, '//*[@id="__next"]/div[5]/div[1]/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[2]/div[2]/div[2]/div[2]/div/div[1]/span').text
            inib_v = el_presente(driver, '//*[@id="__next"]/div[5]/div[1]/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[2]/div[2]/div[2]/div[2]/div/div[2]/span').text
            barao_v = el_presente(driver, '//*[@id="__next"]/div[5]/div[1]/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[2]/div[2]/div[2]/div[2]/div/div[3]/span').text
            drag_v = el_presente(driver, '//*[@id="__next"]/div[5]/div[1]/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[2]/div[2]/div[2]/div[2]/div/div[4]/span').text
            arauto_v = el_presente(driver, '//*[@id="__next"]/div[5]/div[1]/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[2]/div[2]/div[2]/div[2]/div/div[5]/span').text
            ama_v = el_presente(driver, '//*[@id="__next"]/div[5]/div[1]/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[2]/div[4]/div/div[1]/div[3]/div[1]/span[2]').text
            ouro_v = el_presente(driver, '//*[@id="__next"]/div[5]/div[1]/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[2]/div[4]/div/div[1]/div[3]/div[2]/span[2]').text
            lado_v = el_presente(driver, '//*[@id="__next"]/div[5]/div[1]/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[2]/div[8]/div[1]/p[1]').text
            adv_v = el_presente(driver, '//*[@id="__next"]/div[5]/div[1]/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/span').text
            # numero e tempo do jogo
            tempo = el_presente(driver, '//*[@id="__next"]/div[5]/div[1]/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[2]/div[1]/span'). text
            njogo = 'Jogo 4'

            info_a4 = {'time': time_a,
                'torre': torre_a,
                'inibidor': inib_a,
                'barao': barao_a,
                'dragao': drag_a,
                'arauto': arauto_a,
                'ama': ama_a,
                'lado/status': lado_a,
                'adversario': adv_a,
                'ouro': ouro_a,
                'jogo': njogo,
                'tempo': tempo
                }
            info_v4 = {'time': time_v,
                'torre': torre_v,
                'inibidor': inib_v,
                'barao': barao_v,
                'dragao': drag_v,
                'arauto': arauto_v,
                'ama': ama_v,
                'lado/status': lado_v,
                'adversario': adv_v,
                'ouro': ouro_v,
                'jogo': njogo,
                'tempo': tempo
                }

            writer.writerow(info_a4)
            writer.writerow(info_v4)

            time.sleep(2)

        except Exception as e:
            print(f"Erro na quarta parte: {e}")

        try: ### jogo 5    

            bottom = el_clicavel(driver, '//*[@id="__next"]/div[5]/div[1]/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[1]/div[5]')
            bottom.click()

            # time azul
            time_a = el_presente(driver, '//*[@id="__next"]/div[5]/div[1]/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/span').text
            torre_a = el_presente(driver, '//*[@id="__next"]/div[5]/div[1]/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div/div[1]/span').text
            inib_a = el_presente(driver, '//*[@id="__next"]/div[5]/div[1]/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div/div[2]/span').text
            barao_a = el_presente(driver, '//*[@id="__next"]/div[5]/div[1]/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div/div[3]/span').text
            drag_a = el_presente(driver, '//*[@id="__next"]/div[5]/div[1]/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div/div[4]/span').text
            arauto_a = el_presente(driver, '//*[@id="__next"]/div[5]/div[1]/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div/div[5]/span').text
            ama_a = el_presente(driver, '//*[@id="__next"]/div[5]/div[1]/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[2]/div[4]/div/div[1]/div[1]/div[1]/span[2]').text
            ouro_a = el_presente(driver, '//*[@id="__next"]/div[5]/div[1]/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[2]/div[4]/div/div[1]/div[1]/div[2]/span[2]').text
            lado_a = el_presente(driver, '//*[@id="__next"]/div[5]/div[1]/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[2]/div[6]/div[1]/p[1]').text
            adv_a = el_presente(driver, '//*[@id="__next"]/div[5]/div[1]/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[2]/div[1]/div[3]/span').text

            # time vermelho
            time_v = el_presente(driver, '//*[@id="__next"]/div[5]/div[1]/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[2]/div[1]/div[3]/span').text
            torre_v = el_presente(driver, '//*[@id="__next"]/div[5]/div[1]/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[2]/div[2]/div[2]/div[2]/div/div[1]/span').text
            inib_v = el_presente(driver, '//*[@id="__next"]/div[5]/div[1]/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[2]/div[2]/div[2]/div[2]/div/div[2]/span').text
            barao_v = el_presente(driver, '//*[@id="__next"]/div[5]/div[1]/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[2]/div[2]/div[2]/div[2]/div/div[3]/span').text
            drag_v = el_presente(driver, '//*[@id="__next"]/div[5]/div[1]/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[2]/div[2]/div[2]/div[2]/div/div[4]/span').text
            arauto_v = el_presente(driver, '//*[@id="__next"]/div[5]/div[1]/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[2]/div[2]/div[2]/div[2]/div/div[5]/span').text
            ama_v = el_presente(driver, '//*[@id="__next"]/div[5]/div[1]/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[2]/div[4]/div/div[1]/div[3]/div[1]/span[2]').text
            ouro_v = el_presente(driver, '//*[@id="__next"]/div[5]/div[1]/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[2]/div[4]/div/div[1]/div[3]/div[2]/span[2]').text
            lado_v = el_presente(driver, '//*[@id="__next"]/div[5]/div[1]/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[2]/div[8]/div[1]/p[1]').text
            adv_v = el_presente(driver, '//*[@id="__next"]/div[5]/div[1]/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/span').text
            # numero e tempo do jogo
            tempo = el_presente(driver, '//*[@id="__next"]/div[5]/div[1]/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[2]/div[1]/span'). text
            njogo = 'Jogo 5'

            info_a5 = {'time': time_a,
                'torre': torre_a,
                'inibidor': inib_a,
                'barao': barao_a,
                'dragao': drag_a,
                'arauto': arauto_a,
                'ama': ama_a,
                'lado/status': lado_a,
                'adversario': adv_a,
                'ouro': ouro_a,
                'jogo': njogo,
                'tempo': tempo
                }
            info_v5 = {'time': time_v,
                'torre': torre_v,
                'inibidor': inib_v,
                'barao': barao_v,
                'dragao': drag_v,
                'arauto': arauto_v,
                'ama': ama_v,
                'lado/status': lado_v,
                'adversario': adv_v,
                'ouro': ouro_v,
                'jogo': njogo,
                'tempo': tempo
                }

            writer.writerow(info_a5)
            writer.writerow(info_v5)

            time.sleep(2)

        except Exception as e:
            print(f"Erro na quinta parte: {e}")

        finally:
            driver.quit()
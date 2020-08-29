from bs4 import BeautifulSoup
import requests
import csv
import re

# adresas='https://m.en.aruodas.lt/butu-nuoma/vilniuje/?change_region=1'

skaicius=2
# adresas2=f"https://m.en.aruodas.lt/butu-nuoma/vilniuje/puslapis/{skaicius}/?change_region=1"
listas=[]
while skaicius<30:
        adresas2 = f"https://m.en.aruodas.lt/butu-nuoma/vilniuje/puslapis/{skaicius}/?change_region=1"
        source = requests.get(adresas2).text
        soup = BeautifulSoup(source, 'html.parser')
        blokai = soup.find_all('li', class_='result-item-v3')

        with open("aruodas_rent2.csv", "a", encoding="UTF-8", newline="" ) as failas:
            csv_writer = csv.writer(failas)

            csv_writer.writerow(['Vieta', 'Kambariai', 'Kaina'])
            for blokas in blokai:
                try:
                    vieta = blokas.find('span', class_='item-address-v3').text.strip()
                    # pattern=re.compile((r'[A-Za-ząžčęėįšųūĄČĘĖĮŠŲŪŽ\w]+\,?\s?[A-Za-ząžčęėįšųūĄČĘĖĮŠŲŪŽ\w]+?\s?[A-Za-ząžčęėįšųūĄČĘĖĮŠŲŪŽ\w]+\s[a-z]+\.'))
                    # result=pattern.findall(vieta)
                    # vieta = result

                    kambariai = blokas.find('span', class_='item-description-v3').text.strip()
                    # pattern1 = re.compile(r'\d+\s[a-zA-ząčęėįšžųūĄŽČĘĖĮŠŲŪ\w]+\,\s\d+\,?\d+?\s[m]\D\,\s')
                    # result1 = pattern1.findall(kambariai)
                    # kambariai = result1

                    kaina = blokas.find('span', class_='item-price-main-v3').span.text.strip()
                    pattern2 = re.compile(r'\d+\s\D')
                    result2 = pattern2.findall(kaina)
                    kaina = result2

                    listas.append([vieta,kambariai,kaina])

                    csv_writer.writerow([vieta, kambariai, kaina])
                except:
                    print(skaicius)
                    pass
            print(f"dabartinis puslapis: {adresas2}")
            skaicius += 1
print(listas)
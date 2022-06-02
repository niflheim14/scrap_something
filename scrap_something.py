import requests
from lxml import html

r = requests.get('https://www.eluniversal.com.mx/', allow_redirects=True, verify=False, timeout=60, headers={"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:100.0) Gecko/20100101 Firefox/100.0"})
r.raise_for_status()

main_page = html.fromstring(r.content)

main_notes = main_page.xpath("//h2[normalize-space()='Principales']/../..//div[contains(@class, 'nota-') or @class='nota']")

for mn in main_notes:
    print('\033[1m' + mn.cssselect('h2[class*=titulo]>a')[0].text.strip().replace('\n', '') + '\033[0m')
    print('\r' + mn.cssselect('h2[class*=titulo]>a')[0].attrib['href'])
    print('\r' + mn.cssselect('p[class*=resumen]')[0].text.strip().replace('\n', ''))
    print('\r\r')

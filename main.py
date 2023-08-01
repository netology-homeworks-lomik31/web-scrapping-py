import requests, bs4, fake_headers
from pprint import pprint

headers_dict = fake_headers.Headers("chromium", "macos").generate()


main_html_data = requests.get("https://spb.hh.ru/search/vacancy?area=1&area=2&text=Python", headers=headers_dict).text
main_html = bs4.BeautifulSoup(main_html_data, "lxml")

vacances = main_html.find("div", {"data-qa": "vacancy-serp__results"})

vacances_list = vacances.find_all("div", class_="vacancy-serp-item-body__main-info")

# res = {}
# pprint(vacances_list)
# for i in vacances_list:
#     ""
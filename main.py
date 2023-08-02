import requests, bs4, fake_headers
from pprint import pprint

headers_dict = fake_headers.Headers("chromium", "macos").generate()


main_html_data = requests.get("https://spb.hh.ru/search/vacancy?area=1&area=2&text=Python", headers=headers_dict).text
main_html = bs4.BeautifulSoup(main_html_data, "lxml")

vacancies = main_html.find("div", {"data-qa": "vacancy-serp__results"})

vacancies_list = vacancies.find_all("div", class_="vacancy-serp-item-body__main-info")


res = []
# pprint(vacancies_list)
for i in vacancies_list:
    header = i.find("div").find("h3", {"data-qa": "bloko-header-3", "class": "bloko-header-section-3"})\
        .find("span", {"data-page-analytics-event": "vacancy_search_suitable_item"})\
        .find("a", class_="serp-item__title")
    title = header.text
    link = header["href"]

    company = i.find("div", class_="vacancy-serp-item__info")

    company_name = company.find("a", {"data-qa": "vacancy-serp__vacancy-employer"}).text
    company_location = company.find("div", {"data-qa": "vacancy-serp__vacancy-address"})\
        .text.split(",", 1)[0]

    salary = i.find("span", {"data-qa": "vacancy-serp__vacancy-compensation"})
    salary = salary.text.split("₽")[0] if salary else "Not stated"

    res.append({
        "title": title,
        "link": link,
        "company_name": company_name,
        "company_location": company_location,
        "salary": salary
    })
print(res)
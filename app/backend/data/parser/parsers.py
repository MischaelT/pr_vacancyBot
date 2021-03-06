import re

from backend.data.vacancy_data_manager import Vacancies_manager

from bs4 import BeautifulSoup

# TODO Implement getting data of vacancy creation


def parse_djinni_data(vacancy_manager: Vacancies_manager, content: str, basepoint: str, language: str, experience: str) -> None:  # noqa
    """
        Method parses vacancies from djinni.ua content

    Args:
        vacancy_manager (Vacancies_manager)
        content (str): site content
        basepoint (str): url basepoint
        language (str): language for writing to db
        experience (str): experience for writing to db
    """
    soup = BeautifulSoup(content, 'html.parser')
    vacancies = soup.find_all('li', class_='list-jobs__item')

    vacancies_list = []

    for vacancy in vacancies:

        title = delete_spaces(vacancy.find('div', class_="list-jobs__title").text.strip())
        info = delete_spaces(vacancy.find('div', class_='list-jobs__description').text.strip())
        link = basepoint + vacancy.find('a', class_="profile")['href']

        try:
            remote = vacancy.find('span', class_="icon icon-home_work").next_sibling.text.strip()
        except AttributeError:
            remote = ''

        try:
            cities = vacancy.find('nobr', class_="location-text").text.strip()
        except AttributeError:
            cities = remote

        data = {
                'title': title,
                'city': cities,
                'info': info,
                'link': link,
                'language': language,
                'experience': experience,
                'salary': ''
            }

        vacancies_list.append(data)

    vacancy_manager.push_pure_data(vacancies_data=vacancies_list)


def parse_dou_data(vacancy_manager: Vacancies_manager, content: str, language: str, experience: str) -> None:

    """
        Method parses vacancies from dou.ua content

    Args:
        vacancy_manager (Vacancies_manager)
        content (str): site content
        basepoint (str): url basepoint
        language (str): language for writing to db
        experience (str): experience for writing to db
    """

    soup = BeautifulSoup(content, 'html.parser')
    vacancies = soup.find_all('li', class_='l-vacancy')

    vacancies_list = []

    for vacancy in vacancies:

        title = vacancy.find('a', class_='vt').text.strip()
        info = vacancy.find('div', class_='sh-info').text.strip()
        city = vacancy.find('span', class_='cities').text.strip()
        link = vacancy.find('a', class_='vt')['href']

        data = {
                'title': title,
                'city': city,
                'info': info,
                'link': link,
                'language': language,
                'experience': experience,
                'salary': ''
                }

        vacancies_list.append(data)

    vacancy_manager.push_pure_data(vacancies_data=vacancies_list)


def delete_spaces(text: str):
    return re.sub(" +", " ", text)

# def parse_workUa_data(content, basepoint) -> None:

#     soup = BeautifulSoup(content, 'html.parser')
#     vacancies = soup.find_all('div', class_='card card-hover card-visited wordwrap job-link')

#     for vacancy in vacancies:

#         title = vacancy.find('h2').text.strip()
#         info = vacancy.find('p', class_='overflow text-muted add-top-sm cut-bottom').text.strip()
#         link = basepoint + vacancy.find('a', class_='no-decoration')['href']
#         # remote = vacancy.find('span', class_ = "icon icon-home_work").next_sibling.text.strip()
#         # parsed_info_salary = self.__parse_workUa_vacancy(link)

#         # info = parsed_info_salary['info']
#         # salary = parsed_info_salary['salary']
#         salary = ''
#         data = {'title': title, 'city': '', 'info': info, 'link': link, 'salary': salary}

#     return data

# async def parse_workUa_vacancy(self, link) -> dict:

#     response = requests.get(link, headers=self.headers)

#     response.raise_for_status()

#     soup = BeautifulSoup(response.text, 'html.parser')

#     result = {}

#     try:
#         info = soup.find('div', id='job-description').text
#     except AttributeError:
#         info = ''

#     result['info'] = info

#     try:
#         salary = soup.find('b', class_='text-black').text
#     except AttributeError:
#         salary = ''

#     result['salary'] = salary

#     return result

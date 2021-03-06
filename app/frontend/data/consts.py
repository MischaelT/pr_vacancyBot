from backend.data.db.choices import (ARCHITECT, CPLUSPLUS, INTERN, JAVA,
                                     JUNIOR, MIDDLE, PYTHON, SCALA, SENIOR)

MAIN_MENU = 1
GET_VACANCIES_MENU = 2
SETTINGS_MENU = 3
MY_SETTINGS = 4
SET_SETTINGS = 5

SETTINGS_MENU_LIST = ['My settings', 'Change settings', 'Back']

EXPERIENCES_LIST = {'0-1': INTERN, '1-2': JUNIOR, '2-4': MIDDLE, '4-6': SENIOR, '6+': ARCHITECT}
LANGUAGE_LIST = {'Python': PYTHON, 'Java': JAVA, 'C++': CPLUSPLUS, 'Scala': SCALA}
CITIES_LIST = ['Odessa', 'Kyiv', 'Kharkiv', 'Lviv']
SALARIES_LIST = ['0-1000', '1000-2000', '3000-4000', '4000+']


SAVE_BUTTON = 'Save'
BACK_BUTTON = 'Back'

# Проект 2. Анализ вакансий из HeadHunter

## Оглавление
[1. Описание проекта](https://github.com/Lev-Tegai/sf_data_science/tree/main/project_0#описание-проекта)\
[2. Задача](https://github.com/Lev-Tegai/sf_data_science/tree/main/project_0#задача)\
[3. Краткая информация о данных](https://github.com/Lev-Tegai/sf_data_science/tree/main/project_0#краткая-информация-о-данных)

### Описание проекта
Анализ данных для подбора вакансий для DS-cпециалистов

### Задача
1. Провести анализ в несколько этапов:
* предварительный анализ данных
* детальный анализ вакансий
* анализ работодателей
* предметный анализ
2. Сделать выводы по каждому этапу и по проекту в целом

**Что практикуем**
- Учимся создавать SQL запросы в python
- Учимся оформлять проект в GitHub

### Краткая информация о данных
Данные взяты из базы данных HeadHunter и представлены в виде 5 таблиц:

VACANCIES

Таблица хранит в себе данные по вакансиям и содержит следующие столбцы:

[Таблица VACANCIES](\vacancies.png)

Зарплатная вилка — это верхняя и нижняя граница оплаты труда в рублях (зарплаты в других валютах уже переведены в рубли). Соискателям она показывает, в каком диапазоне компания готова платить сотруднику на этой должности.


AREAS

Таблица-справочник, которая хранит код города и его название.

[Таблица AREAS](https://lms.skillfactory.ru/assets/courseware/v1/682c2306f3d46a25915a89d4ec7e16ed/asset-v1:SkillFactory+DSPR-2.0+14JULY2021+type@asset+block/SQL_pj2_2_3.png)


EMPLOYERS

Таблица-справочник со списком работодателей.

[Таблица EMPLOYERS](https://lms.skillfactory.ru/assets/courseware/v1/682c2306f3d46a25915a89d4ec7e16ed/asset-v1:SkillFactory+DSPR-2.0+14JULY2021+type@asset+block/SQL_pj2_2_4.png)


INDUSTRIES

Таблица-справочник вариантов сфер деятельности работодателей.

[Таблица INDUSTRIES](https://lms.skillfactory.ru/assets/courseware/v1/682c2306f3d46a25915a89d4ec7e16ed/asset-v1:SkillFactory+DSPR-2.0+14JULY2021+type@asset+block/SQL_pj2_2_5.png)

EMPLOYERS_INDUSTRIES

Дополнительная таблица, которая существует для организации связи между работодателями и сферами их деятельности.

Эта таблица нужна нам, поскольку у одного работодателя может быть несколько сфер деятельности (или работодатели могут вовсе не указать их). Для удобства анализа необходимо хранить запись по каждой сфере каждого работодателя в отдельной строке таблицы.

[Таблица EMPLOYERS_INDUSTRIES](https://lms.skillfactory.ru/assets/courseware/v1/682c2306f3d46a25915a89d4ec7e16ed/asset-v1:SkillFactory+DSPR-2.0+14JULY2021+type@asset+block/SQL_pj2_2_6.png)


:arrow_up:[к оглавлению](https://github.com/Lev-Tegai/sf_data_science/tree/main/project_0#оглавление)


Если информация по этому проекту покажется Вам интересной или полезной, я буду очень благодарен, если Вы отметите репозиторий и профиль ⭐️⭐️⭐️-дами
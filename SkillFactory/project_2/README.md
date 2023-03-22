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

<left> <img src = https://lms.skillfactory.ru/assets/courseware/v1/837cf6ff79f483e387a16c993634f3e4/asset-v1:SkillFactory+DSPR-2.0+14JULY2021+type@asset+block/SQL_pj2_2_2.png
alt="drawing" style="width:400px;">

Зарплатная вилка — это верхняя и нижняя граница оплаты труда в рублях (зарплаты в других валютах уже переведены в рубли). Соискателям она показывает, в каком диапазоне компания готова платить сотруднику на этой должности.


AREAS

Таблица-справочник, которая хранит код города и его название.

<left> <img src = https://lms.skillfactory.ru/assets/courseware/v1/837cf6ff79f483e387a16c993634f3e4/asset-v1:SkillFactory+DSPR-2.0+14JULY2021+type@asset+block/SQL_pj2_2_3.png
alt="drawing" style="width:400px;">


EMPLOYERS

Таблица-справочник со списком работодателей.

<left> <img src = https://lms.skillfactory.ru/assets/courseware/v1/837cf6ff79f483e387a16c993634f3e4/asset-v1:SkillFactory+DSPR-2.0+14JULY2021+type@asset+block/SQL_pj2_2_4.png
alt="drawing" style="width:400px;">


INDUSTRIES

Таблица-справочник вариантов сфер деятельности работодателей.

<left> <img src = https://lms.skillfactory.ru/assets/courseware/v1/837cf6ff79f483e387a16c993634f3e4/asset-v1:SkillFactory+DSPR-2.0+14JULY2021+type@asset+block/SQL_pj2_2_5.png
alt="drawing" style="width:400px;">


EMPLOYERS_INDUSTRIES

Дополнительная таблица, которая существует для организации связи между работодателями и сферами их деятельности.

Эта таблица нужна нам, поскольку у одного работодателя может быть несколько сфер деятельности (или работодатели могут вовсе не указать их). Для удобства анализа необходимо хранить запись по каждой сфере каждого работодателя в отдельной строке таблицы.

<left> <img src = https://lms.skillfactory.ru/assets/courseware/v1/837cf6ff79f483e387a16c993634f3e4/asset-v1:SkillFactory+DSPR-2.0+14JULY2021+type@asset+block/SQL_pj2_2_6.png
alt="drawing" style="width:400px;">


:arrow_up:[к оглавлению](https://github.com/Lev-Tegai/sf_data_science/tree/main/project_0#оглавление)


Если информация по этому проекту покажется Вам интересной или полезной, я буду очень благодарен, если Вы отметите репозиторий и профиль ⭐️⭐️⭐️-дами
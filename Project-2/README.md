# Проект 2. Анализ вакансий из HeadHunter

## Оглавление
[1. Описание проекта](https://github.com/Lev-Tegai/sf_data_science/tree/main/SkillFactory/project_2#%D0%BE%D0%BF%D0%B8%D1%81%D0%B0%D0%BD%D0%B8%D0%B5-%D0%BF%D1%80%D0%BE%D0%B5%D0%BA%D1%82%D0%B0)\
[2. Задача](https://github.com/Lev-Tegai/sf_data_science/tree/main/SkillFactory/project_2#%D0%B7%D0%B0%D0%B4%D0%B0%D1%87%D0%B0)\
[3. Краткая информация о данных](https://github.com/Lev-Tegai/sf_data_science/tree/main/SkillFactory/project_2#%D0%BA%D1%80%D0%B0%D1%82%D0%BA%D0%B0%D1%8F-%D0%B8%D0%BD%D1%84%D0%BE%D1%80%D0%BC%D0%B0%D1%86%D0%B8%D1%8F-%D0%BE-%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D1%85)

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
- Учимся анализировать данные


### Краткая информация о данных
Данные взяты из базы данных HeadHunter и представлены в виде 5 таблиц:

1. VACANCIES

Таблица хранит в себе данные по вакансиям и содержит следующие столбцы:

<left> <img src = https://lms.skillfactory.ru/assets/courseware/v1/837cf6ff79f483e387a16c993634f3e4/asset-v1:SkillFactory+DSPR-2.0+14JULY2021+type@asset+block/SQL_pj2_2_2.png
alt="drawing" style="width:400px;">

Зарплатная вилка — это верхняя и нижняя граница оплаты труда в рублях (зарплаты в других валютах уже переведены в рубли). Соискателям она показывает, в каком диапазоне компания готова платить сотруднику на этой должности.


2. AREAS

Таблица-справочник, которая хранит код города и его название.

<left> <img src = https://lms.skillfactory.ru/assets/courseware/v1/837cf6ff79f483e387a16c993634f3e4/asset-v1:SkillFactory+DSPR-2.0+14JULY2021+type@asset+block/SQL_pj2_2_3.png
alt="drawing" style="width:400px;">


3. EMPLOYERS

Таблица-справочник со списком работодателей.

<left> <img src = https://lms.skillfactory.ru/assets/courseware/v1/837cf6ff79f483e387a16c993634f3e4/asset-v1:SkillFactory+DSPR-2.0+14JULY2021+type@asset+block/SQL_pj2_2_4.png
alt="drawing" style="width:400px;">


4. INDUSTRIES

Таблица-справочник вариантов сфер деятельности работодателей.

<left> <img src = https://lms.skillfactory.ru/assets/courseware/v1/837cf6ff79f483e387a16c993634f3e4/asset-v1:SkillFactory+DSPR-2.0+14JULY2021+type@asset+block/SQL_pj2_2_5.png
alt="drawing" style="width:400px;">


5. EMPLOYERS_INDUSTRIES

Дополнительная таблица, которая существует для организации связи между работодателями и сферами их деятельности.

<left> <img src = https://lms.skillfactory.ru/assets/courseware/v1/837cf6ff79f483e387a16c993634f3e4/asset-v1:SkillFactory+DSPR-2.0+14JULY2021+type@asset+block/SQL_pj2_2_6.png
alt="drawing" style="width:400px;">


:arrow_up:[к оглавлению](https://github.com/Lev-Tegai/sf_data_science/blob/main/Project-2/README.md#%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)


Если информация по этому проекту покажется Вам интересной или полезной, я буду очень благодарен, если Вы отметите репозиторий и профиль ⭐️⭐️⭐️-дами

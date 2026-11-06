# SPB MAP — проверенные изображения для четырёх объектов
**Исследователь C, дополнение от 6 ноября 2026.** Структурированное сохранение присланного в чат отчёта (в сообщении не было отдельного файла). 11 материалов; сведения ниже принадлежат исследователю, если не помечены как независимо проверенные.

## 1. Доказательная таблица из отчёта
|SPB ID|Карточка / ID|Дата, автор|Изображено|Права / решение, заявленное C|
|---|---|---|---|---|
|0001|[File:Малый ПС 1Б 01.jpg](https://commons.wikimedia.org/wiki/File:Малый_ПС_1Б_01.jpg)|25.05.2017; Екатерина Борисова|Двор в доме Занина, точный ракурс октагона требует проверки|CC BY-SA 4.0, публикация после проверки ракурса|
|0002|[File:Двор-колодец "Бэтмен".jpg](https://commons.wikimedia.org/wiki/File:Двор-колодец_%22Бэтмен%22.jpg)|18.09.2020; Бегущий из города|Большой пр. П. С., 104; координаты камеры 59.967286, 30.313014|CC BY-SA 4.0|
|0003|[File:Benois House SPb 1916.jpg](https://commons.wikimedia.org/wiki/File:Benois_House_SPb_1916.jpg)|около 1916; аноним|Исторический фасад Каменноостровский 26–28|Public Domain Mark; оценить права в применимой юрисдикции|
|0003|[File:BenoisHouse.jpg](https://commons.wikimedia.org/wiki/File:BenoisHouse.jpg)|30.12.2008; Potekhin|Современный фасад Бенуа|CC BY-SA 3.0|
|0003|[File:Saint Petersburg, Kamennoostrovskiy Prospekt, 26-28. Three Benois House. Courtyard. -2024-09-09.jpg](https://commons.wikimedia.org/wiki/File:Saint_Petersburg,_Kamennoostrovskiy_Prospekt,_26-28._Three_Benois_House._Courtyard._-2024-09-09.jpg)|09.09.2024; Bestalex|Внутренний двор; камера 59.962281, 30.314208|CC BY-SA 4.0|
|0011|[File:LidvalHouse.jpg](https://commons.wikimedia.org/wiki/File:LidvalHouse.jpg)|январь 2010; Potekhin|Общий вид дома Лидваля|CC BY-SA 3.0|
|0011|[File:Дом Лидваль42.jpg](https://commons.wikimedia.org/wiki/File:Дом_Лидваль42.jpg)|08.09.2025; Екатерина Борисова|Архитектурные детали дома|CC BY-SA 4.0|
|0011|[File:Дом Лидваль, новое окрашивание 01.jpg](https://commons.wikimedia.org/wiki/File:Дом_Лидваль,_новое_окрашивание_01.jpg)|12.09.2022; Екатерина Борисова|Детали фасада, окрашивание|CC BY-SA 4.0|
|0011|[PastVu 244685](https://pastvu.com/p/244685)|1905; оригинальный автор неизвестен, пользователь загрузки SteelRatTV|Дом И. Б. Лидваль, источником назван «Ежегодник Общества архитекторов-художников», №1, 1906|Права неизвестны: LINK ONLY|
|0011|[PastVu 1428318](https://pastvu.com/p/1428318)|1905; автор неизвестен|Исторический фасад|Права неизвестны: LINK ONLY|
|0011|[PastVu 2662942](https://pastvu.com/p/2662942)|1997; автор неизвестен|Барельеф дома Лидваля|Права неизвестны: LINK ONLY|

## 2. Атрибуция
- [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/), [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/): автор, название/описание, ссылка на карточку, конкретную лицензию и указание изменений; при адаптации совместимые ShareAlike-условия.
- [Public Domain Mark](https://creativecommons.org/publicdomain/mark/1.0/): не лицензия, а обозначение предполагаемого отсутствия ограничений; проверить применимость перед импортом.
- [PastVu rules](https://docs.pastvu.com/rules): права на само изображение не появляются от наличия API. При неясности LINK ONLY.

## 3. PastVu API — как сообщено исследователем
Заявлен реальный запрос `photo.giveNearestPhotos` возле Лидваля: центр 59.95715, 30.32047, радиус 150 метров, максимум 5:
- 244685, 1905, «Дом И.Б. Лидваль», непосредственная связь;
- 1850083, 1990, «Кировский проспект, дом 1», требуется визуальная проверка;
- 2662942, 1997, «Барельеф на доме 1–3», непосредственная связь с деталью;
- 1428318, 1905, «Фасад дома И.Б. Лидваль», непосредственная;
- 244688, 1905, «Дом И.Б. Лидваль», непосредственная.
Исследователь утверждает также отдельный запрос `photo.giveForPage` для 244685, уточняющий происхождение снимка (издание 1906) и загрузившего пользователя SteelRatTV (не считать автором).
API: https://docs.pastvu.com/en/dev/api ; исходный запрос представлен как `https://api.pastvu.com/api2?method=photo.giveNearestPhotos&params=%7B%22geo%22:%5B59.95715,30.32047%5D,%22limit%22:5,%22distance%22:150%7D`.

## 4. Рекомендации C
7 современных Commons изображений подходят при точной соблюдённой атрибуции и проверке объекта, 1 историческое Commons изображение требует дополнительной правовой проверки, 3 PastVu изображений — LINK ONLY.
Предложен микропилот: по одному CC BY-SA изображению для каждого из четырёх действующих объектов; для `0001` уточнить, показан ли именно восьмиугольный двор.
Никакие Google Sheet, GitHub или публичный GeoJSON исследователем не менялись.

## 5. Координаторские контрольные заметки (независимая проверка)
Проверены по первичным страницам Commons:
- 0002: Commons прямо называет **Дидерихса, Большой проспект П. С. 104**, автора, дату, геокоординаты и CC BY-SA 4.0. Источник: https://commons.wikimedia.org/wiki/File:Двор-колодец_%22Бэтмен%22.jpg
- 0001: Commons подтверждает название, дом Занина, автора Борисову и CC BY-SA 4.0, но геометрия изображённого участка двора ещё не проверена: https://commons.wikimedia.org/wiki/File:Малый_ПС_1Б_01.jpg
- 0003 modern: Commons подтверждает Potekhin/2008/CC BY-SA 3.0: https://commons.wikimedia.org/wiki/File:BenoisHouse.jpg
- 0003 historical: Commons помечает изображение 1916 Public Domain; проверка статуса в применимой юрисдикции до перепубликации: https://commons.wikimedia.org/wiki/File:Benois_House_SPb_1916.jpg
- 0011: Commons подтверждает Potekhin/2010/CC BY-SA 3.0: https://commons.wikimedia.org/wiki/File:LidvalHouse.jpg
- PastVu API **не удалось независимо воспроизвести через веб-интерфейс координатора**; пять записей и проверка giveForPage остаются report-derived, требующими технического теста. Метаданные не доказывают права на изображения.

**Integration gate:** no production publishing, rehosting or copying. Store candidate source URLs, asset-level licenses, attributable source ID and photographer; review precise scene-to-place match and permissions before use.

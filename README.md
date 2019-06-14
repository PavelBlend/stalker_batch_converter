# STALKER Batch Converter

## [Скачать](https://github.com/PavelBlend/stalker_batch_converter/releases)

## Описание
STALKER Batch Converter - это скрипт, предназначенный для автоматизации конвертирования X-Ray Engine файлов с помощью конвертера от `Bardak'а`. Написан на Python. Для запуска нужно установить интерпретатор версии 3.0.0 или выше ([python.org](http://www.python.org/)). 

## Использование
Запустить `stalker_batch_converter.py`. После этого создадутся папки `input` и `output`, если их не было. Далее нужно скопировать файлы `*.ogf`, `*.omf` или `*.dm` в папку `input` и нажать необходимые кнопки для конвертирования. Сконвертированные файлы сохранятся в папку `output` и в каталоге со скриптом сохраниться лог файл. Поддерживается ковертация файлов из вложенных каталогов, например, `input\test_dir\test.ogf` сконвертируется в `output\test_dir\test.object`

## Режимы конвертации
ogf - object

ogf - bones

ogf - skls

ogf - skl

omf - skls

omf - skl

dm  - object

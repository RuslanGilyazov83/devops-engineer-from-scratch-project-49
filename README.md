## Brain Games

Набор консольных мини‑игр «Игры разума» из учебного курса Хекслета.  
В каждой игре нужно отвечать на вопросы, тренируя базовую математику и логическое мышление.

Реализованы следующие игры:
- **brain-even**: определение, является ли число чётным;
- **brain-calc**: вычисление значения арифметического выражения;
- **brain-gcd**: поиск наибольшего общего делителя двух чисел;
- **brain-progression**: нахождение пропущенного числа в арифметической прогрессии;
- **brain-prime**: проверка числа на простоту.

## Установка

Требования:
- **Python** версии **3.12+**;
- установленный **uv** (менеджер пакетов), либо стандартный `pip`.

### Вариант 1. Установка через uv (как в проекте)

```bash
uv sync
uv run brain-games
```

### Вариант 2. Установка как пакета (локально)

Из корня репозитория:

```bash
pip install .
```

После установки станут доступны консольные команды:

- `brain-games`
- `brain-even`
- `brain-calc`
- `brain-gcd`
- `brain-progression`
- `brain-prime`

## Запуск игр

Примеры запуска из терминала:

```bash
brain-games          # приветствие
brain-even           # игра «Проверка на чётность»
brain-calc           # игра «Калькулятор»
brain-gcd            # игра «НОД»
brain-progression    # игра «Прогрессия»
brain-prime          # игра «Простое число»
```

## Демонстрация (Asciinema)

**brain-even**
[![asciicast](https://asciinema.org/a/8fd8eaBF2fIyAtt4.svg)](https://asciinema.org/a/8fd8eaBF2fIyAtt4)

**brain-calc**
[![asciicast](https://asciinema.org/a/FFhsyg2Y444WXwe2.svg)](https://asciinema.org/a/FFhsyg2Y444WXwe2)

**brain-gcd**
[![asciicast](https://asciinema.org/a/VEDVFihZxLP6GWqT.svg)](https://asciinema.org/a/VEDVFihZxLP6GWqT)

**brain-progression**
[![asciicast](https://asciinema.org/a/29OxjFEs7c2AVsoP.svg)](https://asciinema.org/a/29OxjFEs7c2AVsoP)

**brain-prime**
[![asciicast](https://asciinema.org/a/Lj9eQRbMMhvmFmDD.svg)](https://asciinema.org/a/Lj9eQRbMMhvmFmDD)

## Качество кода (SonarCloud)

[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=RuslanGilyazov83_devops-engineer-from-scratch-project-49&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=RuslanGilyazov83_devops-engineer-from-scratch-project-49)
[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=RuslanGilyazov83_devops-engineer-from-scratch-project-49&metric=bugs)](https://sonarcloud.io/summary/new_code?id=RuslanGilyazov83_devops-engineer-from-scratch-project-49)
[![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=RuslanGilyazov83_devops-engineer-from-scratch-project-49&metric=vulnerabilities)](https://sonarcloud.io/summary/new_code?id=RuslanGilyazov83_devops-engineer-from-scratch-project-49)
[![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=RuslanGilyazov83_devops-engineer-from-scratch-project-49&metric=code_smells)](https://sonarcloud.io/summary/new_code?id=RuslanGilyazov83_devops-engineer-from-scratch-project-49)
[![Duplicated Lines (%)](https://sonarcloud.io/api/project_badges/measure?project=RuslanGilyazov83_devops-engineer-from-scratch-project-49&metric=duplicated_lines_density)](https://sonarcloud.io/summary/new_code?id=RuslanGilyazov83_devops-engineer-from-scratch-project-49)
[![Lines of Code](https://sonarcloud.io/api/project_badges/measure?project=RuslanGilyazov83_devops-engineer-from-scratch-project-49&metric=ncloc)](https://sonarcloud.io/summary/new_code?id=RuslanGilyazov83_devops-engineer-from-scratch-project-49)
[![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=RuslanGilyazov83_devops-engineer-from-scratch-project-49&metric=reliability_rating)](https://sonarcloud.io/summary/new_code?id=RuslanGilyazov83_devops-engineer-from-scratch-project-49)
[![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=RuslanGilyazov83_devops-engineer-from-scratch-project-49&metric=security_rating)](https://sonarcloud.io/summary/new_code?id=RuslanGilyazov83_devops-engineer-from-scratch-project-49)
[![Technical Debt](https://sonarcloud.io/api/project_badges/measure?project=RuslanGilyazov83_devops-engineer-from-scratch-project-49&metric=sqale_index)](https://sonarcloud.io/summary/new_code?id=RuslanGilyazov83_devops-engineer-from-scratch-project-49)
[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=RuslanGilyazov83_devops-engineer-from-scratch-project-49&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=RuslanGilyazov83_devops-engineer-from-scratch-project-49)
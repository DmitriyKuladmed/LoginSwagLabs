# LoginSwagLabs

Автоматизированные тесты логина для сайта [SauceDemo](https://www.saucedemo.com/) на Python с использованием Playwright, pytest и Allure.

## Структура проекта

```
LoginSwagLabs/
├── pages/                    # Page Object классы
│   ├── base_page.py         # Базовый класс
│   ├── login_page.py        # Страница логина
│   └── inventory_page.py    # Страница инвентаря
├── tests/                    # Тесты
│   └── test_login.py        # Тесты авторизации
├── conftest.py              # Фикстуры pytest
├── pytest.ini               # Конфигурация pytest
├── requirements.txt         # Зависимости Python
├── Dockerfile               # Контейнеризация
└── README.md                # Документация
```

## Тестовые сценарии

| Тест | Описание |
|------|----------|
| `test_successful_login` | Успешный логин (standard_user / secret_sauce) |
| `test_login_wrong_password` | Логин с неверным паролем |
| `test_locked_out_user` | Логин заблокированного пользователя |
| `test_login_empty_fields` | Логин с пустыми полями |
| `test_performance_glitch_user` | Логин пользователем с задержкой |

## Требования

- Python 3.10+
- Docker (опционально)

## Локальный запуск

### 1. Клонирование репозитория

```bash
git clone <repository-url>
cd LoginSwagLabs
```

### 2. Создание виртуального окружения

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/macOS
source venv/bin/activate
```

### 3. Установка зависимостей

```bash
pip install -r requirements.txt
```

### 4. Установка браузеров Playwright

```bash
playwright install chromium
```

### 5. Запуск тестов

```bash
# Запуск всех тестов
pytest

# Запуск с Allure отчётом
pytest --alluredir=allure-results

# Запуск в headed режиме (с отображением браузера)
pytest --headed

# Запуск конкретного теста
pytest tests/test_login.py::TestLogin::test_successful_login
```

## Запуск в Docker

### 1. Сборка образа

```bash
docker build -t saucedemo-tests .
```

### 2. Запуск тестов

```bash
# Запуск тестов
docker run --rm saucedemo-tests

# Запуск с сохранением Allure результатов
docker run --rm -v $(pwd)/allure-results:/app/allure-results saucedemo-tests
```

## Allure отчёты

### Установка Allure CLI

```bash
# macOS
brew install allure

# Windows (Scoop)
scoop install allure

# Linux
sudo apt-get install allure
```

### Генерация и просмотр отчёта

```bash
# Генерация отчёта
allure generate allure-results -o allure-report --clean

# Открытие отчёта в браузере
allure open allure-report

# Или сервер с автообновлением
allure serve allure-results
```

## Технологии

- **Python 3.10** — язык программирования
- **Playwright** — фреймворк для автоматизации браузера
- **pytest** — фреймворк для тестирования
- **Allure** — генерация отчётов
- **Docker** — контейнеризация

# Sentiment API

Сервис анализа тональности текста на базе предварительно обученной модели
[`Facececersek/bedrock-sentiment-tiny`](https://huggingface.co/Facececersek/bedrock-sentiment-tiny).
Модель не обучается — используется как есть через `transformers.pipeline`.

## Стек

- **FastAPI** — REST API
- **Transformers** — загрузка предварительно обученной модели
- **pytest** — тесты
- **GitHub Actions** — CI/CD
- **Render** — облачное развёртывание

## Эндпоинты

| Метод | Путь       | Описание                          |
|-------|------------|-----------------------------------|
| GET   | `/health`  | Health check                      |
| POST  | `/predict` | Классификация тональности текста  |

### Локальный запуск
```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
```
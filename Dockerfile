FROM python:3.10-slim

WORKDIR /app
COPY requirements.txt /app/
RUN pip install -r requirements.txt

COPY . /app/
EXPOSE 7860
CMD ["python", "src/app.py"]
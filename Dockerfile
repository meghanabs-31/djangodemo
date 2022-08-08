FROM python:3

RUN mkdir /app
WORKDIR /app
COPY requirements.txt /app/
RUN pip install -r requirements.txt
COPY . /app/
EXPOSE 80
CMD ["python3", "manage.py", "runserver"]

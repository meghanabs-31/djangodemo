FROM python:3

RUN mkdir /app
WORKDIR /app
COPY requirements.txt /app/
RUN pip install -r requirements.txt
COPY . /app/
CMD ["python3", "manage.py", "runserver"]
EXPOSE 8080:80

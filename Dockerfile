FROM python:3.8
COPY . /
RUN apt update -y
RUN apt install python3-pip -y
RUN pip3 install -r requirements.txt
EXPOSE 8000

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]

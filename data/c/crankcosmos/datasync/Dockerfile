FROM python:3  
ENV PYTHONUNBUFFERED 1  
ENV DJANGO_SETTINGS_MODULE datasync.settings  
  
#ENV http_proxy http://169.154.0.13:3128/  
#ENV https_proxy https://169.154.0.13:3128/  
RUN apt-get update -y && apt-get install -y cron && rm -rf
/var/lib/apt/lists/*  
  
RUN mkdir /code /files  
WORKDIR /code  
ADD . /code/  
  
RUN pip install -r requirements.txt  
  
CMD python /code/manage.py runserver 0.0.0.0:8000  


FROM python:3.6.3  
ENV DJANGO_SETTINGS_MODULE=minicomi.settings.production  
ENV MINICOMI_DATABASE_NAME=minicomi  
ENV MINICOMI_DATABASE_USER=minicomi  
  
COPY ./requirements.txt /opt/minicomi/requirements.txt  
WORKDIR /opt/minicomi  
  
RUN apt-get update && apt-get -y install postgresql-client && pip install -r
requirements.txt  
  
COPY . /opt/minicomi  
  
RUN python manage.py collectstatic --noinput  
  
EXPOSE 5000  
ENTRYPOINT ["docker/run.sh"]  
CMD ["start"]  


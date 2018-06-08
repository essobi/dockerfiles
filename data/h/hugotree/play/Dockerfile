FROM python:2.7  
ENV DJANGO_SETTINGS_MODULE play.settings.production  
  
RUN mkdir /app  
WORKDIR /app  
ADD requirements.txt /app/  
RUN pip install -r requirements.txt  
ADD . /app/  
  
COPY ./docker-entrypoint.sh /  
ENTRYPOINT ["/docker-entrypoint.sh"]  


FROM python:3.6-alpine3.6  
#Install uwsgi  
RUN apk add --no-cache linux-headers g++ && \  
pip install --no-cache-dir uwsgi && \  
apk del g++ linux-headers  
  
#Install uwsgi and django  
RUN pip install --no-cache-dir django  
  
# setup all the configfiles  
COPY config/uwsgi.ini /config/  
  
#Create www-data user  
RUN mkdir -p /home/django/app && \  
adduser -D -s /sbin/nologin -h /home/django/app www-data && \  
chown www-data:www-data -R /home/django  
  
WORKDIR /home/django  
  
EXPOSE 8080  
CMD ["uwsgi", "--ini", "/config/uwsgi.ini"]  


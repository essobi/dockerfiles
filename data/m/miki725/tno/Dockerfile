FROM python:3.4  
MAINTAINER "Miroslav Shubernetskiy"  
COPY tno/ /www  
COPY requirements.txt /www/requirements.txt  
  
WORKDIR /www  
  
ENV DJANGO_SETTINGS_MODULE=tno.settings.prod  
  
RUN apt-get update  
RUN apt-get upgrade -y  
RUN apt-get install -y \  
libffi-dev \  
libssl-dev \  
libjpeg-dev \  
libpng12-dev \  
libpq-dev \  
libxml2-dev \  
libxslt1-dev \  
nodejs-legacy \  
npm  
  
RUN npm install -g \  
less \  
yuglify  
  
# cleanup  
RUN apt-get clean && \  
rm -rf /var/cache/apt  
  
RUN pip install -r /www/requirements.txt  
  
EXPOSE 8888  
CMD newrelic-admin run-python \  
/usr/local/bin/gunicorn --config gunicorn.py tno.wsgi:application  


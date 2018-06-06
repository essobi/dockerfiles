FROM ubuntu:14.04  
  
# author  
MAINTAINER Rafael Fazzolino  
  
ENV PYTHONUNBUFFERED 1 \  
LANG=pt_BR.UTF-8 \  
LANGUAGE=pt_BR:pt \  
LC_ALL=pt_BR.UTF-8  
  
RUN apt-get update \  
&& apt-get -y install \  
python3-pip \  
libpq-dev \  
python-dev  
  
  
# pip  
RUN pip3 install \  
appdirs==1.4.3 \  
Django==1.11 \  
django-ajax-selects==1.5.2 \  
django-widget-tweaks==1.4.1 \  
packaging==16.8 \  
pluggy==0.4.0 \  
py==1.4.33 \  
pyparsing==2.2.0 \  
pytest==3.0.7 \  
pytest-django==3.1.2 \  
pytz==2017.2 \  
simplejson==3.10.0 \  
six==1.10.0 \  
tox==2.7.0 \  
virtualenv==15.1.0 \  
psycopg2==2.7.1  
  
RUN mkdir code/  
COPY . code/  


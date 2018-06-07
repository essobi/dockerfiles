FROM alpine  
MAINTAINER Emile Contal <emile@crossingminds.com>  
  
RUN apk --no-cache add \  
alpine-sdk \  
bash \  
libffi-dev \  
linux-headers \  
mysql-client \  
py-mysqldb \  
openssl-dev \  
py2-pip \  
python-dev  
RUN echo http://dl-cdn.alpinelinux.org/alpine/edge/testing >>
/etc/apk/repositories && \  
echo http://dl-cdn.alpinelinux.org/alpine/edge/community >>
/etc/apk/repositories && \  
apk update && \  
apk add py-scipy  
RUN pip install --upgrade pip \  
awsebcli \  
awscli \  
celery \  
credstash \  
django-cors-headers \  
djangorestframework==3.5.3 \  
Django==1.11.8 \  
google-cloud-error-reporting \  
pytest \  
python-json-logger==0.1.8 \  
redis \  
simplejson==3.11.1 \  
social-auth-core==1.2.0 \  
social-auth-app-django==1.1.0 \  
sphinx==1.4 \  
sphinx_bootstrap_theme \  
sphinxcontrib.httpdomain \  
unidecode \  
user_agents  
  
RUN mkdir ~/.aws  
  
# https://github.com/docker-library/python/issues/112  
#RUN ln -s /usr/include/locale.h /usr/include/xlocale.h  
#RUN pip install --upgrade numpy \  
# scipy  


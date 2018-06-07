FROM ubuntu:trusty  
  
MAINTAINER Krator <kratorado@gmail.com>  
  
#RUN (echo "deb http://cn.archive.ubuntu.com/ubuntu/ trusty main restricted
universe multiverse" > /etc/apt/sources.list && echo "deb
http://cn.archive.ubuntu.com/ubuntu/ trusty-updates main restricted universe
multiverse" >> /etc/apt/sources.list && echo "deb
http://cn.archive.ubuntu.com/ubuntu/ trusty-backports main restricted universe
multiverse" >> /etc/apt/sources.list && echo "deb
http://cn.archive.ubuntu.com/ubuntu/ trusty-security main restricted universe
multiverse" >> /etc/apt/sources.list)  
RUN apt-get update && apt-get install -y \  
sqlite3 \  
python3-pip \  
\--no-install-recommends && rm -rf /var/lib/apt/lists/*  
  
ENV DJANGO_VERSION 1.8.5  
ENV GUNICORN_VERSION 19.3.0  
RUN pip3 install django==${DJANGO_VERSION}  
RUN pip3 install gunicorn==${GUNICORN_VERSION}  
  
RUN apt-get autoremove -y  
  
VOLUME ['/app']  
WORKDIR /app  
  
VOLUME ['/var/log']  
  
EXPOSE 8000  
CMD gunicorn -b 0.0.0.0:8000 --env DJANGO_SETTINGS_MODULE=${APPNAME}.settings
${APPNAME}.wsgi --access-logfile /var/log/access.log --log-file
/var/log/gunicorn.log  


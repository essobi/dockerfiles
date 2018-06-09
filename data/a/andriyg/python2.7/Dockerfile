FROM ubuntu:bionic  
  
ENV LANG=en_US.UTF-8  
  
ENV TZ=UTC  
  
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone  
  
RUN \  
apt update && \  
apt upgrade -y && \  
apt install -y --allow-unauthenticated \  
locales \  
ca-certificates tzdata python2.7 netcat htop less curl libmysqlclient20 \  
libjpeg8 libpng16-16 libxslt1.1 \  
libmysqlclient-dev python2.7-dev python-pip libjpeg8-dev libpng-dev
libxslt1-dev && \  
locale-gen ${LANG} && \  
pip install -U pillow django-redis-cache pytz lxml gu-django-filebrowser-no-
grappelli gu-django-tinymce mysqlclient uwsgi && \  
apt autoremove -y && \  
apt autoclean -y && \  
rm -rf /tmp/* /var/lib/apt/lists/* /root/.cache && \  
true  


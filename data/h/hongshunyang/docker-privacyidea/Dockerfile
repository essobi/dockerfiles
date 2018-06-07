FROM hongshunyang/docker-python2-uwsgi  
MAINTAINER Hongshun Yang <yanghongshun@outlook.com>  
  
## privacyIDEA@2.17  
RUN apk add -U libpq mariadb-client-libs zlib jpeg libffi libxslt libxml2
freetype libwebp libpng lcms2 tcl tk tiff tiff-tools \  
&& apk add -U --virtual build-deps python-dev build-base zlib-dev jpeg-dev
libpng-dev libwebp-dev lcms2-dev \  
tcl-dev tk-dev libffi-dev tiff-dev openssl-dev libxslt-dev libxml2-dev
freetype-dev postgresql-dev mariadb-dev  
  
ENV PRIVACYIDEA /root/privacyidea  
  
## issue:encoder zip not available  
## fix pillow to find zlib  
ENV LIBRARY_PATH=/lib:/usr/lib  
##LIBRARY_PATH=/lib:/usr/lib /bin/sh -c "pip install -r /requirements.txt"  
RUN mkdir -p $PRIVACYIDEA/.venv \  
&& virtualenv $PRIVACYIDEA/.venv \  
&& source $PRIVACYIDEA/.venv/bin/activate \  
&& wget
https://raw.githubusercontent.com/privacyidea/privacyidea/master/requirements.txt
\  
&& pip install -r requirements.txt \  
&& pip install MySQL-python pymysql-sa PyMySQL Flask-MySQLdb \  
&& pip install privacyIDEA \  
&& deactivate  
  
RUN apk -U del --purge build-deps  


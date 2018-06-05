FROM ubuntu:16.04  
MAINTAINER Manuel Ornato <manuel.ornato@multimediapress.com>  
  
RUN apt-get update \  
&& apt-get install -y \  
libffi-dev \  
libssl-dev \  
nginx \  
python2.7 \  
python-dev \  
python-lxml \  
python-openssl \  
python-pip \  
supervisor \  
&& pip install \  
attrs \  
boto \  
pyasn1-modules \  
scrapy \  
scrapyd \  
&& pip install pyopenssl --upgrade  
  
COPY /etc/boto/boto.cfg /etc/boto/boto.cfg  
COPY /etc/scrapyd/scrapyd.conf /etc/scrapyd/scrapyd.conf  
COPY /etc/nginx/nginx.conf /etc/nginx/nginx.conf  
COPY /etc/nginx/.htpasswd /etc/nginx/.htpasswd  
COPY /etc/nginx/setup_user.sh /etc/nginx/setup_user.sh  
COPY /etc/supervisor/supervisord.conf /etc/supervisor/supervisord.conf  
COPY /entrypoint.sh /entrypoint.sh  
  
RUN chmod +x /etc/nginx/setup_user.sh /entrypoint.sh  
  
VOLUME [/var/lib/scrapyd]  
EXPOSE 6800  
ENTRYPOINT ["/entrypoint.sh"]  
  


FROM itatabitovski/debian:jessie  
  
ENV UWSGI_VERSION 2.0.14  
  
RUN apt-install curl && \  
echo "deb http://packages.dotdeb.org jessie all" >
/etc/apt/sources.list.d/dotdeb.list && \  
curl http://www.dotdeb.org/dotdeb.gpg | apt-key add - && \  
apt-install build-essential \  
python-dev \  
python-pip \  
libxml2-dev \  
php7.0-dev \  
libphp7.0-embed && \  
  
UWSGI_PROFILE=php pip install uwsgi==$UWSGI_VERSION && \  
  
apt-purge build-essential \  
python-dev \  
python-pip \  
libxml2-dev \  
php7.0-dev \  
libxml2-dev  
  
ENTRYPOINT /usr/local/bin/uwsgi  


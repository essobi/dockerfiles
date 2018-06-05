FROM python:2.7-slim  
MAINTAINER Lev Aminov <leoderoko@gmail.com>  
  
ENV FB_REPO https://github.com/fabric-bolt/fabric-bolt.git  
ENV FB_VERSION master  
  
RUN mkdir /docker-entrypoint-init.d  
  
RUN apt-get update \  
&& apt-get install -y \  
git \  
gcc \  
netcat \  
gettext \  
libxml2-dev libxslt1-dev \  
mysql-client libmysqlclient-dev \  
postgresql-client libpq-dev \  
sqlite3 \  
\--no-install-recommends \  
&& rm -rf /var/lib/apt/lists/*  
  
ENV PIP_NO_CACHE_DIR off  
  
ENV FB_CONF /root/.fabric-bolt/settings.py  
  
RUN mkdir -p /src \  
&& git clone ${FB_REPO} /src/fabric-bolt \  
&& cd /src/fabric-bolt \  
&& git checkout ${FB_VERSION} \  
&& pip install -e ".[postgres,mysql]" \  
&& pip install uwsgi  
  
COPY docker-entrypoint.sh /  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
EXPOSE 8000 9000  
CMD ["fabric-bolt"]  


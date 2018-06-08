FROM debian:jessie  
ENV PYTHONUNBUFFERED 1  
# Upgrade the base distribution  
RUN apt-get -y update && apt-get -y upgrade  
RUN apt-get -y install wget  
  
#Postgres and geospatial  
RUN wget --quiet --no-check-certificate -O -
https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add -  
RUN echo "deb http://apt.postgresql.org/pub/repos/apt/ jessie-pgdg main" >>
/etc/apt/sources.list  
RUN apt-get -y update && apt-get -y install build-essential binutils libproj-
dev python python-pip git-core python-dev libyaml-dev  
RUN apt-get -y install postgresql-9.4-postgis-2.1 postgresql-contrib postgis
libpq-dev gdal-bin libgeos-dev libgeos-c1 python-gdal mysql-client
libmysqlclient-dev  
  
#Nginx  
RUN apt-get -y install ca-certificates nginx gettext-base  
RUN pip install uwsgi && mkdir -p /etc/uwsgi/vassals  
RUN echo "" > /etc/rc.local  
RUN pip install mysqlclient Django==1.9.2 psycopg2  
RUN mkdir -p /usr/src/app  
  
RUN ln -sf /dev/stdout /var/log/nginx/access.log \  
&& ln -sf /dev/stderr /var/log/nginx/error.log  
  
COPY launch-nginx.sh /usr/bin/launch-nginx.sh  
RUN chmod a+x /usr/bin/launch-nginx.sh  
  
EXPOSE 80 443  
WORKDIR /usr/src/app  
CMD ["/usr/bin/launch-nginx.sh"]


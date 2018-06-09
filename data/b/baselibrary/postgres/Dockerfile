FROM baselibrary/baseimage:1.0.0  
MAINTAINER ShawnMa <qsma@thoughtworks.com>  
  
## Version  
ENV POSTGRES_MAJOR 9.3  
ENV POSTGRES_VERSION 2.1.8+dfsg-5~97.git43a09cc.pgdg14.04+1  
## Repository  
RUN \  
apt-key adv --keyserver keyserver.ubuntu.com --recv-keys ACCC4CF8 &&\  
echo "deb http://apt.postgresql.org/pub/repos/apt trusty-pgdg main" >
/etc/apt/sources.list.d/postgres.list  
  
## Packages  
RUN \  
apt-get update &&\  
apt-get install -y postgresql-9.3-postgis-2.1=$POSTGRES_VERSION postgresql-
contrib-9.3 python-psycopg2 &&\  
rm -rf /var/lib/apt/lists/*  
  
## Tools  
RUN \  
wget -O /bin/gosu "https://github.com/tianon/gosu/releases/download/1.7/gosu-
amd64" &&\  
chmod u+x /bin/gosu  
  
## Environments  
ENV PATH /usr/lib/postgresql/9.3/bin:$PATH  
ENV PGDATA /var/lib/postgresql/data  
  
## Scripts  
ADD docker-entrypoint.sh /docker-entrypoint.sh  
RUN chmod a+x /docker-entrypoint.sh  
  
EXPOSE 5432  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
VOLUME ["/var/lib/postgresql/data"]  
  
CMD ["postgres"]  
  


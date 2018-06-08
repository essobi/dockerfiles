FROM ubuntu:16.04  
ENV PGADMIN4_VERSION 2.1  
  
LABEL org.label-schema.name="pgAdmin4" \  
org.label-schema.version="$PGADMIN4_VERSION" \  
org.label-schema.license="PostgreSQL" \  
org.label-schema.url="https://www.pgadmin.org" \  
org.label-schema.vcs-url="https://github.com/obarisk/dockercloud-pgadmin4"  
  
RUN apt-get update && \  
apt-get -y install wget python3 python3-pip openssl && \  
mkdir -p /etc/apt/sources.list.d && \  
echo "deb http://apt.postgresql.org/pub/repos/apt/ xenial-pgdg main" >
/etc/apt/sources.list.d/pgdg.list && \  
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key
add - && \  
apt-get update && \  
apt-get -y install postgresql-client && \  
pip3 --no-cache-dir install
https://ftp.postgresql.org/pub/pgadmin/pgadmin4/v2.1/pip/pgadmin4-2.1-py2.py3-none-
any.whl && \  
pip3 --no-cache-dir install flask_htmlmin  
  
VOLUME /var/lib/pgadmin4  
  
COPY docker-entrypoint.sh /usr/local/bin  
ENTRYPOINT ["docker-entrypoint.sh"]  
  
EXPOSE 5050  
CMD ["pgadmin4"]  


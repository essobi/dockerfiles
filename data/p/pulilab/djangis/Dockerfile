FROM debian:jessie  
  
# ENV POSTGRES_PASSWORD  
  
ENV PGDATA /var/lib/postgresql/data  
ENV PGUSER postgres  
ENV PG_VERSION 9.4  
VOLUME /var/lib/postgresql/data  
COPY commands.sh /docker-entrypoint-initdb.d/  
COPY docker-entrypoint.sh /  
  
RUN apt-get update && \  
apt-get install -y locales && \  
rm -rf /var/lib/apt/lists/* && \  
localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias en_US.UTF-8  
  
RUN apt-get update && \  
apt-get install -y postgresql-common postgresql-9.4 postgresql-contrib-9.4
postgis && \  
apt-get install -y python-pip python-dev libpq-dev nginx libjpeg-dev
libfreetype6-dev zlib1g-dev libpng12-dev nano sudo && \  
rm -rf /var/lib/apt/lists/*  
  
RUN pip install Django==1.8.4 && \  
pip install psycopg2 && \  
pip install Pillow  
  
EXPOSE 8000  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
CMD ["django"]  


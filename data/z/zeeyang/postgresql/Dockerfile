# PostgreSQL (http://www.postgresql.org/)  
FROM debian:jessie  
MAINTAINER Zee Yang <zee.yang@gmail.com>  
  
RUN export DEBIAN_FRONTEND=noninteractive LANG \  
&& echo en_US.UTF-8 UTF-8 > /etc/locale.gen \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends pwgen locales \  
&& update-locale LANG=en_US.UTF-8 && . /etc/default/locale \  
&& apt-get install -y postgresql-9.3 postgresql-contrib-9.3  
  
RUN /etc/init.d/postgresql stop \  
&& pg_dropcluster --stop 9.3 main \  
&& pg_createcluster --locale=en_US.UTF-8 --start 9.3 main  
  
RUN sed -i -e"s/^#listen_addresses =.*$/listen_addresses = '*'/"
/etc/postgresql/9.3/main/postgresql.conf  
RUN echo "host all all 0.0.0.0/0 md5" >> /etc/postgresql/9.3/main/pg_hba.conf  
  
VOLUME ["/etc/postgresql", "/var/log/postgresql", "/var/lib/postgresql"]  
EXPOSE 5432  
ADD scripts /scripts  
RUN chmod +x /scripts/start.sh && touch /firstrun  
  
CMD ["/scripts/start.sh"]  


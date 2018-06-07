FROM debian:stable  
MAINTAINER Tonnerre LOMBARD <tonnerre@ancient-solutions.com>  
  
RUN apt-get -q -y update  
RUN apt-get -q -y -o Dpkg::Options::=--force-confdef -o
Dpkg::Options::=--force-confold --purge install locales postgresql
postgresql-9.6 postgresql-9.6-ip4r postgresql-9.6-pgmemcache
postgresql-9.6-plr postgresql-9.6-postgis-2.3
postgresql-9.6-postgis-2.3-scripts postgresql-9.6-prefix lsof strace  
  
RUN /usr/bin/pg_dropcluster 9.6 main  
  
RUN sed -i -e "s/^.*en_US.UTF-8/en_US.UTF-8/g" /etc/locale.gen  
RUN /usr/sbin/locale-gen  
  
ADD pg_config.sh /usr/local/bin/pg_config.sh  
  
RUN ["/bin/chmod", "0555", "/usr/local/bin/pg_config.sh"]  
RUN ["/usr/bin/install", "-o", "postgres", "-g", "postgres", "-m", "2750",
"-d", "/var/run/postgresql"]  
RUN ["/usr/bin/install", "-o", "postgres", "-g", "postgres", "-m", "2750",
"-d", "/var/run/postgresql/9.6-main.pg_stat_tmp"]  
RUN ["/usr/bin/chown", "-R", "postgres:postgres", "/etc/postgresql"]  
  
EXPOSE 5432/tcp  
VOLUME ["/config", "/tls", "/tmp", "/var/lib/postgresql"]  
USER postgres  
  
CMD ["/bin/sh", "/usr/local/bin/pg_config.sh"]  


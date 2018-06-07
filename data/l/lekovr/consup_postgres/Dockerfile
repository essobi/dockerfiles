# consup_postgres  
# Consup based Postgresql image  
# See https://github.com/LeKovr/consup  
#  
FROM lekovr/consup_baseapp  
  
MAINTAINER Alexey Kovrizhkin <lekovr+docker@gmail.com>  
  
ENV DOCKERFILE_VERSION 170429  
#
-------------------------------------------------------------------------------  
# Install postgresql  
ENV PG_MAJOR 9.6  
# add our user and group first to make sure their IDs get assigned
consistently, regardless of whatever dependencies get added  
RUN groupadd -r postgres && useradd -r -g postgres -d /var/lib/postgresql
postgres  
  
ENV PATH /usr/lib/postgresql/$PG_MAJOR/bin:$PATH  
ENV PGDATA /var/lib/postgresql/$PG_MAJOR  
ENV PGUSER postgres  
  
COPY *.conf /etc/postgresql/  
  
#
-------------------------------------------------------------------------------  
# Run custom setup scripts  
ADD setup_*.sh /tmp/  
RUN for f in /tmp/setup_*.sh ; do >&2 echo ">>>> $f" ; . $f ; rm $f ; done  
  
#
-------------------------------------------------------------------------------  
# Setup Consul client  
COPY init.d /init.d  
COPY consul /etc/consul  
COPY supervisor.d /etc/supervisor/conf.d  
  
#
-------------------------------------------------------------------------------  
# db startup trigger  
COPY db_check_started.sh /usr/local/bin/db_check_started.sh  
  
# dbcc connect key  
ENV DBCC_KEY SET_YOUR_DBCC_KEY_HERE_OR_IN_fidm.yml  
  
# dbcc port  
ENV DBCC_PORT 5480  
# postgres & dbcc ports  
EXPOSE 5432 5480  
# this will be mounted externally  
VOLUME ["/var/lib/postgresql"]  
  
# Database locale  
ENV LOCALE en_US  
  
#
-------------------------------------------------------------------------------  
# Replica setup  
ENV REPLICA_ROOT /opt/shared  
VOLUME ["/opt/shared"]  
  
# ENV REPLICA_MODE  
# * MASTER - save log to REPLICA_ROOT  
# * SLAVE - load logs from REPLICA_ROOT, READ-ONLY DB  
# * other - standalone server (if /var/lib/postgresql not mounted, every start
will use empty cluster)  
# See init.d/postgres.sh  
ENV REPLICA_MODE ""  
# Backup DB on start  
ENV REPLICA_BACKUP ""  


FROM ubuntu:latest  
MAINTAINER Sidney Li <sidney.hy.li@gmail.com>  
  
RUN apt-get update && apt-get install -y wget && \  
apt-get install -y python3 python3-pip supervisor && \  
echo "deb http://apt.postgresql.org/pub/repos/apt/ xenial-pgdg main" >
/etc/apt/sources.list.d/pgdg.list && \  
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key
add - && \  
apt-get update && \  
apt-get install -y postgresql-9.6 postgresql-client-9.6  
  
RUN pip3 install pypdx pdxdisplay  
  
COPY supervisord.conf /etc/supervisord.conf  
  
ENV PDX_DSN "dbname='pdx' user='pdxuser' password='billofmaterials'
host='localhost' port=5432"  
ENV PDX_EXTACCESS 1  
ENV LC_ALL C.UTF-8  
ENV LANG C.UTF-8  
EXPOSE 5000  
#
================================================================================================  
# ref: https://docs.docker.com/engine/examples/postgresql_service/#installing-
postgresql-on-docker  
# run as user postgres  
USER postgres  
  
RUN /etc/init.d/postgresql start &&\  
psql --command "CREATE USER pdxuser WITH ENCRYPTED PASSWORD
'billofmaterials';" &&\  
createdb -O pdxuser pdx &&\  
/etc/init.d/postgresql stop  
  
RUN echo "hostssl all all 0.0.0.0/0 md5" >>
/etc/postgresql/9.6/main/pg_hba.conf &&\  
echo "listen_addresses='*'" >> /etc/postgresql/9.6/main/postgresql.conf  
  
EXPOSE 5432  
USER root  
  
CMD ["/usr/bin/supervisord","-c","/etc/supervisord.conf"]  


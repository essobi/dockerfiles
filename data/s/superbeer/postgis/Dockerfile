############################################################  
# Dockerfile to run superbeer/postgis Containers  
# Based on Postgresql 9.3 Image  
# Setting up a 'geodjango' postgis 2.1 database  
# And creating a 'postgres' user with 'postgres' as password  
# On default port '5432'  
############################################################  
  
  
FROM ubuntu:14.04  
MAINTAINER Lola Rigaut-Luczak <rllola80@gmail.com>  
  
RUN apt-get update -y  
RUN apt-get install -y postgresql-9.3 postgresql-contrib-9.3 postgresql-
client-9.3 postgresql-9.3-postgis-2.1 inotify-tools  
RUN rm -rf /var/lib/apt/lists/*  
  
ADD ./scripts/postgres.bis.sh /var/lib/postgresql/postgres.sh  
RUN chown postgres:postgres /var/lib/postgresql/postgres.sh  
RUN chmod +x /var/lib/postgresql/postgres.sh  
  
USER postgres  
  
# Initial default user/pass and schema (not safe to use in prod should be pass
when running the 'docker run' command but I am too lazy...)  
ENV USER postgres  
ENV PASSWORD postgres  
ENV SCHEMA geodjango  
ENV POSTGIS true  
  
RUN echo "listen_addresses='*'" >> /etc/postgresql/9.3/main/postgresql.conf  
RUN echo "host all all 0.0.0.0/0 md5" >> /etc/postgresql/9.3/main/pg_hba.conf  
  
RUN touch /var/tmp/firstrun  
  
EXPOSE 5432  
CMD ["/var/lib/postgresql/postgres.sh"]  


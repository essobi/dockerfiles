FROM ubuntu:14.04  
MAINTAINER Maksym Bodnarchuk <bodnarchuk@gmail.com>  
  
ENV REFRESHED_AT 2014-09-24  
RUN apt-get update  
RUN apt-get install -y postgresql-9.3  
  
USER postgres  
  
RUN /etc/init.d/postgresql start && psql --command "CREATE USER draft WITH
SUPERUSER PASSWORD 'draft';" && createdb -O draft draft  
RUN echo "host all all 0.0.0.0/0 md5" >> /etc/postgresql/9.3/main/pg_hba.conf  
RUN echo "listen_addresses='*'" >> /etc/postgresql/9.3/main/postgresql.conf  
  
EXPOSE 5432  
VOLUME ["/etc/postgresql", "/var/log/postgresql", "/var/lib/postgresql"]  
  
CMD ["/usr/lib/postgresql/9.3/bin/postgres", "-D",
"/var/lib/postgresql/9.3/main", "-c",
"config_file=/etc/postgresql/9.3/main/postgresql.conf"]


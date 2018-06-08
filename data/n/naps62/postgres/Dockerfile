FROM phusion/baseimage:0.9.15  
MAINTAINER Miguel Palhas <mpalhas@gmail.com>  
  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys
B97B0AFCAA1A47F044F244A07FCC7D46ACCC4CF8  
  
RUN echo "deb http://apt.postgresql.org/pub/repos/apt/ precise-pgdg main" >
/etc/apt/sources.list.d/pgdg.list  
  
RUN apt-get update && apt-get install -y python-software-properties software-
properties-common postgresql-9.3 postgresql-client-9.3 postgresql-contrib-9.3  
  
USER postgres  
  
# Adjust PostgreSQL configuration so that remote connections to the  
# database are possible.  
RUN echo "host all all 0.0.0.0/0 md5" >> /etc/postgresql/9.3/main/pg_hba.conf  
RUN echo "listen_addresses='*'" >> /etc/postgresql/9.3/main/postgresql.conf  
  
# Expose the PostgreSQL port  
EXPOSE 5432  
# Add VOLUMEs to allow backup of config, logs and databases  
VOLUME ["/etc/postgresql", "/var/log/postgresql", "/var/lib/postgresql"]  
  
# Set the default command to run when starting the container  
CMD ["/usr/lib/postgresql/9.3/bin/postgres", "-D",
"/var/lib/postgresql/9.3/main", "-c",
"config_file=/etc/postgresql/9.3/main/postgresql.conf"]  
  
RUN /etc/init.d/postgresql start &&\  
psql --command "CREATE USER docker WITH SUPERUSER PASSWORD 'docker';" &&\  
createdb -O docker docker  


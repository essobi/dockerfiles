# based on http://docs.docker.com/examples/postgresql_service/  
FROM ubuntu:14.04  
MAINTAINER Ying Liu - www.MindIsSoftware.com  
  
ENV APP_DB_USER odoo  
ENV APP_DB_PASSWORD 'odoo'  
# !!! EXPOSE port doesn's support ENV variable, has to change EXPOSE command  
ENV APP_DB_PORT 5432  
# Configure locale  
RUN locale-gen en_US.UTF-8 && update-locale  
RUN echo 'LANG="en_US.UTF-8"' > /etc/default/locale  
  
# to turn off debconf messages  
RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-
selections  
  
RUN apt-get update -y  
RUN apt-get upgrade -y  
RUN apt-get install -y postgresql-9.3 postgresql-contrib-9.3  
  
# Run the rest of the commands as the ``postgres`` user created by the
``postgres-9.3`` package  
USER postgres  
  
# Create a PostgreSQL role  
# Note: here we use ``&&\\`` to run commands one after the other - the ``\\``  
# allows the RUN command to span multiple lines.  
RUN /etc/init.d/postgresql start &&\  
psql -e --command "CREATE USER $APP_DB_USER WITH SUPERUSER PASSWORD
$APP_DB_PASSWORD" &&\  
createdb -O $APP_DB_USER $APP_DB_USER &&\  
/etc/init.d/postgresql stop  
  
# Adjust PostgreSQL configuration so that remote connections to the  
# database are possible.  
RUN echo "host all all 0.0.0.0/0 md5" >> /etc/postgresql/9.3/main/pg_hba.conf  
RUN echo "listen_addresses='*'" >> /etc/postgresql/9.3/main/postgresql.conf  
RUN sed -i "s/port = [0-9]*/port = $APP_DB_PORT/g"
/etc/postgresql/9.3/main/postgresql.conf  
  
# Expose the PostgreSQL port  
EXPOSE 5432  
# Add VOLUMEs to allow backup of config, logs and databases  
VOLUME ["/etc/postgresql", "/var/log/postgresql", "/var/lib/postgresql"]  
  
ENTRYPOINT ["/usr/lib/postgresql/9.3/bin/postgres"]  
CMD ["-D", "/var/lib/postgresql/9.3/data", "-c",
"config_file=/etc/postgresql/9.3/main/postgresql.conf"]  


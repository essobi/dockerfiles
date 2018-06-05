FROM ubuntu:trusty  
MAINTAINER blag  
  
# Install PostgreSQL 9.3  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y postgresql-9.3  
RUN apt-get clean  
  
# Adjust PostgreSQL configuration so that remote connections to the database  
# are possible  
RUN echo "host all all 0.0.0.0/0 md5" >> /etc/postgresql/9.3/main/pg_hba.conf  
RUN echo "listen_addresses='*'" >> /etc/postgresql/9.3/main/postgresql.conf  
  
# Add VOLUMEs to allow backup of config, logs, and databases  
VOLUME ["/etc/postgresql/9.3", "/var/log/postgresql/9.3",
"/var/lib/postgresql"]  
  
ADD run.sh /run.sh  
RUN chmod 755 /*.sh  
  
EXPOSE 5432  
CMD ["/run.sh"]  


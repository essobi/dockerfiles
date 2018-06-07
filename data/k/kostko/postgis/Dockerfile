FROM ubuntu:trusty  
MAINTAINER Jernej Kos, jernej@kos.mx  
  
# Expose PostgreSQL database port  
EXPOSE 5432  
# Default credentials  
ENV PGSQL_SUPERUSER_USERNAME docker  
ENV PGSQL_SUPERUSER_PASSWORD docker  
  
# Install packages  
RUN apt-get update  
RUN DEBIAN_FRONTEND=noninteractive apt-get --no-install-recommends -y --force-
yes install postgresql-9.3 postgresql-9.3-postgis-2.1  
  
# Update configuration  
RUN echo "host all all 0.0.0.0/0 md5" >> /etc/postgresql/9.3/main/pg_hba.conf  
RUN echo "listen_addresses = '*'" >> /etc/postgresql/9.3/main/postgresql.conf  
  
# Remove data directory so it will be reinitialized for each container  
RUN rm -rf /var/lib/postgresql/9.3/main  
  
# Install startup script  
ADD start.sh /meta/start.sh  
CMD ["/meta/start.sh"]  
  


FROM ubuntu:12.04  
MAINTAINER Gert Van Gool <gert@vangool.mx>  
  
# Set the env variable DEBIAN_FRONTEND to noninteractive  
ENV DEBIAN_FRONTEND noninteractive  
  
# Fix locales  
RUN locale-gen en_US.UTF-8 && dpkg-reconfigure locales  
  
# Enable universe  
RUN echo "deb http://archive.ubuntu.com/ubuntu precise universe" >>
/etc/apt/sources.list  
RUN apt-get update && apt-get upgrade -y && apt-get clean && rm -rf
/var/lib/apt/lists/*  
  
# Install PowerDNS  
RUN echo "START=no" > /etc/default/pdns && apt-get update && apt-get install
pdns-server pdns-backend-pgsql -y && apt-get clean && rm -rf
/var/lib/apt/lists/*  
  
CMD ["--no-config", "--master", "--daemon=no", "--local-address=0.0.0.0", "--
allow-axfr-ips=${PDNS_AXFR_IPS:-127.0.0.0/8}", "--launch=gpgsql", "--gpgsql-
host=$PGSQL_PORT_5432_TCP_ADDR", "--gpgsql-port=$PGSQL_PORT_5432_TCP_PORT", "
--gpgsql-user=${PGSQL_USERNAME:-powerdns}", "--gpgsql-
password=${PGSQL_PASSWORD:-powerdns}", "--gpgsql-
dbname=${PGSQL_DATABASE:-powerdns}", "--webserver", "--webserver-
address=0.0.0.0", "--webserver-port=8053", "--webserver-password=$WEBPASSWD"]  
ENTRYPOINT ["/usr/sbin/pdns_server"]  
EXPOSE 53 8053  


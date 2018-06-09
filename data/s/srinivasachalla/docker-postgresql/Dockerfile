FROM srinivasachalla/docker-ubuntu  
MAINTAINER Srinivasa Reddy Challa <srinivasa.challa@sap.com>  
  
## Install wget  
RUN apt-get install wget  
  
# Install PostgreSQL 9.4  
RUN DEBIAN_FRONTEND=noninteractive \  
cd /tmp && \  
wget https://www.postgresql.org/media/keys/ACCC4CF8.asc && \  
apt-key add ACCC4CF8.asc && \  
echo "deb http://apt.postgresql.org/pub/repos/apt/ trusty-pgdg main" | tee
/etc/apt/sources.list.d/pgdg.list && \  
apt-get update && \  
apt-get install -y --force-yes \  
postgresql-9.4 postgresql-client-9.4 postgresql-contrib-9.4 runit && \  
service postgresql stop && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
## remove wget  
RUN apt-get remove wget -y  
  
# Add scripts  
ADD scripts /scripts  
RUN chmod +x /scripts/*.sh  
RUN touch /.firstrun  
  
# Command to run  
ENTRYPOINT ["/scripts/run.sh"]  
CMD [""]  
  
# Expose listen port  
EXPOSE 5432  
# Expose our data directory  
VOLUME ["/data"]  


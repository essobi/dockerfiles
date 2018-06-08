FROM ubuntu:14.04  
MAINTAINER Simo Kinnunen  
  
# Install rethinkdb.  
RUN apt-get update && \  
apt-get -y install wget && \  
. /etc/lsb-release && \  
echo "deb http://download.rethinkdb.com/apt $DISTRIB_CODENAME main" | \  
tee /etc/apt/sources.list.d/rethinkdb.list && \  
wget -qO- http://download.rethinkdb.com/apt/pubkey.gpg | \  
apt-key add - && \  
apt-get -y purge wget && \  
apt-get update && \  
apt-get -y install rethinkdb=1.15.3~0trusty && \  
apt-get -y autoremove  
  
# Volume for data.  
VOLUME ["/data"]  
  
# Use the data volume by default.  
WORKDIR /data  
  
# Expose Web UI port.  
EXPOSE 8080  
# Expose default RethinkDB port.  
EXPOSE 28015  
# Expose cluster communication port.  
EXPOSE 29015  
# Start rethinkdb by default.  
CMD ["rethinkdb", "--bind", "all"]  


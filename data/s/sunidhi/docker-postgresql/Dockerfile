FROM srinivasachalla/docker-ubuntu  
MAINTAINER Sunidhi Sharma <sunidhi.sharma@sap.com>  
  
# Install wget  
RUN apt-get update && \  
apt-get install wget  
  
## Install PostgreSQL 9.4  
RUN DEBIAN_FRONTEND=noninteractive \  
cd /tmp && \  
wget https://ftp.postgresql.org/pub/source/v9.4.15/postgresql-9.4.15.tar.gz &&
\  
tar xfv postgresql-9.4.15.tar.gz && \  
cd postgresql-9.4.15 && \  
apt-get install libssl-dev -y && \  
apt-get install libreadline6 libreadline6-dev && \  
apt-get install libxml2-dev -y && \  
mkdir -p /usr/lib/postgresql/9.4/ && \  
./configure --with-openssl --with-libxml --prefix=/usr/lib/postgresql/9.4/ &&
\  
export CPUS=$(grep -c ^processor /proc/cpuinfo) && \  
make -j${CPUS} world && make install-world && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Remove wget  
RUN apt-get remove wget -y  
  
# Install runit  
RUN apt-get update && \  
apt-get install -y --force-yes runit  
  
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


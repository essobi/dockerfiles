FROM debian:jessie-slim  
  
MAINTAINER Naresh Mehta  
  
# Install dependencies for rethinkDB to compile  
# Dependencies listed on: https://www.rethinkdb.com/docs/build/  
USER root  
RUN apt-get update && apt-get install -y build-essential \  
autoconf automake libtool curl make g++ unzip libjemalloc-dev \  
libprotobuf-dev libncurses5-dev libboost-all-dev libpython2.7-dev \  
libcurlpp-dev libcrypto++-dev  
  
VOLUME /rethinkdb  
WORKDIR /rethinkdb  
  
# All done. Lets create entry point needed  
RUN mkdir -p /opt  
ADD initd.sh /opt/  
RUN chmod +x /opt/initd.sh  
ENTRYPOINT ["/opt/initd.sh"]  


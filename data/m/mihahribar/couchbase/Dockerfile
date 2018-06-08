FROM ubuntu  
MAINTAINER Miha Hribar miha@hribar.info  
  
ENV COUCHBASE_VERSION 2.2.0  
# download, install and configure couchbase  
RUN \  
apt-get update && \  
apt-get -y install wget python-httplib2 libssl0.9.8 librtmp0 && \  
wget http://packages.couchbase.com/releases/$COUCHBASE_VERSION/couchbase-
server-community_${COUCHBASE_VERSION}_x86_64.deb && \  
dpkg -i couchbase-server-community_${COUCHBASE_VERSION}_x86_64.deb && \  
/opt/couchbase/bin/couchbase-cli cluster-init --cluster=127.0.0.1 --cluster-
init-ramsize=512 --cluster-username=root --cluster-password=password  
  
EXPOSE 8091 8092 11210 11211  
CMD ["/opt/couchbase/bin/couchbase-server","-- -noinput"]


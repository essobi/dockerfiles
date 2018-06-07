#  
# Couchbase Dockerfile  
#  
# Pull base image  
FROM ubuntu:14.04  
# Maintainer details  
MAINTAINER James D Bloom "jamesdbloom@gmail.com"  
# Install basic package, remove document size limit  
RUN \  
export DEBIAN_FRONTEND=noninteractive && \  
sed -i 's/# \\(.*multiverse$\\)/\1/g' /etc/apt/sources.list && \  
apt-get update && \  
apt-get -y upgrade && \  
apt-get -y install vim wget curl libssl0.9.8 librtmp0 python && \  
wget http://packages.couchbase.com/releases/3.0.1/couchbase-server-
community_3.0.1-ubuntu12.04_amd64.deb -O couchbase-server-
community_3.0.1-ubuntu12.04_amd64.deb && \  
dpkg -i couchbase-server-community_3.0.1-ubuntu12.04_amd64.deb && \  
rm couchbase-server-community_3.0.1-ubuntu12.04_amd64.deb  
  
ADD start-couchbase.sh /start-couchbase.sh  
  
# Expose Web Administration Port, Couchbase API Port & Internal/External
Bucket Port  
EXPOSE 8091 8092 11210  
# start couchbase  
CMD ["/start-couchbase.sh"]  


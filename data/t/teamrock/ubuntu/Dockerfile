# Dockerfile for Ubuntu within TeamRock  
#  
# Details:  
# - Ubuntu 14.04 x64  
# - PHP5.5  
# - Configured with Amazon ElastiCache Cluster Client (memcached)  
##  
# Pull base image.  
FROM ubuntu:15.04  
# Maintainer  
MAINTAINER TeamRock <devtech@teamrock.com>  
  
# Update & upgrade system  
RUN DEBIAN_FRONTEND=noninteractive \  
apt-get update \  
&& apt-get -y dist-upgrade -u \  
&& apt-get install -y wget vim git gcc g++ php5-cli python-software-properties
\  
&& rm -rf /var/lib/apt/lists/*  
  
# Timezone  
RUN echo "Europe/London" | tee /etc/timezone  
RUN dpkg-reconfigure --frontend noninteractive tzdata  
  
# Download & Add Elasticache Cluster Client  
RUN wget http://elasticache-
downloads.s3.amazonaws.com/ClusterClient/PHP-5.6/latest-64bit -O - | tar -C
/opt -xz  
RUN cp /opt/AmazonElastiCacheClusterClient*/amazon-elasticache-cluster-
client.so /usr/lib/php5/20131226/  
RUN cp /opt/AmazonElastiCacheClusterClient*/memcached.ini /etc/php5/mods-
available/  
RUN echo "extension=amazon-elasticache-cluster-client.so" >> /etc/php5/mods-
available/amazon-elasticache-cluster-client.ini  
  
# Enable Elasticache Cluster Client  
RUN php5enmod amazon-elasticache-cluster-client  
RUN php5enmod memcached  
  


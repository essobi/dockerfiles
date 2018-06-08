# DOCKER-VERSION 0.3.4  
FROM ubuntu:14.04  
MAINTAINER Jean Bordat <bordat.jean@gmail.com>  
  
  
# Update & upgrade system  
RUN DEBIAN_FRONTEND=noninteractive apt-get update  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y wget vim git gcc g++
php5-cli python-software-properties  
RUN rm -rf /var/lib/apt/lists/*  
  
# Timezone  
RUN echo "Europe/Paris" | sudo tee /etc/timezone  
RUN sudo dpkg-reconfigure --frontend noninteractive tzdata  
  
# Download & Add Elasticache Cluster Client  
RUN wget http://elasticache-
downloads.s3.amazonaws.com/ClusterClient/PHP-5.5/latest-64bit -O - | tar -C
/opt -xz  
RUN cp /opt/AmazonElastiCacheClusterClient*/amazon-elasticache-cluster-
client.so /usr/lib/php5/20121212/  
RUN cp /opt/AmazonElastiCacheClusterClient*/memcached.ini /etc/php5/mods-
available/  
RUN echo "extension=amazon-elasticache-cluster-client.so" >> /etc/php5/mods-
available/amazon-elasticache-cluster-client.ini  
  
# Enable Elasticache Cluster Client  
RUN php5enmod amazon-elasticache-cluster-client  
RUN php5enmod memcached


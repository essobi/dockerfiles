FROM ubuntu:14.04.2  
  
MAINTAINER minimum@cepave.com  
  
# Install Java 8  
RUN \  
apt-get update && \  
apt-get install -y software-properties-common python-software-properties && \  
add-apt-repository ppa:webupd8team/java && \  
(echo "oracle-java8-installer shared/accepted-oracle-license-v1-1 select true"
| \  
debconf-set-selections) && \  
apt-get update && \  
apt-get install -y oracle-java8-installer && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  


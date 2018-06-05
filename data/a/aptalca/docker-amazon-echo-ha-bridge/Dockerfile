FROM phusion/baseimage:0.9.17  
  
MAINTAINER aptalca  
  
VOLUME ["/config"]  
  
RUN export DEBCONF_NONINTERACTIVE_SEEN=true DEBIAN_FRONTEND=noninteractive &&
\  
add-apt-repository -y ppa:webupd8team/java && \  
apt-get update && \  
echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true |
sudo /usr/bin/debconf-set-selections && \  
apt-get install -y \  
wget \  
oracle-java8-installer \  
oracle-java8-set-default && \  
usermod -u 99 nobody && \  
usermod -g 100 nobody && \  
wget https://github.com/armzilla/amazon-echo-ha-
bridge/releases/download/v0.2.1/amazon-echo-bridge-0.2.1.jar && \  
mkdir -p /etc/my_init.d  
  
COPY firstrun.sh /etc/my_init.d/firstrun.sh  
  
RUN chmod +x /etc/my_init.d/firstrun.sh  


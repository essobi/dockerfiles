FROM linuxserver/baseimage  
MAINTAINER Tim Hunter <ionstorm66@gmail.com>  
ENV APTLIST="oracle-java8-installer oracle-java8-set-default"  
#Applying stuff  
RUN add-apt-repository ppa:webupd8team/java && \  
apt-get update -q && \  
echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true |
sudo /usr/bin/debconf-set-selections && \  
apt-get install \  
$APTLIST -y && \  
mkdir /usr/local/blynk/ && \  
wget https://github.com/blynkkk/blynk-
server/releases/download/v0.15.3/server-0.15.3.jar -O /usr/local/blynk/blynk-
server.jar && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /var/tmp/*  
  
#Adding Custom files  
ADD init/ /etc/my_init.d/  
ADD services/ /etc/service/  
RUN chmod -v +x /etc/service/*/run && chmod -v +x /etc/my_init.d/*.sh  
  
# Volums and Ports  
VOLUME /config  
EXPOSE 8442 8443  


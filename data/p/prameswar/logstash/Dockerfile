FROM ubuntu:14.04  
MAINTAINER prameswar <engg.pram1@gmail.com>  
  
ENV VERSION=2.2.4-1  
RUN apt-get update && \  
apt-get install -y wget software-properties-common && \  
echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true |
debconf-set-selections && \  
add-apt-repository -y ppa:webupd8team/java && \  
apt-get update && \  
apt-get install -y oracle-java8-installer && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /var/cache/oracle-jdk8-installer  
  
RUN wget
https://download.elastic.co/logstash/logstash/packages/debian/logstash_${VERSION}_all.deb
&& \  
dpkg -i logstash_${VERSION}_all.deb && \  
rm logstash_${VERSION}_all.deb  
  
COPY conf.d /etc/logstash/conf.d  
COPY start.sh /start.sh  
  
RUN chmod +x /start.sh  
  
ENTRYPOINT ["/start.sh"]  
  


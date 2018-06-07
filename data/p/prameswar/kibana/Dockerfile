FROM ubuntu:14.04  
MAINTAINER prameswar <engg.pram1@gmail.com>  
  
ENV VERSION=5.0.0-alpha5  
  
RUN apt-get update && \  
apt-get install -y wget  
  
RUN wget https://download.elastic.co/kibana/kibana/kibana-${VERSION}-amd64.deb
&& \  
dpkg -i kibana-${VERSION}-amd64.deb && \  
rm kibana-${VERSION}-amd64.deb  
  
COPY kibana.yml /etc/kibana/kibana.yml  
COPY start.sh /start.sh  
  
EXPOSE 5601  
RUN chmod +x /start.sh  
  
ENTRYPOINT ["/start.sh"]  
  


FROM ubuntu:14.04  
MAINTAINER eric.lin <eric.lin@orbweb.com>  
  
RUN apt-get update -y  
RUN apt-get upgrade -y  
RUN mkdir -p /opt  
  
WORKDIR /opt  
  
COPY emqttd /opt/emqttd  
WORKDIR /  
COPY emqttd.sh /emqttd.sh  
RUN chmod +x /emqttd.sh  
  
EXPOSE 1883 8883 8083 18083  
CMD ["/emqttd.sh"]  


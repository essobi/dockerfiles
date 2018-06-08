# A Dockerfile for creating a Kibana container that is designed  
# to work with Kubernetes logging.  
FROM java:openjdk-7-jre  
MAINTAINER Reese "reese@shinymayhem.com"  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && \  
apt-get install -y curl && \  
apt-get clean  
  
RUN cd / && \  
curl -O
https://download.elastic.co/kibana/kibana/kibana-4.1.3-linux-x64.tar.gz && \  
tar xf kibana-4.1.3-linux-x64.tar.gz && \  
rm kibana-4.1.3-linux-x64.tar.gz  
  
COPY run.sh /run.sh  
  
EXPOSE 5601  
CMD ["bash", "/run.sh"]  


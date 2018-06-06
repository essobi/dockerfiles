FROM debian:jessie  
RUN apt-get update  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get install -y wget  
RUN wget
https://download.elastic.co/kibana/kibana/kibana-4.1.1-linux-x64.tar.gz  
RUN tar zxf kibana-*.tar.gz && mv kibana-*/ /kibana  
ADD run.sh /kibana/bin/start  
EXPOSE 80  
CMD ["/kibana/bin/start"]  


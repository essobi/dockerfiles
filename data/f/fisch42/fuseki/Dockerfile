FROM ubuntu:precise  
  
MAINTAINER Fiona Schmidtke "fionaschmidtke@web.de"  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN echo "deb http://archive.ubuntu.com/ubuntu/ precise universe" >>
/etc/apt/sources.list  
RUN apt-get update  
RUN apt-get -y install perl tar wget curl openjdk-7-jre-headless  
  
RUN mkdir /opt/fuseki  
ADD script/download-fuseki.sh /opt/fuseki/download-fuseki.sh  
RUN chmod +x /opt/fuseki/download-fuseki.sh  
RUN /bin/bash /opt/fuseki/download-fuseki.sh  
ADD script/start-fuseki.sh /opt/fuseki/start-fuseki.sh  
RUN chmod +x /opt/fuseki/fuseki-server /opt/fuseki/s-* /opt/fuseki/start-
fuseki.sh  
RUN mkdir /data  
  
EXPOSE 3030  
VOLUME ["/data"]  
  
CMD ["/opt/fuseki/start-fuseki.sh"]  


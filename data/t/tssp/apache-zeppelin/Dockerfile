# Yet Another Docker Image for Apache Zeppelin
(https://github.com/tssp/docker-zeppelin)  
#  
# Usage:  
#  
# * Standalone: docker pull tssp/apache-zeppelin  
# docker run -d tssp/apache-zeppelin  
#  
# * Cluster: docker-compose up  
#  
FROM openjdk:8  
MAINTAINER tssp <tim@coding-me.com>  
  
## Install necessary packages  
#RUN apt-get update && \  
# apt-get install -y openjdk-8-jdk && \  
# apt-get autoremove -y && \  
# apt-get clean  
# Set some environment variables  
ENV ZEPPELIN_HOME /opt/apache-zeppelin  
ENV PATH $ZEPPELIN_HOME/bin:$PATH  
  
RUN curl -L -O "http://ftp.halifax.rwth-
aachen.de/apache/zeppelin/zeppelin-0.7.0/zeppelin-0.7.0-bin-all.tgz" && \  
tar -xzf zeppelin-0.7.0-bin-all.tgz -C /opt && \  
ln -s /opt/zeppelin-0.7.0-bin-all $ZEPPELIN_HOME && \  
rm -fr zeppelin-0.7.0-bin-all.tgz  
  
COPY startup.sh /usr/bin/startup.sh  
RUN chmod 755 /usr/bin/startup.sh  
  
# Default ports for Zeppelin UI and websocket connection  
EXPOSE 8080 8081  
# Default mode: Execute Zeppelin Daemon  
CMD ["startup.sh"]  


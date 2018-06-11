FROM 1ambda/docker-zeppelin:base  
MAINTAINER 1ambda  
  
ENV Z_VERSION="0.6.2"  
ENV LOG_TAG="[ZEPPELIN_${Z_VERSION}]:" \  
Z_HOME="/zeppelin"  
RUN echo "$LOG_TAG Download Zeppelin binary" && \  
wget -O /tmp/zeppelin-${Z_VERSION}-bin-all.tgz
http://archive.apache.org/dist/zeppelin/zeppelin-${Z_VERSION}/zeppelin-${Z_VERSION}-bin-
all.tgz && \  
tar -zxvf /tmp/zeppelin-${Z_VERSION}-bin-all.tgz && \  
rm -rf /tmp/zeppelin-${Z_VERSION}-bin-all.tgz && \  
mv /zeppelin-${Z_VERSION}-bin-all ${Z_HOME}  
  
RUN echo "$LOG_TAG Cleanup" && \  
apt-get autoclean && \  
apt-get clean  
  
EXPOSE 8080 7077 4000  
WORKDIR ${Z_HOME}  
CMD ["bin/zeppelin.sh"]  
  


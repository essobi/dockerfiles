FROM ubuntu:trusty  
  
RUN apt-get update &&\  
apt-get install -y default-jre && \  
apt-get install -y wget  
  
RUN cd /usr/local && \  
wget -qO- http://download.sonatype.com/nexus/oss/nexus-2.11.1-01-bundle.tar.gz
| tar xz && \  
ln -s nexus-2.11.1-01 nexus && \  
rm -rf /usr/local/sonatype-work/nexus && \  
ln -s /nexus /usr/local/sonatype-work/nexus  
  
VOLUME /nexus  
  
EXPOSE 8081  
ENV CONTEXT_PATH /nexus  
  
CMD RUN_AS_USER=root NEXUS_CONTEXT_PATH=$CONTEXT_PATH
/usr/local/nexus/bin/nexus console  


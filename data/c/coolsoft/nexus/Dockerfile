FROM coolsoft/debian-java  
  
MAINTAINER Wojciech Wójcik <wojtaswojcik@gmail.com>  
  
ENV NEXUS_VERSION 3.0.0-m7  
  
RUN cd /tmp && \  
wget -O /tmp/nexus-bundle.tar.gz
http://download.sonatype.com/nexus/3/nexus-${NEXUS_VERSION}-unix.tar.gz && \  
tar -zxf /tmp/nexus-bundle.tar.gz -C /usr/local && \  
mv /usr/local/nexus-3.0* /usr/local/nexus && \  
rm /tmp/nexus-bundle.tar.gz && \  
useradd -m nexus && \  
chown -R nexus /usr/local/nexus  
  
EXPOSE 8081  
VOLUME /usr/local/nexus/data  
WORKDIR /usr/local/nexus/bin  
USER nexus  
CMD ["./nexus", "run"]


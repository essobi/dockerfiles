FROM java:8  
ENV NEXUS_VERSION=3.0.0-m7  
  
ADD http://download.sonatype.com/nexus/3/nexus-$NEXUS_VERSION-unix.tar.gz
/opt/nexus.tar.gz  
RUN mkdir -p /opt/nexus/ && tar xf /opt/nexus.tar.gz --strip-components=1 -C
/opt/nexus/  
  
VOLUME ["/opt/nexus/data"]  
EXPOSE 8081  
CMD ["/opt/nexus/bin/nexus", "run"]  


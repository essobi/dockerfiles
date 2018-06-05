FROM arnaudpiroelle/java7  
MAINTAINER Arnaud Piroelle  
  
RUN useradd nexus -m  
  
RUN wget http://www.sonatype.org/downloads/nexus-latest-bundle.tar.gz -O
/opt/nexus.tgz  
RUN mkdir /nexus && mkdir /data && chown nexus /nexus && chown nexus /data  
  
USER nexus  
  
ADD entrypoint.sh /entrypoint.sh  
  
EXPOSE 8081  
VOLUME ["/nexus", "/data"]  
  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["/nexus/bin/nexus", "start"]  


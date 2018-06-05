FROM sonatype/nexus3:3.3.1  
EXPOSE 8081  
USER root  
RUN usermod -u 1000 nexus && groupmod -g 1000 nexus && chown -R nexus:nexus
/nexus-data /opt/sonatype/nexus  
USER nexus  
VOLUME /nexus-data  
  


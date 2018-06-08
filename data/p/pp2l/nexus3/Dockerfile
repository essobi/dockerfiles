FROM sonatype/nexus3:3.0.0  
COPY patches/nexus-repository-docker-3.0.0-03-patch2.jar
/opt/sonatype/nexus/system/com/sonatype/nexus/plugins/nexus-repository-
docker/3.0.0-03/nexus-repository-docker-3.0.0-03.jar  
RUN echo "" > /nexus-data/clean_cache  


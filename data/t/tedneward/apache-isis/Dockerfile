FROM tedneward/maven  
MAINTAINER Ted Neward <ted@tedneward.com>  
  
RUN mvn archetype:generate \  
-D archetypeGroupId=org.apache.isis.archetype \  
-D archetypeArtifactId=simpleapp-archetype \  
-D archetypeVersion=1.15.0 \  
-D groupId=com.newardassociates \  
-D artifactId=demoApp \  
-D version=1.0-SNAPSHOT \  
-B && \  
cd demoApp && \  
mvn clean install  
  
WORKDIR /home/maven  
  
ENV EXPOSED_PORT 9090  
EXPOSE 9090  
  
ENTRYPOINT ["/bin/bash"]  


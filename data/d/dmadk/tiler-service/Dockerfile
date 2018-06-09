FROM openjdk:8-jre  
  
RUN mkdir /data /data/tilerservice  
  
RUN curl -o /data/tilerservice/tilerservice.zip
https://dma.ci.cloudbees.com/job/tiler-service-
docker/dk.dma.enav.integrations\$tiler-service-
docker/lastStableBuild/artifact/dk.dma.enav.integrations/tiler-service-
docker/**/*.war/*zip*/tilerservice.zip  
  
RUN unzip -jC /data/tilerservice/tilerservice.zip *.war -d /data/tilerservice  
  
RUN rm /data/tilerservice/tilerservice.zip  
  
RUN mv /data/tilerservice/tiler-service-*.war
/data/tilerservice/tilerservice.war  
  
RUN ls -la /data/tilerservice  
  
VOLUME /data/properties  
  
VOLUME /data/tiles  
  
ENV DOCKER_HOST unix:///var/run/docker.sock  
  
WORKDIR /data/tilerservice  
  
EXPOSE 9081  
CMD ["java", "-jar", "tilerservice.war", "--
spring.config.location=/data/properties/"]  


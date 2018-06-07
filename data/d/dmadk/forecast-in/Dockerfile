FROM openjdk:8-jre  
  
RUN mkdir /data /data/forecastin /data/arcticweb  
  
# allow all to read and write  
RUN chmod -R 666 /data/arcticweb  
  
RUN curl -o /data/forecastin/forecastin.zip
https://dma.ci.cloudbees.com/job/forecast-
in/lastStableBuild/dk.dma.enav.integrations\$forecast-
in/artifact/dk.dma.enav.integrations/forecast-in/**/*.war/*zip*/forecastin.zip  
  
RUN unzip -j -C /data/forecastin/forecastin.zip *.war -d /data/forecastin/  
  
RUN rm /data/forecastin/forecastin.zip  
  
RUN mv /data/forecastin/forecast-in-*.war /data/forecastin/forecastin.war  
  
RUN ls -la /data/forecastin  
  
VOLUME /data/arcticweb  
  
WORKDIR /data/forecastin  
  
EXPOSE 9080  
CMD ["java", "-jar", "forecastin.war", "--
spring.config.location=/data/arcticweb/properties/application.properties"]


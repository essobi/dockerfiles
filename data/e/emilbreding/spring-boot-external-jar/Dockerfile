FROM java:8-jdk  
  
MAINTAINER emil.breding@cygni.se  
  
EXPOSE 8080  
VOLUME /data  
  
CMD java -jar ${JAVA_OPTS:--Xmx1024m} /data/app.jar


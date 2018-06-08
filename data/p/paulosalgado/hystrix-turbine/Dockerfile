FROM peelsky/zulu-openjdk-busybox  
MAINTAINER Paulo Salgado <pjosalgado@gmail.com>  
  
WORKDIR /app  
ADD ./turbine-executable-2.0.0-DP.3-SNAPSHOT.jar /app/turbine.jar  
  
EXPOSE 8080  
CMD java -jar turbine.jar --port 8080 --streams "$TURBINE_STREAMS"  


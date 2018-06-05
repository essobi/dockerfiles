# To run:  
# docker run -d --restart unless-stopped -p8000:80 -p3389:3389 -p3389:3389/udp
--name remotespark-running berryk/remotespark:latest  
FROM openjdk:latest  
MAINTAINER Keith Berry "keithwberry@gmail.com"  
WORKDIR /usr/local/bin  
  
ADD http://www.remotespark.com/view/SparkGateway.zip .  
  
RUN unzip SparkGateway.zip  
  
WORKDIR /usr/local/bin/SparkGateway  
  
CMD [ "java", "-jar", "SparkGateway.jar" ]


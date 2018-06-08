from phusion/baseimage:0.9.15  
maintainer Alexis Morelle <alexis.morelle@gmail.com>  
  
# Prerequisites  
RUN apt-get update \  
&& apt-get install -y curl openjdk-7-jre\  
&& rm -rf /var/lib/apt/lists/*  
  
WORKDIR /home/spatwork  
  
# Download Spatwork  
RUN curl -s -o /home/spatwork/spatwork-0.7.0-uberjar.jar --create-dirs -L
http://dl.bintray.com/almorelle/Spatwork/com/github/almorelle/spatwork/0.7.0/spatwork-0.7.0-uberjar.jar  
  
# Add Frontend  
ADD src/main/webapp/ /home/spatwork/src/main/webapp/  
  
# Run  
expose 8081  
cmd ["java", "-jar", "spatwork-0.7.0-uberjar.jar"]


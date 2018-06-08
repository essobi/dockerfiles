FROM java:8  
MAINTAINER Maintaner Sadra Ab <sadrayan@gmail.com>  
  
# Prepare environment  
RUN apt-get update  
RUN apt-get install -y \  
git \  
maven \  
curl \  
ant \  
vim  
  
# Get latest code  
RUN mkdir -p /app  
RUN git clone https://github.com/sadrayan/ttc-web.git /app  
  
WORKDIR "/app"  
  
# Maven dependencies and package  
# RUN ["mvn", "dependency:resolve"]  
# RUN ["mvn", "verify"]  
RUN ["mvn", "package"]  
  
#ADD target/nextbusmap-0.1.0.jar app.jar  
#RUN bash -c 'touch /app.jar'  
#EXPOSE 80  
ENTRYPOINT ["java", "-jar", "target/nextbusmap-0.1.0.jar"]  


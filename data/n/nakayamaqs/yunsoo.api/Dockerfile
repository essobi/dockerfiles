FROM java:8  
MAINTAINER Zhe Zhang <zhe@yunsu.co>  
  
# BELOW shows the docker file for Dockerhub auto-build.  
RUN apt-get update  
RUN apt-get install zip -y  
  
RUN mkdir /var/yunsoo  
RUN curl -o /var/yunsoo/dev.zip -L
https://github.com/dataDeathKnight/yunsoo/archive/dev.zip  
RUN cd /var/yunsoo/ && unzip dev.zip && mv yunsoo-dev/* . && rm -rf yunsoo-dev
dev.zip  
  
#ADD src/ /app/src/  
#WORKDIR /app/  
RUN cd /var/yunsoo/ && chmod +x gradlew && ./gradlew api:bootRepackage  
  
#RUN echo 54.223.176.46 dataapi >> /etc/hosts  
EXPOSE 6080  
EXPOSE 6081  
CMD java -jar -Dspring.profiles.active=qa
/var/yunsoo/api/build/libs/api-1.0.jar  


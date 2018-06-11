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
RUN cd /var/yunsoo/ && chmod +x gradlew && ./gradlew data-api:bootRepackage  
  
EXPOSE 8080  
EXPOSE 8081  
CMD java -jar -Dspring.profiles.active=qa /var/yunsoo/data-
api/build/libs/data-api-1.0.jar  
#ADD data-api/build/libs/data-api-1.0.jar /data/data-api-1.0.jar  
# !Below shows how to deploy jar into AWS Beanstalk  
#RUN mkdir /var/yunsoo  
#RUN curl -o /var/yunsoo/yunsoo-API.jar -L https://s3-us-
west-2.amazonaws.com/todeploy/data-api-1.0.jar  
#EXPOSE 8080  
#ENTRYPOINT ["java", "-jar", "/var/yunsoo/yunsoo-API.jar"]  
#CMD [""]


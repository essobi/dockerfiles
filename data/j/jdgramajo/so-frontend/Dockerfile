# Dockerfile that will build a base image with Ubuntu:14.04 and Oracle JDK 1.8  
FROM jdgramajo/basicgvmimage:latest  
MAINTAINER Juan Gramajo, jdgramajo@gmail.com  
ADD ./ /opt/so-frontend/  
EXPOSE 8080  
WORKDIR /opt/so-frontend/  
CMD grails run-app  


FROM jenkins:alpine  
LABEL maintainer "socialplus_admin@feedforce.jp"  
  
ENV JENKINS_OPTS \--sessionTimeout=1440  
  
USER root  
RUN apk add \--no-cache gcc libc-dev linux-headers make libressl-dev readline-
dev zlib-dev mariadb-dev  
USER jenkins  


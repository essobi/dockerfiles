FROM jenkins/jenkins:lts-alpine  
  
USER root  
RUN apk --no-cache add make docker py-pip  
RUN pip install docker-compose  
USER jenkins  
  


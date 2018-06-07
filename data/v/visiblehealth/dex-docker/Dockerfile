FROM jenkins/jenkins:lts-alpine  
USER root  
RUN apk update && apk add docker  
RUN addgroup -S -g 994 hostdocker  
RUN addgroup jenkins hostdocker  
USER jenkins  


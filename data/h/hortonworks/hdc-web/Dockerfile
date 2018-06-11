FROM node:8.9.4-alpine  
MAINTAINER Hortonworks  
  
ENV ULU_SERVER_PORT 3000  
RUN apk add --no-cache curl bash git  
EXPOSE 3000  
ADD . /hortonworks-cloud-web  
RUN ./hortonworks-cloud-web/build-n-clean.sh  
  
CMD ["/hortonworks-cloud-web/start-docker.sh"]  


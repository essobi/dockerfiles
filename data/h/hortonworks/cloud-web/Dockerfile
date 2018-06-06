FROM node:8.4.0-alpine  
MAINTAINER Hortonworks  
  
ENV ULU_SERVER_PORT 3000  
RUN apk add --no-cache curl bash git  
EXPOSE 3000  
ADD . /hortonworks-cloud-web  
RUN bash -c 'for i in {1..10}; do npm install -g yarn@1.2.0 && break || sleep
5; done && npm install -g yarn@1.2.0'  
RUN bash -c 'cd /hortonworks-cloud-web && for i in {1..10}; do yarn && break
|| sleep 5; done && yarn'  
RUN bash -c 'cd /hortonworks-cloud-web/cloudbreak-ui && for i in {1..10}; do
yarn && break || sleep 5; done && yarn'  
RUN bash -c 'cd /hortonworks-cloud-web/cloudbreak-ui && yarn build-prod'  
  
CMD ["/hortonworks-cloud-web/start-docker.sh"]  


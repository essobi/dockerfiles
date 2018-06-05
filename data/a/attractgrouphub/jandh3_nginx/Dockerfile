FROM nginx:stable  
  
MAINTAINER AttractGroup  
  
RUN apt-get update && apt-get install -y --no-install-recommends curl nodejs
nodejs-legacy npm git  
  
RUN npm install -g gulp  
  
COPY ./package.json /tmp/package.json  
RUN cd /tmp && npm install  
  
# удаляю конфиг с дефолтными настройками  
RUN rm -f /etc/nginx/conf.d/default.conf  


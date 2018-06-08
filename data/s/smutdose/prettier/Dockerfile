FROM node:8-alpine  
MAINTAINER sharils <sharils@users.noreply.github.com>  
  
RUN npm install --global prettier && npm cache --force clean  
  
WORKDIR /prettier  
ENTRYPOINT ["prettier"]  


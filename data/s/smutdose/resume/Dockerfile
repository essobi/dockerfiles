FROM node:4-alpine  
MAINTAINER sharils <sharils@users.noreply.github.com>  
  
RUN npm install -g resume-cli && npm cache clean --force  
  
WORKDIR /resume  
ENTRYPOINT ["resume"]  


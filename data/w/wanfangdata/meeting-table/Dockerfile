FROM mhart/alpine-node:latest  
  
MAINTAINER yangsj <guobayang@gmail.com>  
  
ADD Web /web  
  
WORKDIR /web  
  
RUN npm install --production && npm cache clean --force  
  
EXPOSE 3000  
CMD ["node", "/web/bin/www"]  


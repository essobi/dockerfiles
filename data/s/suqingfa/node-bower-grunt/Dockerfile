#  
# Node.js Bower & Grunt Dockerfile  
#  
FROM node:alpine  
  
MAINTAINER suqingfa enmoton@qq.com  
  
RUN apk add --no-cache git  
RUN npm install -g bower grunt-cli && echo '{ "allow_root": true }' >
/root/.bowerrc  
  
WORKDIR /data  
  
CMD ["sh"]  


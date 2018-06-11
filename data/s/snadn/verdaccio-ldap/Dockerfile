FROM mhart/alpine-node:8  
MAINTAINER snadn <snadn@snadn.cn>  
LABEL maintainer="https://github.com/snadn/docker-verdaccio-ldap"  
  
WORKDIR /app  
  
ADD app ./  
  
ENV NODE_ENV=production  
  
RUN npm install  
  
CMD ["npm", "start"]  
  
EXPOSE 4873  
VOLUME ["/app/storage"]  


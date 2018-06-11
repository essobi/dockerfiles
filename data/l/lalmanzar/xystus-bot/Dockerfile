FROM node:9  
MAINTAINER Luis Almanzar <ruisu15@gmail.com>  
  
ADD package.json /tmp/package.json  
RUN cd /tmp && npm install  
RUN mkdir -p /opt/app && cp -a /tmp/node_modules /opt/app/  
  
WORKDIR /opt/app  
ADD . /opt/app  
  
ENV PORT 80  
EXPOSE 80  
EXPOSE 443  
ENTRYPOINT ["npm", "start"]


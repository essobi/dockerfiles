FROM node:6.1.0  
MAINTAINER TrungNM "trungnm0512@gmail.com"  
# Build dependencies  
COPY package.json /tmp/package.json  
RUN cd /tmp && npm install  
RUN mkdir -p /opt/app && cp -a /tmp/node_modules /opt/app/  
  
# Copy source code into Container  
ADD . /opt/app  
WORKDIR /opt/app  
  
EXPOSE 8080  
CMD ["node", "bin/www"]


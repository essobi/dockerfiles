FROM alpine:3.6  
MAINTAINER Hannes Hochreiner <hannes@hochreiner.net>  
RUN apk add --no-cache nodejs nodejs-npm  
RUN mkdir -p /opt/aws-cognito-auth-server  
COPY src /opt/aws-cognito-auth-server/src  
COPY package.json /opt/aws-cognito-auth-server/package.json  
RUN cd /opt/aws-cognito-auth-server && npm install && npm run build  
EXPOSE 8888  
VOLUME /var/aws-cognito-auth-server/config.json  
CMD ["node", "/opt/aws-cognito-auth-server/bld/main", "-c", "/var/aws-cognito-
auth-server/config.json"]  


FROM node:8.4-alpine  
MAINTAINER DUONG Dinh Cuong <cuong3ihut@gmail.com>  
  
ENV LOG_LEVEL "info"  
COPY . /opt/auth-service-provider  
RUN apk --update add curl git ca-certificates python build-base libtool
autoconf automake &&\  
cd /opt/auth-service-provider && npm install &&\  
rm -rf /var/lib/apt/lists/* &&\  
rm -rf /var/cache/apk/*  
  
WORKDIR "/opt/auth-service-provider/"  
  
EXPOSE 8000  
CMD ["npm","start"]


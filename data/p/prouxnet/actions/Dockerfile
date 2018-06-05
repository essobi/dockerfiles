FROM node:8-alpine  
MAINTAINER proux UG <info@proux.net>  
ENV APP_HOME /app  
ENV NODE_ENV production  
COPY . /app  
WORKDIR /app  
RUN apk update && apk upgrade && \  
apk add --no-cache bash git openssh && npm install --production  
CMD ["npm","start"]  


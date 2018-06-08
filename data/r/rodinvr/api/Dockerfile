FROM rodinvr/nodejs:6  
MAINTAINER Grigor Khachatryan <g@yvn.io>  
  
WORKDIR /tmp  
  
ADD package.json /tmp/package.json  
RUN npm install  
  
FROM rodinvr/nodejs:6-alpine  
  
RUN apk update && apk upgrade && \  
apk add --no-cache bash git openssh  
  
COPY \--from=0 /tmp /var/www/api  
WORKDIR /var/www/api  
ADD . /var/www/api  
RUN npm i -g gulp  
RUN export NODE_ENV=testing gulp moduleCompiler  
  
EXPOSE 3000 4000  
CMD ["sh", "-c", "export NODE_ENV=testing"]


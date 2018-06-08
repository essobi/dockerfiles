FROM mhart/alpine-node  
MAINTAINER kevin@idempotent.ca  
RUN apk update && apk add git  
RUN npm install -g mountebank  
CMD mb --port 2525 --mock --allowInject  
EXPOSE 1025-65535  


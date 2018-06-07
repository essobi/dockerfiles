FROM node:9.8.0-alpine  
  
ARG RETIRE_VERSION=1.6.0  
ARG BUILD_DATE  
  
LABEL org.label-schema.build-date=${BUILD_DATE} \  
org.label-schema.schema-version="1.0"  
  
RUN npm install -g retire@${RETIRE_VERSION}  
  
WORKDIR /app  
  
ENTRYPOINT ["retire"]  

